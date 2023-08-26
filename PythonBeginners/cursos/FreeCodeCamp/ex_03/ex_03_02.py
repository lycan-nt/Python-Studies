sHours = input("Enter Hours: ")
sRate = input("Enter Rate: ")
try:
    fHours = float(sHours)
    fRate = float(sRate)
except:
    print("Error, please enter numeric input.")
    quit()

if fHours > 40 :
    reg = fHours * fRate
    otp = (fHours - 40.0) * (fRate * 0.5)
    print(reg, otp)
    xp = reg + otp
else:
    xp = fHours * fRate
print("Pay: ", xp)