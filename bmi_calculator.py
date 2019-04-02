# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit



#gets the users weight and saves it int he variable weight, in format float not integer because that would be bad
weight = float(input("Enter your weight in Kilograms:"))


#get user Height
height = float(input("Enter your height in Meters:"))


bmi = (weight/(height * height))
#print bmi


print ("Your BMI is:", bmi)


if bmi <= 18.5:
        print ("You are Underweight")

if  18.6 < bmi < 24.9:
        print ("You are Normal Weight")

if  25 < bmi < 29.9:
        print ("You are OverWeight")

if  30 < bmi:
        print ("You are Obese")



