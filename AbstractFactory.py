# Abstract Factory Design Pattern
# Classes for each computer part with attributes
# Includes ComputerPartsFactory, AdvancedComputerPartsFactory, StandardComputerPartsFactory
# Computer parts factory interface
class ComputerPartsFactory:
    # intalizing interfaces to create objects
    def __init__(self):
        self.monitor = Monitor()
        self.cpu = CPU()
        self.keyboard = Keyboard()
    
    def createMonitor(self):
        # create and return a monitor
        return self.monitor
    
    def createCPU(self):
        # create and return a cpu
        return self.cpu
    
    def createKeyboard(self):
        # create and return a keyboard
        return self.keyboard
    
# Advanced computer parts factory interface
# Concrete advanced computer parts factory
class AdvancedComputerPartsFactory:
    def __init__(self):
        self.monitor = Monitor()
        self.cpu = CPU()
        self.keyboard = Keyboard()
    
    def createMonitor(self):
        # create and return an advanced monitor
        return self.monitor
    
    def createCPU(self):
        # create and return an advanced cpu
        return self.cpu
    
    def createKeyboard(self):
        # create and return an advanced keyboard
        return self.keyboard

# Standard computer parts factory interface
# Concrete standard computer parts factory
class StandardComputerPartsFactory:
    def __init__(self):
        self.monitor = Monitor()
        self.cpu = CPU()
        self.keyboard = Keyboard()
    
    def createMonitor(self):
        # create and return a standard monitor
        return self.monitor
    
    def createCPU(self):
        # create and return a standard cpu
        return self.cpu
    
    def createKeyboard(self):
        # create and return a standard keyboard
        return self.keyboard

# Monitor interface
class Monitor:
    def __init__(self, name = None, model = None, cost = 0):
        self.name = name
        self.model = model
        self.cost = cost
    
    def displayInformation(self):
        print("Monitor Name: %s" %self.name)
        print("Monitor Model: %s" %self.model)
        print("Monitor Cost: %s\n" %self.cost)

# CPU interface
class CPU:
    def __init__(self, name = None, processor = None, series = None, cost = 0):
        self.name = name
        self.processor = processor
        self.series = series
        self.cost = cost
    
    def displayInformation(self):
        print("CPU Name: %s" %self.name)
        print("CPU Processor: %s" %self.processor)
        print("CPU Series: %s" %self.series)
        print("CPU Cost: %s\n" %self.cost)

# Keyboard interface
class Keyboard:
    def __init__(self, name = None, cost = 0):
        self.name = name
        self.cost = cost
    
    def displayInformation(self):
        print("Keyboard Name: %s" %self.name)
        print("Keyboard Cost: %s\n" %self.cost)