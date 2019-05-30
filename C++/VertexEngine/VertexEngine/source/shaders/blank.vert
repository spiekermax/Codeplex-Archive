#version 330 core

layout (location = 0) in vec3 vposition;

out vec4 vertexColor;

void main()
{

	gl_Position = vec4(vposition, 1.0f);
	vertexColor = vec4(0.247f, 0.498f, 1.0f, 1.0f);
}