def message_people(people: list) -> callable:
    def print_message(message: str) -> str:
        people_together = ", ".join(people)
        if message == "hello":
            print(f"Hello, {people_together}, nice to see you!")
        elif message == "meeting":
            print(f"{people_together}, we have a meeting in an hour, don't be late!")
        elif message == "bye":
            print(f"Bye {people_together}, see you tomorrow!")
    return print_message
people_list = ["Alice", "Bob", "Charlie"]
the_message = message_people(people_list)
print(the_message("hello"))
print(the_message("meeting"))