
debug = False


def decoder(string, offset):
    
    if debug: print(f"initialized decoder() with '{str}'")

    new_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in string:

        if debug: print(f"iterating through {letter} in string")

        if letter in alphabet:
            old_index = alphabet.index(letter)

            if debug: print(f"old_index = {old_index}")

            new_index = old_index + (offset % 26)

            if new_index > 25:
                new_index = new_index - 26

            if debug: print(f"new_index = {new_index}")

            new_str += alphabet[new_index]

            if debug: print(f"{new_str}")

        else:
            new_str += letter

            if debug: print(f"{new_str}")

    print(f"new_str = '{new_str}'")
    
    return new_str


# decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", 1)


for offset in range(1, 26):
    print (offset, decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",  offset))











    