# Computer store class that takes in computer parts objects from AbstractFactory
from AbstractFactory import *

class ComputerStore:
    # Initiated with computer parts factory
    def __init__(self, factory = None):
        self._factory = factory
        self._monitor = factory.monitor
        self._cpu = factory.cpu
        self._keyboard = factory.keyboard
        
    def displayMonitorInfo(self):
        # display information about the monitor
        self._monitor.displayInformation()
    
    def displayCpuInfo(self):
        # display information about CPU
        self._cpu.displayInformation()
    
    def displayKeyboardInfo(self):
        # display information about keyboard
        self._keyboard.displayInformation()
    
    def displayCost(self):
        # display the total cost of all of the components for the client
        total = self._monitor.cost + self._cpu.cost + self._keyboard.cost
        print("Total Cost: %s\n" % total)

if __name__ == "__main__":
    # declaring variables
    computer = ComputerPartsFactory()
    advComputer = AdvancedComputerPartsFactory()
    standardComputer = StandardComputerPartsFactory()
    
    monitor = computer.createMonitor()
    advMonitor = advComputer.createMonitor()
    standardMonitor = standardComputer.createMonitor()
    
    cpu = computer.createCPU()
    advCpu = advComputer.createCPU()
    standardCpu = standardComputer.createCPU()
    
    keyboard = computer.createKeyboard()
    advKeyboard = advComputer.createKeyboard()
    standardKeyboard = standardComputer.createKeyboard()
    
    # testing to see if the function of the classes work properly
    monitor.name = "Acer"
    monitor.model = "G277HL"
    monitor.cost = "$176.99"
    
    cpu.name = "Intel Core i3-8100"
    cpu.processor = "3.60"
    cpu.series = "Core i3"
    cpu.cost = "$117"
    
    keyboard.name = "PICTEK Mechanical Gaming Keyboard"
    keyboard.cost = "$39.99"
    
    # setting each attribute for advanced parts
    # testing to see if the function of the advanced computer parts factory class works
    advMonitor.name = "Dell Alienware"
    advMonitor.model = "AW3418HW"
    advMonitor.cost = "$929.99"
    
    advCpu.name = "AMD Ryzen 9 3900X"
    advCpu.processor = "3.80"
    advCpu.series = "3000"
    advCpu.cost = "$499"
    
    advKeyboard.name = "Razer BlackWidow Tournament Edition Chroma V2"
    advKeyboard.cost = "$139.99"
    
    # setting each attribute for standard parts
    # testing to see if the function of the standard computer parts factory class works
    standardMonitor.name = "HP"
    standardMonitor.model = "Z32 31.5-inch"
    standardMonitor.cost = "$749"
    
    standardCpu.name = "AMD Ryzen 3"
    standardCpu.processor = "3.5"
    standardCpu.series = "2200G"
    standardCpu.cost = "$91.95"
    
    standardKeyboard.name = "Razer BlackWidowX Tournament Edition"
    standardKeyboard.cost = "$69.99"
    
    print("--------------------")
    # Debugging ComputerPartsFactory
    print("Simple Components:\n")
    monitor.displayInformation()
    cpu.displayInformation()
    keyboard.displayInformation()
    
    print("--------------------")
    # Debugging AdvancedComputerPartsFactory
    print("Advanced Components:\n")
    advMonitor.displayInformation()
    advCpu.displayInformation()
    advKeyboard.displayInformation()
    
    print("--------------------")
    # Debugging StandardComputerPartsFactory
    print("Standard Components:\n")
    standardMonitor.displayInformation()
    standardCpu.displayInformation()
    standardKeyboard.displayInformation()
    
    print("--------------------")
    # Setting ComputerStore class with advanced computer and testing the attributes
    print("Buying the components:\n")
    computer = ComputerStore(advComputer)
    
    computer._monitor.name = "Pro Display XDR"
    computer._monitor.model = "Pro Display XDR"
    computer._monitor.cost = 5999
    
    computer._cpu.name = "Intel Xeon W"
    computer._cpu.processor = "4.4"
    computer._cpu.series = "W-3275"
    computer._cpu.cost = 4995
    
    computer._keyboard.name = "Magic Keyboard with Numeric Keypad - Space Gray"
    computer._keyboard.cost = 149
    
    # Displaying the computer attributes
    computer.displayMonitorInfo()
    computer.displayCpuInfo()
    computer.displayKeyboardInfo()
    computer.displayCost()
