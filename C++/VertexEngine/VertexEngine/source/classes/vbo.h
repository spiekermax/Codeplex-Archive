#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{

	// Vertex buffer object
	class vbo
	{
	private:
		GLuint m_vbo;
	public:
		vbo();
		operator GLuint();
		operator GLuint&();
		static void setCurrent(GLuint &buffer);
		static void setDataCurrent(int size, const void *data, GLenum usage);
	};

	inline vbo::vbo()
	{
		glGenBuffers(1, &m_vbo);
	}

	inline vbo::operator GLuint()
	{
		return m_vbo;
	}

	inline vbo::operator GLuint&()
	{
		return m_vbo;
	}

	inline void vbo::setCurrent(GLuint &buffer)
	{
		glBindBuffer(GL_ARRAY_BUFFER, buffer);
	}

	inline void vbo::setDataCurrent(int size, const void *data, GLenum usage)
	{
		glBufferData(GL_ARRAY_BUFFER, size, data, usage);
	}

}