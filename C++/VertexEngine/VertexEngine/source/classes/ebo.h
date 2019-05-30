#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{

	// Element buffer object
	class ebo
	{
	private:
		GLuint m_ebo;
	public:
		ebo();
		operator GLuint();
		operator GLuint&();
		static void setCurrent(GLuint &buffer);
		static void setDataCurrent(int size, const void *data, GLenum usage);
	};

	ebo::ebo()
	{
		glGenBuffers(1, &m_ebo);
	}

	inline ebo::operator GLuint()
	{
		return m_ebo;
	}

	inline ebo::operator GLuint&()
	{
		return m_ebo;
	}

	inline void ebo::setCurrent(GLuint &buffer)
	{
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffer);
	}

	inline void ebo::setDataCurrent(int size, const void *data, GLenum usage)
	{
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, size, data, usage);
	}

}