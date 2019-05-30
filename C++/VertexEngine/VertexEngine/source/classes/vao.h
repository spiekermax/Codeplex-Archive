#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{
	// Vertex array object
	class vao
	{
	private:
		GLuint m_vao;
	public:
		vao();
		operator GLuint();
		operator GLuint&();
		static void setCurrent(GLuint &varray);
		static void setCurrent(int = 0);
		static void attachBuffer(UINT index, int size, GLenum type, GLboolean normalized, int stride, const void *pointer);
		static void enableBuffer(UINT index);
	};

	inline vao::vao()
	{
		glGenVertexArrays(1, &m_vao);
	}

	inline vao::operator GLuint()
	{
		return m_vao;
	}

	inline vao::operator GLuint&()
	{
		return m_vao;
	}

	inline void vao::setCurrent(GLuint &varray)
	{
		glBindVertexArray(varray);
	}

	inline void vao::setCurrent(int arg)
	{
		if(arg == 0)glBindVertexArray(0);
	}

	inline void vao::attachBuffer(UINT index, int size, GLenum type, GLboolean normalized, int stride, const void *pointer)
	{
		glVertexAttribPointer(index, size, type, normalized, stride, pointer);
	}

	inline void vao::enableBuffer(UINT index)
	{
		glEnableVertexAttribArray(index);
	}

}