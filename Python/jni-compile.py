# Copyright (c) 2016 Maximilian Spiekermann All Rights Reserved.
import os

print("Required software: JDK, GCC")
print("Please ensure that the following environment variables are set:")
os.system("echo JAVA_HOME (is currently set to %JAVA_HOME%)")
print("")

java_source_path = raw_input("Java Source File: ")
java_cmd = 'javac "' + java_source_path + '"'
print(java_cmd)
os.system(java_cmd)
cpp_source_path = raw_input("C++ Source File: ")
dll_output_path = raw_input("DLL Output Path: ")
cpp_cmd = 'gcc -Wl,--add-stdcall-alias -I"%JAVA_HOME%\include" -I"%JAVA_HOME%\include\win32" -shared -o "'+  dll_output_path + '" "' + cpp_source_path + '"'
os.system(cpp_cmd)
raw_input();