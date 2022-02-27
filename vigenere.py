debug = False

def encode(message, key):

    if debug: print(f"crack(message='{message}', key='{key}')")

    message_copy = message.lower()
    key = key.lower()

    if debug: print(f"message - '{message}'; key - '{key}'")

    letters = "abcdefghijklmnopqrstuvwxyz"
    key_index = 0

    new_message = []

    for i in range(len(message_copy)):

        if debug: print(message_copy[i])
            
        if not message_copy[i].isalpha():
            new_message.append(message[i])
            continue

        if debug: print(f"key_index='{key_index}'")

        new_index = letters.index(message_copy[i]) + (letters.index(key[key_index]) % 26)

        if new_index > 25:
            new_index -= 26

        new_message.append(letters[new_index])

        key_index += 1

        if key_index >= len(key):
            key_index = key_index % len(key)

    for i in range(len(message)):

        if debug: print(f"message[i] - '{message[i]}'")

        if message[i].isupper():
            new_message[i] = new_message[i].upper()
            
            if debug: print(f"new_message[i] - '{new_message[i]}'")
    
    new_message = "".join(new_message) 

    if debug: print(new_message)

    return new_message


def decode(message, key):

    if debug: print(f"crack(message='{message}', key='{key}')")

    message_copy = message.lower()
    key = key.lower()

    if debug: print(f"message_copy - '{message_copy}'; key - '{key}'")

    letters = "abcdefghijklmnopqrstuvwxyz"
    key_index = 0

    new_message = []

    for i in range(len(message_copy)):

        if debug: print(message_copy[i])
            
        if not message_copy[i].isalpha():
            new_message.append(message_copy[i])
            continue
        
        if debug: print(f"key_index='{key_index}'")

        new_index = letters.index(message_copy[i]) - (letters.index(key[key_index]) % 26)

        if new_index < 0:
            new_index += 26

        new_message.append(letters[new_index])

        key_index += 1

        if key_index >= len(key):
            key_index = key_index % len(key)
<<<<<<< HEAD

    for i in range(len(message)):

        if debug: print(f"message[i] - '{message[i]}'")

        if message[i].isupper():
            new_message[i] = new_message[i].upper()
            
            if debug: print(f"new_message[i] - '{new_message[i]}'")
    
    new_message = "".join(new_message)
      
    if debug: print(f"new_message - '{new_message}'")
=======
>>>>>>> 43c0b34716577f6d29677960c1a6bf3bcfe69aea

    for i in range(len(message)):

        if debug: print(f"message[i] - '{message[i]}'")

<<<<<<< HEAD
if __name__ == "__main__":
    print(decode("Dfc aruw fsti gr vjtwhr wznj? Vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friEnds"))
    print(encode("You were able to decode this? Nice work! You are becoming quite the expert at crytography!", "Friends"))
=======
        if message[i].isupper():
            new_message[i] = new_message[i].upper()
            
            if debug: print(f"new_message[i] - '{new_message[i]}'")
>>>>>>> 43c0b34716577f6d29677960c1a6bf3bcfe69aea
    
    new_message = "".join(new_message)
      
    if debug: print(f"new_message - '{new_message}'")

    return new_message


if __name__ == "__main__":
    print(decode("Dfc aruw fsti gr vjtwhr wznj? Vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friEnds"))
    print(encode("You were able to decode this? Nice work! You are becoming quite the expert at crytography!", "Friends"))
