sHours = input("Enter Hours: ")
sRate = input("Enter Rate: ")
fHours = float(sHours)
fRate = float(sRate)

if fHours > 40 :
    print("Overtime")
    reg = fHours * fRate
    otp = (fHours - 40.0) * (fRate * 0.5)
    print(reg, otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fHours * fRate
print("Pay: ", xp)