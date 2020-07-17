# Templating is part of the string module
# Allows for data to change without having to edit the application
# Can be modified with subclasses

from string import Template

def main():
    cart = []
    cart.append(dict(item = "Coke", price = 8, qty = 2))
    cart.append(dict(item = "Cake", price = 12, qty = 1))
    cart.append(dict(item = "Fish", price = 32, qty = 4))


    t = Template("$qty x $item = $price")
    total = 0
    print("Cart:")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total: " + str(total))

if __name__ == "__main__":
    main()

# Template Errors
# No placeholder match, will result in a KeyError in which the Template wasnt given a value for a placeholder
# Bad placeholder, will result in a Value Error. The placeholder started with an invalid character (Usually a number)