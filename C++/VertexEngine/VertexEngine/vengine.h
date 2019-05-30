#pragma once
#include "source\definitions.h"
#include "source\dependencies.h"

#include "source\classes\ebo.h"
#include "source\classes\fsh.h"
#include "source\classes\shp.h"
#include "source\classes\vao.h"
#include "source\classes\vbo.h"
#include "source\classes\vsh.h"
#include "source\classes\wnd.h"

#include "source\functions\glf.h"

namespace vtx
{
	extern inline int main();
}

int main()
{
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);	
	return glfwInit() && vtx::main();
}