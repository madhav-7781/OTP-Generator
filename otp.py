# OTP-Generator
One time password generator using random
import random as r
def otpgenerator():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print("Your One time Password is")
    print(otp)
otpgenerator()
