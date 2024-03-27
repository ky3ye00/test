import random

class GreetingError(Exception):
    def __init__(self, message):
        super().__init__(message)

def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            name = args[0]
            if not name:
                raise GreetingError("Name is required.")
            greetings = ["Howdy", "Ahoy", "Hello", "Hi"]
            message = random.choice(greetings)
            return func(name, message)
        except GreetingError as e:
            return str(e)
    return wrapper

@greeting_decorator
def generate_greeting(name, message):
    return f"{message}, {name}! :)"

def main():
    user_name = input("Please enter your name: ")
    result = generate_greeting(user_name)
    print(result)

if __name__ == "__main__":
    main()
