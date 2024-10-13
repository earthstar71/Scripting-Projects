from time import sleep
print("The clock has started:")
i = 60
print(i)
for x in range(59):
    sleep(1)
    i -= 1
    print(i)
print("1-minute countdown ended.")

# REQUIREMENTS:
# ------------
# You must have Python installed on your device, it installs pip tool and time package by default

# You must have time package installed on your system

# Install it by typing "pip install time" in Windows Command Prompt if it isn't installed already