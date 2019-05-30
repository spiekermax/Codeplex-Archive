#pragma once
// Debugging
#define LOGERROR(name) std::cout << "ERROR caused by " << name << " at line " << __LINE__ << ", in file "<< __FILE__ << std::endl

// Value definitions
#define NONE nullptr
#define FALSE 0
#define TRUE 1

// Variable types
#define UINT unsigned int
#define CSTR char *

// GLFW
#define GLFW_KEYS_TOTAL 349