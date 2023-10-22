# **kwargs

def print_user_attributes(**kwargs):
    print("kwargs:", kwargs)
    print("Type kwargs:", type(kwargs))
    for key, value in kwargs.items():
        print(key + ": " + str(value))

print_user_attributes(
    first_name='Meredith',
    last_name='Teo',
    age=30,
)

def make_a_pizza(name, size, toppings):
    return f"{name.capitalize()} ordered a {size.lower()} {toppings.lower()} pizza."

print(make_a_pizza(name="Mikey", 
                   size="Large",
                   toppings="Lettuce, tomato and onion"))

def smallest_number(*args):
    return min(args)

print(smallest_number(11, 5, 21, 67, 3, 9))

def order_milk_tea(**kwargs):
    print("Order Successful: ")
    for key, value in kwargs.items():
        print(key + ": " + str(value))
        
order_milk_tea(
    size='Medium',
    has_milk=True,
    has_boba=True,
    flavor='Burnt Sugar'
)