'''
this code excercise is a practice of oops in python, if you observe kine you find shirt in place of self and this does run well and can be replaced by anyother word
'''
class Shirt:
    def __init__(shirt, shirt_color, shirt_size, shirt_style, shirt_price):
        shirt.color = shirt_color
        shirt.size = shirt_size
        shirt.style = shirt_style
        shirt.price = shirt_price
    def change_price(shirt, new_price):
        shirt.price = new_price
    def discount(shirt, discount):
        return shirt.price*(1-discount)
        
