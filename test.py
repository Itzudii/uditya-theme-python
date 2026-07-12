# ============================================================
# PYTHON THEME COLOR TEST FILE
# ============================================================

# -------------------- IMPORTS --------------------

import os
import sys
import math as mathematics

from pathlib import Path
from typing import Optional, Union, List, Dict, Tuple
from collections import defaultdict


# -------------------- CONSTANTS --------------------

APP_NAME = "Uditya Theme"
VERSION = 1.0
DEBUG = True
MAX_USERS = 100
NOTHING = None


# -------------------- VARIABLES --------------------

name = "Uditya"
age = 21
height = 5.9
is_developer = True
user_data = None

users = ["Uditya", "Alex", "John"]
coordinates = (10, 20)
unique_ids = {1, 2, 3}

profile = {
    "name": "Uditya",
    "age": 21,
    "developer": True,
}


# -------------------- STRING TYPES --------------------

single_string = 'Hello World'
double_string = "Hello Python"
multiline_string = """
This is
a multiline
string.
"""

raw_string = r"C:\Users\Uditya"
byte_string = b"Python Bytes"

username = "Uditya"
formatted_string = f"Hello {username}, age is {age}"


# -------------------- NUMBERS --------------------

integer_number = 100
negative_number = -50
float_number = 10.55
complex_number = 3 + 5j

binary_number = 0b1010
octal_number = 0o755
hex_number = 0xFF

large_number = 1_000_000


# -------------------- BASIC FUNCTION --------------------

def greet(name: str) -> str:
    message = f"Hello {name}"
    return message


result = greet("Uditya")


# -------------------- FUNCTION PARAMETERS --------------------

def calculate(
    number_one: int,
    number_two: int = 10,
    *args,
    operation: str = "add",
    **kwargs,
) -> Union[int, float]:

    local_variable = 100

    if operation == "add":
        return number_one + number_two

    elif operation == "subtract":
        return number_one - number_two

    else:
        return 0


# -------------------- LAMBDA --------------------

square = lambda number: number ** 2

lambda_result = square(5)


# -------------------- DECORATOR --------------------

def logger(function):

    def wrapper(*args, **kwargs):
        print("Function called")

        result = function(*args, **kwargs)

        return result

    return wrapper


@logger
def protected_function()->None:
    print("Protected Function")


# -------------------- CLASS --------------------

class Player:

    game_name = "Heart Flame"

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.inventory = []

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    @staticmethod
    def game_version():
        return "1.0"

    @classmethod
    def create_default(cls):
        return cls("Default Player")

    def attack(self, enemy: "Enemy") -> None:
        damage = 10
        enemy.health -= damage

    def __str__(self):
        return self.name


# -------------------- INHERITANCE --------------------

class Enemy(Player):

    def __init__(self, name: str, health: int, damage: int):
        super().__init__(name, health)

        self.damage = damage

    def attack_player(self, player: Player):
        player.health -= self.damage


# -------------------- OBJECTS --------------------

player = Player(name="Uditya", health=100)

enemy = Enemy(
    name="Void Beast",
    health=50,
    damage=20,
)

player.attack(enemy)

print(player.name)
print(enemy.health)


# -------------------- IF / ELIF / ELSE --------------------

score = 85

if score >= 90:
    grade = "A"

elif score >= 75:
    grade = "B"

elif score >= 50:
    grade = "C"

else:
    grade = "Fail"


# -------------------- MATCH / CASE --------------------

command = "start"

match command:

    case "start":
        print("Game Started")

    case "stop":
        print("Game Stopped")

    case _:
        print("Unknown Command")


# -------------------- FOR LOOP --------------------

for user in users:

    print(user)

    if user == "Alex":
        continue

    if user == "John":
        break


# -------------------- WHILE LOOP --------------------

counter = 0

while counter < 5:

    counter += 1

else:
    print("Loop Finished")


# -------------------- LIST COMPREHENSION --------------------

numbers = [1, 2, 3, 4, 5]

squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]


# -------------------- DICTIONARY COMPREHENSION --------------------

number_map = {
    number: number ** 2
    for number in numbers
}


# -------------------- SET COMPREHENSION --------------------

unique_squares = {
    number ** 2
    for number in numbers
}


# -------------------- GENERATOR --------------------

generator = (
    number * 2
    for number in numbers
)


# -------------------- TRY / EXCEPT --------------------

try:

    result = 10 / 0

except ZeroDivisionError as error:

    print(error)

except Exception as exception:

    print(exception)

else:

    print("No Error")

finally:

    print("Finished")


# -------------------- RAISE --------------------

def validate_age(age: int):

    if age < 18:
        raise ValueError("Age must be 18+")


# -------------------- ASSERT --------------------

assert age >= 18, "Invalid Age"


# -------------------- WITH --------------------

file_path = Path("example.txt")

with open(file_path, "w") as file:

    file.write("Hello Python")


# -------------------- ASYNC / AWAIT --------------------

async def fetch_data():

    await async_operation()

    return {"status": "success"}


async def async_operation():

    pass


# -------------------- YIELD --------------------

def number_generator():

    for number in range(5):

        yield number


for generated_number in number_generator():

    print(generated_number)


# -------------------- GLOBAL --------------------

global_counter = 0


def update_counter():

    global global_counter

    global_counter += 1


# -------------------- NONLOCAL --------------------

def outer_function():

    outer_variable = 10

    def inner_function():

        nonlocal outer_variable

        outer_variable += 1

        return outer_variable

    return inner_function


# -------------------- BOOLEAN OPERATORS --------------------

value_a = True
value_b = False

boolean_and = value_a and value_b
boolean_or = value_a or value_b
boolean_not = not value_a


# -------------------- COMPARISON --------------------

number = 10

equal = number == 10
not_equal = number != 5

greater = number > 5
less = number < 20

greater_equal = number >= 10
less_equal = number <= 10


# -------------------- IDENTITY --------------------

object_a = None

is_none = object_a is None
is_not_none = object_a is not None


# -------------------- MEMBERSHIP --------------------

has_user = "Uditya" in users
missing_user = "Bob" not in users


# -------------------- TYPE HINTS --------------------

user_name: str = "Uditya"
user_age: int = 21

user_score: float = 99.5

active: bool = True

optional_name: Optional[str] = None

user_list: List[str] = []

user_dictionary: Dict[str, int] = {}

position: Tuple[int, int] = (10, 20)


# -------------------- BUILT-IN FUNCTIONS --------------------

print("Hello")

length = len(users)

number_value = int("100")

float_value = float("10.5")

string_value = str(100)

boolean_value = bool(1)

list_value = list((1, 2, 3))

tuple_value = tuple([1, 2, 3])

set_value = set([1, 2, 2])

dictionary_value = dict(name="Uditya")

maximum = max(numbers)

minimum = min(numbers)

total = sum(numbers)

sorted_numbers = sorted(numbers)

reversed_numbers = reversed(numbers)

enumerated_users = enumerate(users)

zipped_data = zip(users, numbers)

range_values = range(10)

object_id = id(player)

object_type = type(player)

is_player = isinstance(player, Player)

has_name = hasattr(player, "name")

player_name = getattr(player, "name")

setattr(player, "level", 10)


# -------------------- DEL --------------------

temporary_variable = "Delete Me"

del temporary_variable


# -------------------- PASS --------------------

def empty_function():

    pass


# -------------------- MAIN --------------------

if __name__ == "__main__":

    protected_function()

    update_counter()

    print(APP_NAME)

    print(VERSION)