def computepay(hours, rate):
    if fHours > 40 :
        reg = fHours * fRate
        otp = (fHours - 40.0) * (fRate * 0.5)
        print(reg, otp)
        pay = reg + otp
    else:
        pay = fHours * fRate
    return pay

sHours = input("Enter Hours: ")
sRate = input("Enter Rate: ")
try:
    fHours = float(sHours)
    fRate = float(sRate)
    pay = computepay(fHours, fRate)
    print("Pay: ", pay)
except:
    print("Error, please enter numeric input.")
    quit()

