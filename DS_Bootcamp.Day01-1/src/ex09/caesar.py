import sys

def latter_generator(mode,text, step):
    if len(sys.argv) != 4:
        raise ValueError("Argument count error: incorrect number of arguments.")

    res_text = ""
    step = int(step)

    if mode == "encode":
        step = int(step)
    elif mode == "decode":
        step = int(step) * -1
    else:
        raise ValueError("Mode error: mode must be 'encode' or 'decode'.")


    for char in text:
        if char.isalpha(): 
            if ord(char) >= 65 and ord(char) <= 90:
                step_base = ord('A')
            elif ord(char) >= 97 and ord(char) <= 122:
                step_base = ord('a')
            else:
                raise ValueError("The script does not support your language yet")
            
            res_text += chr((ord(char) - step_base + step) % 26 + step_base)
        else:
            res_text += char

    print(res_text)
   
if __name__ == '__main__':
    if len(sys.argv) == 4:
        latter_generator(sys.argv[1], sys.argv[2], sys.argv[3])