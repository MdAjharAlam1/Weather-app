def running_main_code(link):
    if link == "1":
        print()
        print("you have to selected GUI Weather option")

        import gui_weather
    elif (link == "2"):
        print("you have selected Normal weather option")
        print()

        import normal_weather
    else:
        print("select only 1 for GUI Weather and 2 for Normal Weather")
        link = input("Please Enter Your Option :- >   ")
        running_main_code(link)

print("what do you want to select GUI Weather or Normal Weather")
print()
print("select 1 for GUI Weather")
print("select 2 for Normal Weather")

selection_button = input("Please Enter Your Option :- >   ")
print()
running_main_code(selection_button)