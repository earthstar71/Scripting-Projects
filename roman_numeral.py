from time import sleep

def run_program():
    input_str = input("\nEnter any decimal number between 1 and 3999 and this will return the equivalent roman numeral number (press \"q\" to exit): ")

    if input_str == "q":
        quit()

    decimal_roman = {
        "1": "I",
        "2": "II",
        "3": "III",
        "4": "IV",
        "5": "V",
        "6": "VI",
        "7": "VII",
        "8": "VIII",
        "9": "IX",
        "10": "X",
        "20": "XX",
        "30": "XXX",
        "40": "XL",
        "50": "L",
        "60": "LX",
        "70": "LXX",
        "80": "LXXX",
        "90": "XC",
        "100": "C",
        "200": "CC",
        "300": "CCC",
        "400": "CD",
        "500": "D",
        "600": "DC",
        "700": "DCC",
        "800": "DCCC",
        "900": "CM",
        "1000": "M",
        "2000": "MM",
        "3000": "MMM"
    }

    def convert_to_roman():
        result = ""
        zeros = ""
        for i in range(1, len(input_str)):
            zeros += "0"
        list_digits = list(input_str)
        first_digit = list_digits[0]
        num = first_digit + zeros
        roman_num = decimal_roman[num]
        msg = ""
        msg += roman_num
        for first_digit in range(1, len(input_str) - 1):
            zeros = zeros[1:]
            list_digits.pop(0)
            first_digit = list_digits[0]
            if first_digit == "0":
                continue
            num = first_digit + zeros
            roman_num = decimal_roman[num]
            msg += roman_num
        else:
            if len(input_str) - 1 == 0:
                print(decimal_roman[input_str])
        if input_str[-1] == "0":
            list_digits.pop()
            result = msg
        elif input_str[-1] != "0" and len(input_str) != 1:
            result = msg + decimal_roman[list_digits[-1]]
        print(result)

    error_code = False
    int_input = 0

    if input_str == "":
        print("Empty strings are not processable.")
        error_code = True
    else:
        if input_str[0] == "0":
            print("Leading zeros are not allowed.")
            error_code = True
        else:
            try:
                int_input = int(input_str)
            except ValueError:
                print("Oops! Looks like the value you entered is not a valid integer.")
                error_code = True

    if not error_code:
        min_num = int_input >= 1
        max_num = int_input <= 3999
        number_is_valid = min_num and max_num
        if number_is_valid:
            convert_to_roman()
        else:
            print("The value you entered is outside the allowed range for this roman numeral converter. Try entering an integer between 1 and 3999.")

while True:
    is_terminated = False
    try:
        run_program()
    except (EOFError, KeyboardInterrupt):
        is_terminated = True

    if is_terminated:
        try:
            confirmation = input("\nAre you sure you want to exit? (type yes to continue, no to cancel): ")
        except (EOFError, KeyboardInterrupt):
            print("\nSorry, but you didn't type yes or no, so we decided to exit the program.")
            print("Exiting the program...")
            sleep(1)
            quit()
        
        if confirmation == "yes":
            print("Thanks for using this roman numeral converter!")
            print("Terminating the program. Goodbye!")
            sleep(1)
            quit()
        elif confirmation == "no":
            print("Restarting the program...")
            sleep(1)
            continue
        else:
            if len(confirmation) > 10:
                print(f"\nSorry, you didn't type yes or no, you typed \"{confirmation[0:9]}...\", so we decided to restart the program.")
            else:
                print(f"\nSorry, you didn't type yes or no, you typed \"{confirmation}\", so we decided to restart the program.")
            print("Restarting the program...")
            sleep(1)
            continue

# The program might have bugs in it