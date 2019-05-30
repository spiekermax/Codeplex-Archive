#include "vengine.h"

int vtx::main()
{
	wnd window(800, 600, "I am awesome!", true);
	// glPolygonMode(GL_FRONT_AND_BACK, GL_FILL); // Debugging
	vtx::clearColor(0.9, 0.9, 0.9);

	shp shader_prog;
	vsh vertex_shader("source/shaders/blank.vert");
	fsh fragment_shader("source/shaders/blank.frag");
	shader_prog.attachShader(vertex_shader);
	vertex_shader.deleteShader();
	shader_prog.attachShader(fragment_shader);
	fragment_shader.deleteShader();

	GLfloat vertices[] = { 0.5f, 0.5f, 0.0f, 0.5f, -0.5f, 0.0f, -0.5f, -0.5f, 0.0f, -0.5f, 0.5f, 0.0f };
	GLuint indices[] = { 0, 1, 3, 1, 2, 3 };
	
	vao vert_array;
	ebo element_buffer;
	vbo vert_buffer;
	
	vao::setCurrent(vert_array);
		vbo::setCurrent(vert_buffer);
		vbo::setDataCurrent(sizeof(vertices), vertices, GL_STATIC_DRAW);

		ebo::setCurrent(element_buffer);
		ebo::setDataCurrent(sizeof(indices), indices, GL_STATIC_DRAW);
		
		vao::attachBuffer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0); // Research
		vao::enableBuffer(0);
	vao::setCurrent(NULL);
	
	while (window.isOpen())
	{
		window.pollEvents();

		window.clear();
		shader_prog.useProgram();
		vao::setCurrent(vert_array);
			glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
		vao::setCurrent(0);

		window.swapBuffers();
	}
	
	return 0;
}