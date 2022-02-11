debug = False

def crack(message, key):

    if debug: print(f"crack(message='{message}', key='{key}')")

    letters = "abcdefghijklmnopqrstuvwxyz"
    key_index = 0

    new_message = ""

    for i in range(len(message)):

        if debug: print(message[i])
            
        if not message[i].isalpha():
            new_message += message[i]
            continue
        
        if debug: print(f"key_index='{key_index}'")

        new_message += key[key_index]

        key_index += 1

        if key_index >= len(key):
            key_index = key_index % len(key)
        
        if debug: print(new_message)


    cracked_message = ""

    for i, letter in enumerate(new_message):

        if not letter.isalpha():
            cracked_message += letter
            continue

        new_index = letters.index(message[i]) - letters.index(new_message[i])
        
        if debug: print(i, message[i], new_message[i], new_index)

        if new_index < 0:
            new_index += 26

        cracked_message += letters[new_index]

    return cracked_message


if __name__ == "__main__":
    print(crack("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friends"))
    



    
