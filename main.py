def universal_integer_input(message):
    """This function is used for safe user input of integers."""
    while True:
        try:
            n = input(message)
            n = int(n)
            break
        except ValueError:
            print("This is not a number. Try again...")
    return n

def universal_float_input(message):
    """This function is used for safe user input of floats."""
    while True:
        try:
            n = input(message)
            n = float(n)
            break
        except ValueError:
            print("This is not a number. Try again...")
    return n

def a_function(arguments):
    """Oh boy i sure am a function"""
    while True:
        try:
            break
        except:
             print("Something wrong. Try again...")
        finally:
            return None

while True:
    print(universal_integer_input("this is a test\n"))
    print(universal_float_input("this is a test2\n"))