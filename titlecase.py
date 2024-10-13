import time

input_str = input("Enter any name: ")
input_str += " isinputtedname"

def to_title(string):
    splitted_str = f"{string}".split()
    result = ""
    index = -1

    for i in range(len(splitted_str) - 1):
        index += 1
        f = splitted_str[index]
        ff = f[0]
        ffc = ff.upper()
        ffc_remaining = f[1:]
        ffl = ffc_remaining.lower()
        string = ffc + ffl
        result += string + " "
    
    result = result.rstrip()
    print("Goodbye, "+result+"! Thanks for testing this program! (It may have bugs in it.)")
    print("\nExiting...")
    time.sleep(2)

to_title(input_str)