#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{
	// Shader program
	class shp
	{
	private:
		GLuint m_shprogram;
	public:
		shp();
		operator GLuint&();
		void attachShader(GLuint &shader);
		void useProgram();
	};

	shp::shp()
		:m_shprogram(glCreateProgram()){}

	inline shp::operator GLuint&()
	{
		return m_shprogram;
	}

	void shp::attachShader(GLuint &shader)
	{
		glAttachShader(m_shprogram, shader);
		glLinkProgram(m_shprogram);
		GLint link_success;
		glGetProgramiv(m_shprogram, GL_LINK_STATUS, &link_success);
		if (!link_success)
		{
			GLchar link_msg[256];
			glGetProgramInfoLog(m_shprogram, 256, NULL, link_msg);
			LOGERROR("glLinkProgram(shp)");
			std::cout << link_msg << std::endl;
		}
	}

	inline void shp::useProgram()
	{
		glUseProgram(m_shprogram);
	}

}