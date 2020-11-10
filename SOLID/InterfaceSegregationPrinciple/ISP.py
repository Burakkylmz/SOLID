# In the field of software engineering, the interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy.


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

message = "SOLID Principles"

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


