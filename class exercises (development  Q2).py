#Michelle Yick
#06-10-2014
#Selection class exercises development Q2

temperature = int(input("Please enter the water's temperature in Centigrade"))

if temperature > 100 or temperature == 100:
    print("The water is boiling")
elif temperature < 0 or temperature == 0:
    print("The water is in a frozen state")
else:
    print("The water is neither frozen or boiling.")
    
