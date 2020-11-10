
class PrintTasks:
    def PrintContent(self, content):
        print(f'Content to be Printed : \n{content}')

    def TakePhotoCopy(self, content):
        print(f'Content to be Photo Copied : \n{content}')

    def ScanContent(self, content):
        print(f'Content to be Scanned : \n{content}')

class FaxTask:
    def FaxContent(self, content):
        print(f'Content to be Faxed : \n{content}')

class PrintDuplexTasks:
    def PrintDuplexContent(self, content):
        print(f'Content is Printing With Duplex Mode : \n{content}')

    def StapleContent(self, content):
        print(f'Content will be Stapled : \n{content}')

class BasicPrinters( PrintTasks) :
    pass

class IntermediatePrinters( BasicPrinters, FaxTask) :
    pass

class AdvancedPrinters( IntermediatePrinters, PrintDuplexTasks) :
    pass

message = "Demo on SOLID Principles - ISP with Sekhar Srinivasan (SekharTheGuru.net)"

prefix = "Basic Printer Performing : \n"
content = prefix + message 
bp = BasicPrinters()
bp.PrintContent( content)
bp.TakePhotoCopy( content)
bp.ScanContent( content)
print("-----------------------------")

prefix = "Intermediate Printer Performing : \n"
content = prefix + message 
ip = IntermediatePrinters()
ip.PrintContent( content)
ip.TakePhotoCopy( content)
ip.ScanContent( content)
ip.FaxContent(content)
print("-----------------------------")

prefix = "Advanced Printer Performing : \n"
content = prefix + message 
ap = AdvancedPrinters()
ap.PrintContent( content)
ap.TakePhotoCopy( content)
ap.ScanContent( content)
ap.FaxContent(content)
ap.PrintDuplexContent(content)
ap.StapleContent(content)
print("-----------------------------")


