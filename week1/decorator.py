# display

def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper

@decorator_function
def display():
    print('Hello how are you?')

@decorator_function
def display_info(name, age):
    print(f"The name is {name} and the age is {age}")

display()
display_info("arun", 10)