#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{

	inline void clearColor(float red, float green, float blue)
	{
		glClearColor(red, green, blue, 1.0f);
	}

	inline void clearColor(float red, float green, float blue, float alpha)
	{
		glClearColor(red, green, blue, alpha);
	}

	inline void deleteShader(GLuint shader)
	{
		glDeleteShader(shader);
	}

}