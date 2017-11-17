class Apple:
    manufacturer = 'Apple, Inc.'
    contactWebsite = 'www.apple.com/contact'

    def contactDetails(self):
        print("To contact us, go to ", self.contactWebsite)

class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacturer = 2017

    def manufactureDetails(self):
        print("This Macbook was manufacturered in the year {} by {}".format(self.yearOfManufacturer, self.manufacturer))

macBook = Macbook()
macBook.manufactureDetails()
macBook.contactDetails()
