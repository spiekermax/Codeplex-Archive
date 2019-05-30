#pragma once
#include "..\dependencies.h"
#include "..\definitions.h"

namespace vtx
{
	// Fragment shader
	class fsh
	{
	private:
		GLuint m_fragsh;
	public:
		fsh(const char *filepath);
		operator GLuint();
		operator GLuint&();
		void deleteShader();
	};

	fsh::fsh(const char *filepath)
		:m_fragsh(glCreateShader(GL_FRAGMENT_SHADER))
	{
		// Reads the file
		char* fms_content = nullptr;
		try
		{
			FILE* fms;
			fopen_s(&fms, filepath, "rt");
			fseek(fms, 0, SEEK_END);
			unsigned long vts_size = ftell(fms);
			fms_content = new char[vts_size + 1];
			memset(fms_content, 0, vts_size + 1);
			fseek(fms, 0, SEEK_SET);
			fread(fms_content, 1, vts_size, fms);
			fclose(fms);
		}
		catch (std::fstream::failure e)
		{
			LOGERROR("FILE not found");
		}
		// Sets the shader source
		glShaderSource(m_fragsh, 1, &fms_content, NULL);
		// Compiles the shader
		glCompileShader(m_fragsh);
		// Debugger
		GLint cmp_success;
		glGetShaderiv(m_fragsh, GL_COMPILE_STATUS, &cmp_success);
		if (!cmp_success)
		{
			GLchar cmp_msg[256];
			glGetShaderInfoLog(m_fragsh, 256, NULL, cmp_msg);
			LOGERROR("glCompileShader(fsh)");
			std::cout << cmp_msg << std::endl;
		}
	}

	inline fsh::operator GLuint()
	{
		return m_fragsh;
	}

	inline fsh::operator GLuint&()
	{
		return m_fragsh;
	}

	inline void fsh::deleteShader()
	{
		glDeleteShader(m_fragsh);
	}

}