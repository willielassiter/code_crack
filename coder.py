debug = False


def offset(string):
    
    if debug: print(f"initialized undo_offset() with '{str}'")

    new_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in string:

        if debug: print(f"iterating through {letter} in string")

        if letter in alphabet:
            old_index = alphabet.index(letter)

            if debug: print(f"old_index = {old_index}")

            new_index = old_index - 10

            if new_index < 0:
                new_index = new_index + 26

            if debug: print(f"new_index = {new_index}")

            new_str += alphabet[new_index]

            if debug: print(f"{new_str}")

        else:
            new_str += letter

            if debug: print(f"{new_str}")

    print(f"new_str = '{new_str}'")
    
    return new_str


offset("hello to you!")
    