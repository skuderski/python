"""import time

def timer(func):
    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Elapsed: {end - start}")
        return result
    return inner

@timer
def long_function():
    return sum(range(50_000_000))

long_function()"""

from typing import Callable, Any


def create_permissions(users: list) -> None:
    for user in users:
        print(f'Creating permissions for {user["username"]}')


def only_admin(func: Callable[[list], Any]) -> Callable[[list], Any]:
    def wrapper(users: list) -> Any:
        true_list = []
        for user in users:
            if user.get("is_admin") is True:
                true_list.append(user)
        return func(true_list)
    return wrapper

@only_admin
def process_users(users: list) -> Any:
    create_permissions(users)

users_data = [
    {"username": "Alice", "is_admin": True},
    {"username": "Bob", "is_admin": False},
    {"username": "Charlie", "is_admin": True}
]
process_users(users_data)
