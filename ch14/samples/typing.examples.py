# samples/typing.examples.py


###############################################
# This module is not supposed to be executed! #
###############################################


# not strongly typed language
a = 7
b = "7"

a + b == 14
# concatenate(a, b) == "77"


# dynamic typing
a = 7
a * 2 == 14
a = "Hello"
a * 2 == "HelloHello"


# other languages
# String greeting = "Hello";
# int m = 7;
# float pi = 3.141592;


# function annotations
def greet(first_name, last_name, age):
    return f"Greeting {first_name} {last_name} of age {age}"

# def greet(
#     first_name: "First name of the person we are greeting",
#     last_name: "Last name of the person we are greeting",
#     age: "The person's age"
# ) -> "Returns the greeting sentence":
#     return f"Greeting {first_name} {last_name} of age {age}"

# def greet(first_name: str, last_name: str, age: int = 18) -> str:
#     return f"Greeting {first_name} {last_name} of age {age}"


# # list
# from typing import List

# def process_words(words: List[str]):
#     for word in words:
#         # do something with word


# # dict
# from typing import Dict

# def process_users(users: Dict[str, int]):
#     for name, age in users.items():
#         # do something with name and age


# # optional
# from typing import Optional

# def greet_again(name: Optional[str] = None):
#     if name is not None:
#         print(f"Hello {name}!")
#     else:
#         print("Hey dude")


# # custom
# class Cat:
#     def __init__(self, name: str):
#         self.name = name

# def call_cat(cat: Cat):
#     return f"{cat.name}! Come here!"
