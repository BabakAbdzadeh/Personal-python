# real estate application
# agent can manage properties
#
# 2 type of properties :
#       1.apartments
#       2.houses
#
# agent must be able to :
#       1. enter relevant details about new properties
#       2. list all currently available properties
#       3. mark a property as sold or rented
#       4. for brevity we do not want to edit property details after it is sold


class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super.__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_bathrooms = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms :{}".format(self.num_bathrooms))
        print()

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of bathrooms: "))

    prompt_init = staticmethod(prompt_init)


######
# without class function #      !!!!  validation function  !!!!!!!


def get_valid_input(input_string, valid_option):
    input_string += "({})".format(", ".join(valid_option))
    response = input(input_string)
    while response.lower() not in valid_option:
        response = input(input_string)
    return response


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("what laundry facilities does the property have?"
                                  , House.valid_garage)
        balcony = get_valid_input("Does the property have a balcony?"
                                  , House.valid_fenced)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced?"
                                 , House.valid_fenced)
        garage = get_valid_input("Does the property have a garage?"
                                 , House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().diplay()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("what are the estimated taxes?")
        )
    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, rent='', furnished='', utilities='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().diplay()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("is property furnished? ",
                                      ("yes", "no"))
        )

    prompt_init = staticmethod(prompt_init)
    