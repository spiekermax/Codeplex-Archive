#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{
	// Vertex shader
	class vsh
	{
	private:
		GLuint m_vertsh;
	public:
		vsh(const char *filepath);
		operator GLuint();
		operator GLuint&();
		void deleteShader();
	};

	vsh::vsh(const char *filepath)
		:m_vertsh(glCreateShader(GL_VERTEX_SHADER))
	{
		// Reads the file
		char* vts_content = nullptr;
		try
		{
			FILE* vts;
			fopen_s(&vts, filepath, "rt");
			fseek(vts, 0, SEEK_END);
			unsigned long vts_size = ftell(vts);
			vts_content = new char[vts_size + 1];
			memset(vts_content, 0, vts_size + 1);
			fseek(vts, 0, SEEK_SET);
			fread(vts_content, 1, vts_size, vts);
			fclose(vts);
		}
		catch (std::fstream::failure e)
		{
			LOGERROR("FILE not found");
		}
		// Sets the shader source
		glShaderSource(m_vertsh, 1, &vts_content, NULL);
		// Compiles the shader
		glCompileShader(m_vertsh);
		// Debugger
		GLint cmp_success;
		glGetShaderiv(m_vertsh, GL_COMPILE_STATUS, &cmp_success);
		if (!cmp_success)
		{
			GLchar cmp_msg[256];
			glGetShaderInfoLog(m_vertsh, 256, NULL, cmp_msg);
			LOGERROR("glCompileShader(vsh)");
			std::cout << cmp_msg << std::endl;
		}
	}

	inline vsh::operator GLuint()
	{
		return m_vertsh;
	}

	inline vsh::operator GLuint&()
	{
		return m_vertsh;
	}

	inline void vsh::deleteShader()
	{
		glDeleteShader(m_vertsh);
	}

}