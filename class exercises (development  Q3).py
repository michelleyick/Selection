#Michelle Yick
#10-10-2014
#Selection class exercises development Q3

hours = int(input("Please enter the number of hours you work in one week:"))

if hours > 40 and hours < 60 or hours == 60:
    pay_rate = int(input("Please enter your hourly pay rate:"))
    answer = pay_rate*1.5
    print("The amount of money you will recieve after the extra pay is {0}".format(answer))
    
elif hours < 40 or hours == 40:
    print("Sorry you are not eligable for any extra pay.")
    
else:
    print("Sorry the number you have entered is not in the range")


