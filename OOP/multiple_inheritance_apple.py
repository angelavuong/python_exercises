class OperatingSystem:
    multitasking = True

class Apple:
    website = 'www.apple.com'

class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if(self.multitasking is True):
            print("This is a multi-tasking system. Visit {} for more details".format(self.website))

macBook = MacBook()
