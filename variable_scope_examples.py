# Here is a function we have defined in global scope
# It will be available to all functions we define as well

a = "Hello"

print(f"Outside the function {a}")

def print_variable():
    # The variable "a" is in global scope, so we can safely reference it here
    print(f"Inside the function {a}")

    # Let's define a variable "b" that is only available inside the print_variable() function, not globally
    b = "Shalom"
    print(f"This was defined inside the function, so it is only avaialable inside the function {b}")


# Let's see the function reference a global variable "a" and a local variable "b"
print_variable()


# This will throw an error, because variable b does not exist outside of the print_variable() function
# Uncomment it to see the error
# print(f"This won't work - {b}")


def pass_a_variable(variable_name_001):
    # Here we still have variable "a" defined, because it is in the global scope
    print(f"Still want to say {a}")

    # We cannot call variable "b" because it lives under the print_variable() function only
    # This will throw an error if we uncomment it
    #print(f"Can you say {b}...?")

    # This variable is defined after pass_a_variable function, but it is being passed in, so it is in scope
    print(f"Thank you for passing in the value {variable_name_001}")


c = f"{a} and Goodbye"
pass_a_variable(c)