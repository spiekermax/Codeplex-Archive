#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{
	// Window
	class wnd
	{
	private:
		// Window instance pointer
		GLFWwindow *m_window;
		bool m_inited = FALSE;
		// Keycallback
		friend void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods);
		friend void resizecallback(GLFWwindow *window, int widht, int height);
		friend void window_refresh_callback(GLFWwindow* window);
	public:
		// Variables
		int width;
		int height;
		bool keydown[GLFW_KEYS_TOTAL];
		// Operators
		bool operator== (bool arg);
		bool operator!= (bool arg);
		// Constructor
		explicit wnd(UINT width, UINT height, CSTR title, bool isResizable);
		// Destructor
		~wnd();
		// Ultility methods
		void clear();
		void resize(UINT width_new, UINT height_new);
		// Returns wether the window is closed
		bool isOpen() const;
		// Update methods
		void pollEvents();
		void waitEvents();
		void swapBuffers();
	};

	void key_callback(GLFWwindow *window, int key, int scancode, int action, int mods)
	{
		// Creates a pointer to the active window class
		wnd *class_ref = (wnd*)glfwGetWindowUserPointer(window);
		// Sets the item at 'key' to true, if pressed
		class_ref->keydown[key] = (action != GLFW_RELEASE);
	}

	void resizecallback(GLFWwindow *window, int width, int height)
	{
		wnd *class_ref = (wnd*)glfwGetWindowUserPointer(window);
		glViewport(0, 0, width, height);
		glfwGetFramebufferSize(window, &class_ref->width, &class_ref->height);
	}

	void window_refresh_callback(GLFWwindow* window)
	{
		glClear(GL_COLOR_BUFFER_BIT); // Replace with draw()
		glfwSwapBuffers(window);
	}

	inline bool wnd::operator==(bool arg)
	{
		return m_inited == arg;
	}

	inline bool wnd::operator!=(bool arg)
	{
		return m_inited != arg;
	}

	wnd::wnd(UINT wdth, UINT hght, CSTR title, bool isResizable)
		:width(wdth), height(hght)
	{
		// Sets the value of all items of keydown[] to 0
		std::memset(keydown, false, GLFW_KEYS_TOTAL*sizeof(bool));
		// Sets wether the window is resizable
		glfwWindowHint(GLFW_RESIZABLE, isResizable);
		// Creates the window with the specified parameters
		m_window = glfwCreateWindow(width, height, title, NONE, NONE);
		// Sets the current OpenGL context to the created window
		glfwMakeContextCurrent(m_window);
		// Creates a window user pointer
		glfwSetWindowUserPointer(m_window, this);
		// Initializes GLEW
		glewExperimental = TRUE; if (glewInit() != GLEW_OK) { LOGERROR("glewInit()"); system("PAUSE"); }
		// Sets the OpenGL drawing area
		glViewport(0, 0, width, height);
		// Sets the keycallback
		glfwSetWindowRefreshCallback(m_window, window_refresh_callback);
		glfwSetWindowSizeCallback(m_window, resizecallback);
		glfwSetKeyCallback(m_window, key_callback);
		m_inited = TRUE;
	}

	inline wnd::~wnd()
	{
		// Terminates GLFW
		glfwTerminate();
	}

	inline void wnd::clear()
	{
		glClear(GL_COLOR_BUFFER_BIT);
	}

	void wnd::resize(UINT width_new, UINT height_new)
	{
		width = width_new;
		height = height_new;
		glfwSetWindowSize(m_window, width, height);
	}

	bool wnd::isOpen() const
	{
		// Returns wether the window is closed
		return !glfwWindowShouldClose(m_window);
	}

	inline void wnd::pollEvents()
	{
		// Calls the events
		glfwPollEvents();
	}

	inline void wnd::waitEvents()
	{
		// Waits until a event occurs
		glfwWaitEvents();
	}

	void wnd::swapBuffers()
	{
		// Runs a double buffer
		glfwSwapBuffers(m_window);
	}

}