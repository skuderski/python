def count_letters_in_string(string: str) -> dict:
    count = {}
    for letter in string.lower():
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] +=1

    return coun
print(count_letters_in_string("wodeczkawsad"))