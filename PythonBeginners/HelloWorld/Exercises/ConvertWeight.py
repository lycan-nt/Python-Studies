weight = float(input("What's your weight? "))
measure = input("What's measure? (K) kilo or (L) libra ")

if measure.upper() == 'L':
    weight = weight // 2.2046
    print("Your weight is: ", weight, " KG")
elif measure.upper() == 'K':
    print("Your weight is: ", weight, " KG")
else:
    print("Type Invalid.")
print("Done!")
