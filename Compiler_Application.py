class Compiler:
    def __init__(self,compiler_name,language,website_link):
        self.compiler_name = compiler_name
        self.language = language
        self.website_link = website_link
    def exceute_code(self):
        print("Code executed....")
    def create_file(self):
        print("File created....")
class Python(Compiler):
    def __init__(self,website_link):
        super().__init__("Online Compiler","Python",website_link)
    def run_ai(self):
        print("AI Running....")
    def run_ml(self):
        print("ML Running....")
        
class Java(Compiler):
    def __init__(self,website_link):
        super().__init__("GB Online Compiler","Java",website_link)
    def spring_boot(self):
        print("Springboot Running....")
compiler = Python("www.programiz.com")
compiler.exceute_code()
compiler.create_file()
print(compiler.compiler_name,compiler.language,compiler.website_link)
print()
compiler = Java("www.onlinegdb.com")
compiler.exceute_code()
compiler.create_file()
print(compiler.compiler_name,compiler.language,compiler.website_link) 
