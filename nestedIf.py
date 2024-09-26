weather = input("What is the weather condition: ")
time_of_day = input("time of day: ")

if weather == "sunny":
    if time_of_day == "day":
        print("You can play the cricket. ")
    else:
        print("You cant play cricket. ")
elif weather == "rainy":
    print("You play with your teddy bear toy. ")
elif weather == "snowy":
    if time_of_day == "night":
        print("You play with teddy bear. ")
    else:
        print("You play with your snowman toy. ")
else:
    print("You stay inside home and read a story books. ")