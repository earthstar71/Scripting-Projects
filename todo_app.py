from win11toast import *


name = input("Welcome to this Todo App. Please enter you name to contine (press \"q\" to exit): ")

task = input(f"Hello, {name.title()}! Add a task to get to the next step: ")

url = input(f"Please enter a url to open your task: ")


# date = input(f"Please enter a date for your task: ")

# time = input(f"Please enter a time to be reminded of your task: ")
# f = open(path, "w")
# f.write(name)
# f.writelines(task.capitalize())
# f.writelines(date)
# f.writelines(time)


toast(name.title() + ", it's time to do " + task.capitalize(), 'Click to open task', on_click="https://www." + url)


# Install win11toast or win10toast on your system by typing pip install win11toast or win10toast in Windows Command Prompt

# Shows toast notification reminding you to do a task, also shows url to click on

# When the program asks you to enter a url, don't start your url with https://www., the program adds that prefix itself