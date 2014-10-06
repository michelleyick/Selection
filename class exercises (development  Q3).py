#Michelle Yick
#06-10-2014
#Selection class exercises development Q3

hours = int(input("Please enter the number of hours you work in one week:"))

pay_rate = int(input("Please enter your hourly pay rate:"))

if hours > 40:
    print("You will get paid 1.5 times the rate due to extra hours")
elif hours < 0 or hours > 60:
    print("Sorry the number you have entered is not in the range")


