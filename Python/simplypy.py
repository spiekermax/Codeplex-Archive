# (c) Max Spiekermann, 2016
# Use this to add a basic node system to pygame
# It simplifies the usage of pygame with python

import pygame
from maxamathics import devidable

class node():


	# Defines the current position of the node
	pos_x = 0.0
	pos_y = 0.0
	# Defines the current scale of the node
	scl_x = 0.0
	scl_y = 0.0
	# Colors
	clr_r = 255
	clr_g = 255
	clr_b = 255

	# Returns wether the node is ready for a drag-and-drop operation
	drad_ready = False
	# Dragdrop variable, which returns the difference between the node's visual origin and the mouse-location
	mouserelative_x = 0.0
	mouserelative_y = 0.0

	# The visual output of the node -> How it looks like
	n_visual = None
	n_inputs = 0
	n_outputs = 0
	# Selection rectangle
	n_selrect_sclx = 0.0
	n_selrect_scly = 0.0
	n_selrect_posx = 0.0
	n_selrect_posy = 0.0
	n_selrect2_sclx = 0.0
	n_selrect2_scly = 0.0
	n_selrect2_posx = 0.0
	n_selrect2_posy = 0.0

	# The window it is drawn in
	env_window = None
	env_background = []
	env_scr_w = 0.0
	env_scr_h = 0.0

	connect_ready = False
	inputvectorsource = []
	drawto = []



	# Require basics to draw a rectangle with pygame
	def __init__ (self, env_window, root = [pos_x, pos_y], scale = [scl_x, scl_y], color = [clr_r, clr_g, clr_b], backgroundcolor = [0, 0, 0], inputs = 1, outputs = 1):
		self.pos_x = root[0]
		self.pos_y = root[1]
		self.scl_x = scale[0]
		self.scl_y = scale[1]
		self.clr_r = color[0]
		self.clr_g = color[1]
		self.clr_b = color[2]
		self.n_inputs = inputs
		self.n_outputs = outputs
		self.env_window = env_window
		self.env_background = backgroundcolor
		self.n_visual = pygame.draw.rect(env_window, [255, 255, 255], [root[0], root[1], scale[0], scale[1]])


	# Shows a selection rectangle, when node is clicked
	def select (self, event):
		if (event.type == pygame.MOUSEBUTTONDOWN and
			event.pos[0] >= self.pos_x and event.pos[0] <= self.pos_x+self.scl_x-5 and
			event.pos[1] >= self.pos_y and event.pos[1] <= self.pos_y+self.scl_y):
			#
			self.n_selrect_sclx = self.scl_x + 12
			self.n_selrect_scly = self.scl_y + 12
			self.n_selrect2_sclx = self.scl_x + 6
			self.n_selrect2_scly = self.scl_y + 6
			#
			self.n_selrect_posx = self.pos_x + ((self.scl_x - self.n_selrect_sclx)/2)
			self.n_selrect_posy = self.pos_y + ((self.scl_x - self.n_selrect_sclx)/2)
			self.n_selrect2_posx = self.pos_x + ((self.scl_x - self.n_selrect2_sclx)/2)
			self.n_selrect2_posy = self.pos_y + ((self.scl_x - self.n_selrect2_sclx)/2)
			#
		elif (event.type == pygame.MOUSEBUTTONDOWN):
			self.n_selrect_sclx = 0.0
			self.n_selrect_scly = 0.0
			self.n_selrect_posx = 0.0
			self.n_selrect_posy = 0.0
			self.n_selrect2_sclx = 0.0
			self.n_selrect2_scly = 0.0
			self.n_selrect2_posx = 0.0
			self.n_selrect2_posy = 0.0



	# Sets the node's location - this function requires the possibility to read from all events -> place it in the for-loop
	# Snap ist nicht ricthig funktionabel
	def dragdrop (self, event, snap, grid, screenwidth, screenheight):
		self.env_scr_w = screenwidth
		self.env_scr_h = screenheight
		for n in range (0, self.n_outputs):
			if (event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= self.pos_x+self.scl_x-5 and event.pos[0] <= self.pos_x+self.scl_x-5+10 and
				event.pos[1] >= self.pos_y+(n+1)*15-10 and event.pos[1] <= self.pos_y+(n+1)*15-10-5+10):
				self.inputvectorsource = event.pos
				self.drawto = event.pos
				self.connect_ready = True
			elif (event.type == pygame.MOUSEBUTTONUP):
				self.connect_ready = False
		if (self.connect_ready == True and event.type == pygame.MOUSEMOTION):
			self.drawto = event.pos
		else:
			if (event.type == pygame.MOUSEBUTTONDOWN and
				event.pos[0] >= self.pos_x and event.pos[0] <= self.pos_x+self.scl_x-5 and
				event.pos[1] >= self.pos_y and event.pos[1] <= self.pos_y+self.scl_y):
				#
				self.mouserelative_x = self.pos_x - event.pos[0]
				self.mouserelative_y = self.pos_y - event.pos[1]
				self.drad_ready = True
				#
			elif (event.type == pygame.MOUSEBUTTONUP):
				self.drad_ready = False
			if (self.drad_ready == True and event.type == pygame.MOUSEMOTION):
					if (snap == True):
						snapX = screenwidth / grid
						self.pos_x = round((event.pos[0]+self.mouserelative_x)/snapX)*snapX+2
						self.pos_y = round((event.pos[1]+self.mouserelative_y)/snapX)*snapX+2
					else:
						self.pos_x = event.pos[0]+self.mouserelative_x
						self.pos_y = event.pos[1]+self.mouserelative_y
					self.n_selrect_posx = self.pos_x + ((self.scl_x - self.n_selrect_sclx)/2)
					self.n_selrect_posy = self.pos_y + ((self.scl_x - self.n_selrect_sclx)/2)
					self.n_selrect2_posx = self.pos_x + ((self.scl_x - self.n_selrect2_sclx)/2)
					self.n_selrect2_posy = self.pos_y + ((self.scl_x - self.n_selrect2_sclx)/2)


	# Draws the node
	def update (self):
		# Selction rectangle
		pygame.draw.rect(self.env_window, [255, 100, 10], [self.n_selrect_posx, self.n_selrect_posy, self.n_selrect_sclx, self.n_selrect_scly])
		pygame.draw.rect(self.env_window, [self.env_background[0], self.env_background[1], self.env_background[2]], [self.n_selrect2_posx, self.n_selrect2_posy, self.n_selrect2_sclx, self.n_selrect2_scly])
		# Node
		self.n_visual = pygame.draw.rect(self.env_window, [self.clr_r, self.clr_g, self.clr_b], [self.pos_x, self.pos_y, self.scl_x, self.scl_y])
		# Outputs
		for n in range (0, self.n_outputs):
			pygame.draw.rect(self.env_window, [255, 0, 0], [self.pos_x+self.scl_x-5, self.pos_y+(n+1)*15-10, 10, 10])
		# Inputs
		for n in range (0, self.n_inputs):
			pygame.draw.rect(self.env_window, [0, 255, 0], [self.pos_x-5, self.pos_y+(n+1)*15-10, 10, 10])
		# Lines
		if (self.connect_ready):
			pygame.draw.line (self.env_window, [255, 255, 255], self.inputvectorsource, self.drawto, 2)
			self.drad_ready = False


