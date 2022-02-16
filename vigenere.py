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

        new_message += letters[letters.index(message[i]) - letters.index(key[key_index])]

        key_index += 1

        if key_index >= len(key):
            key_index = key_index % len(key)
        
        if debug: print(new_message)

    return new_message


if __name__ == "__main__":
    print(crack("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friends"))
    



    
