#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2

# example of the test

# fuction myFunction (params) { 
# console.log("running myFunction")
# return param +1;
# }

# def my_function(promp):
#     print("running my_function")
#     return promp+ 1

# def say_hi(name):
#     print(f"Hi there, {name}!")

# say_hi()

# def stylish_painter():
#     best_hairstyle = "Bob Ross"
#     return "Jean-Michel Basquiat"
#     return best_hairstyle
#     print(best_hairstyle)

# stylish_painter()