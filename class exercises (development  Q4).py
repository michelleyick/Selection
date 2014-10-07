#Michelle Yick
#06-10-2014
#Selection class exercises development Q4

mark = int(input("Please enter your exam mark:"))

if mark > 81 and mark < 100 or mark == 100 or mark == 81:
    print("You've achieved a grade A")

elif mark > 71 and mark < 80 or mark == 71 or mark == 80:
    print("You've achieved a grade B")

elif mark > 61 and mark < 70 or mark == 61 or mark == 70:
    print("You've achieved a grade C")

elif mark > 51 and mark < 60 or mark == 51 or mark == 60:
    print("You've achieved a grade D")

elif mark > 41 and mark < 50 or mark == 41 or mark == 50:
    print("You've achieved a grade E")

elif mark > 0 and mark < 40 or mark == 0 or mark == 40:
    print("You've achieved a grade U")

else:
    print("You have entered an invalid number. Please enter a number between 0 and 100")
