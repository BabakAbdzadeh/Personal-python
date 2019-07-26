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
                                  , Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?"
                                  ,Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)
