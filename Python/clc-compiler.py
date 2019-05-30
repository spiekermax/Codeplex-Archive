# Abstract compiler
class compiler ():

    filename = None
    filecontent = None
    fileoutput = None
    fileoutput_r = None

    def __init__ (self, filename):
        self.filename = filename

    def read_file (self):
        self.filecontent = open(self.filename, "r").read()

    def write_base (self):
        filename = self.filename.replace (".clc", ".c")
        self.fileoutput = open(filename, "w")
        self.fileoutput.write("#include <stdio.h>\n\n")
        self.fileoutput.write("main()\n{\n\n\n}")
        self.fileoutput.close()

    def read_base (self):
        filename = self.filename.replace(".clc", ".c")
        self.fileoutput_r = open(filename, "r").read()

    def detect_line (self, dest_line):
        filecontent = ""
        keyword = ""
        output = ""
        cur_line = 0
        linestart = 0

        for char in list(self.filecontent):
        #
            if (cur_line == dest_line-1):
                break
            linestart += 1
            if (char == "\n"):
                cur_line += 1
        #
        lineend = list(self.filecontent)[linestart+1:].index("\n")+linestart+1
        for char in list(self.filecontent[linestart:lineend]):
            output += char
        return output

    def detect_keyword (self, line):
            keyword = ""
            line = list(line)

            for char in line:
                if (char == " "):
                    return keyword
                    break
                else:
                    keyword += char

    def analyze_line (self, keyword, line, linenumber):
        filename = self.filename.replace (".clc", ".c")
        if (keyword == "int"):
            self.read_base()
            basefile = list(self.fileoutput_r)
            output = list(line)
            output.append(";\n")
            output = ''.join(output)
            basefile.insert(29+linenumber, output)
            basefile = ''.join(basefile)
            self.fileoutput = open(filename, "w")
            self.fileoutput.write(basefile)




compiler = compiler(input (""))
compiler.read_file()
compiler.write_base()
line = compiler.detect_line(1)
keyword = compiler.detect_keyword(line)
compiler.analyze_line(keyword, line, 1)

input("Press 'enter' to quit...")