# Collective update
# Looks which node is selected and puts it on top
def coll_update (instances = []):
	nonLayerUpdate = True
	for n in instances:
		if (n.n_selrect_sclx != 0.0 and n.n_selrect_scly != 0.0):
			nonLayerUpdate = False
			topLayer = n
			for n in instances :
				if n == topLayer:
					pass
				else:
					n.update()
			topLayer.update()

	if (nonLayerUpdate == True):
		for n in instances:
			n.update()


# Creates a grid of squares
class grid():

	g_size = 0
	g_stroke = 0
	g_highlight = 0
	env_scr_w = 0
	env_scr_h = 0
	env_window = None

	def __init__(self, window, size , screenwidth, screenheight, strokewidth , highlight):
		self.env_window = window
		self.env_scr_w = screenwidth
		self.env_scr_h = screenheight
		self.g_size = size
		self.g_stroke = strokewidth
		self.g_highlight = highlight

	def draw (self):
		for n in range (0, self.g_size):
			if not (devidable(n, self.g_highlight)):
				pygame.draw.line (self.env_window, [60, 60, 60], [n* self.env_scr_w / self.g_size, 0], [n*self.env_scr_w / self.g_size, self.env_scr_h], self.g_stroke)
			else:
				pygame.draw.line (self.env_window, [100, 100, 100], [n* self.env_scr_w / self.g_size, 0], [n*self.env_scr_w / self.g_size, self.env_scr_h], self.g_stroke*2)

		for n in range (0, self.g_size):
			if not (devidable(n, self.g_highlight)):
				pygame.draw.line (self.env_window, [60, 60, 60], [0, n* self.env_scr_h / self.g_size * (self.env_scr_w / self.env_scr_h)], [self.env_scr_w , n*self.env_scr_h / self.g_size * (self.env_scr_w / self.env_scr_h)], self.g_stroke)
			else:pygame.draw.line (self.env_window, [100, 100, 100], [0, n* self.env_scr_h / self.g_size * (self.env_scr_w / self.env_scr_h)], [self.env_scr_w , n*self.env_scr_h / self.g_size * (self.env_scr_w / self.env_scr_h)], self.g_stroke*2)
