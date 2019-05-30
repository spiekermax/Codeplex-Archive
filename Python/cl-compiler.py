# Abstract compiler
# Python 3.x required
class compiler ():

    filename_old      = None
    filename_new      = None
    content_read_old  = None
    content_read_new  = None
    content_write     = None
    content_args      = None

    def __init__ (self, filename):
        self.filename_old = filename
        self.filename_new = filename.replace (".cl", ".py")

    # Reads from the .cl file => content_read_old
    def file_read_old (self):
        try:
            self.content_read_old = open(self.filename_old, "r").read()
            print("Found file " + "'" + self.filename_old + "'.")
            print("Reading file...")
            print("Read succesfully.")
        except FileNotFoundError:
            print ("Could not find " + "'" + self.filename_old + "'.")
            self.__init__(input("Please enter the filename:\n"))
            self.file_read_old()

    # Writes the basic Python-file
    def file_write_base (self):
        self.content_write = open(self.filename_new, "w")
        print(self.content_write)
        self.content_write.write("import pygame\n\n")
        self.content_write.write("pygame.init()\n")
        self.content_write.close()
        self.content_read_new = open(self.filename_new, "r").read()
        print ("Generated Python-file succesfully...")

    # Lists all args(/words) inside th file => content_args
    def file_list_args (self):
        word = ""
        words = []
        for char in list(self.content_read_old):
            if (char == " "):
                words.append (word)
                word = ""
            elif (char == "\n"):
                words.append (word)
                words.append ("\n")
                word = ""
            else:
                word += char
        self.content_args = words

    # Returns all args of a specific line
    def file_argsInLine (self, line = 0):
        content_line = []
        linenumber = 0
        for arg in self.content_args:
            if (linenumber+1 == line and arg == "\n"):
                for item in content_line:
                    try:
                        content_line.remove("")
                    except ValueError:
                        continue
                return content_line
            elif (arg == "\n"):
                linenumber += 1
                content_line = []
            else:
                content_line.append(arg)

    def code_compile_line (self, content_line):
        try:
            if (content_line[0] == "int"):
                output = ''.join(content_line[1:])+"\n"
                content_new = list(self.content_read_new)
                content_new.insert(len(content_new), output)
                content_new = ''.join(content_new)
                self.content_write = open(self.filename_new, "w")
                self.content_write.write(content_new)
                self.content_write.close()
                self.content_read_new = open(self.filename_new, "r").read()
        except IndexError:
            pass


Compiler = compiler(input("Please enter the filename:\n"))
Compiler.file_read_old()
Compiler.file_write_base()
Compiler.file_list_args()
for n in range(1, len(list(Compiler.content_read_new))):
    content_line = Compiler.file_argsInLine(n)
    Compiler.code_compile_line(content_line)

input("\nPress 'enter' to exit...")
