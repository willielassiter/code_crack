
debug = True


def decoder(string, offset):
    
    if debug: print(f"initialized decoder() with '{str}'")

    string_copy = string.lower()

    if debug: print(f"string_copy - '{string_copy}'")

    new_string = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in string_copy:

        if debug: print(f"iterating through {letter} in string_copy")

        if letter in alphabet:
            old_index = alphabet.index(letter)

            if debug: print(f"old_index = {old_index}")

            new_index = old_index + (offset % 26)

            if new_index > 25:
                new_index = new_index - 26

            if new_index < 0:
                new_index += 26

            if debug: print(f"new_index = {new_index}")

            new_string.append(alphabet[new_index])

        else:
            new_string.append(letter)

        if debug: print(f"new_string - {new_string}")

    for i in range(len(string)):

        if debug: print(f"string[i] - '{string[i]}'")

        if string[i].isupper():
            new_string[i] = new_string[i].upper()
            
            if debug: print(f"new_string[i] - '{new_string[i]}'")
    
    new_string = "".join(new_string)

    if debug: print(f"new_string = '{new_string}'")

    return new_string


decoder("HelLo", 3)


# for offset in range(1, 26):
#     print (offset, decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",  offset))

