print("Body-mass-index calculator")

def calculateBMI(weight,height):
    bmi = weight/height**2
    return bmi

weight = float(input('Please enter your weight in kgs:'))
height = float(input('Please enter your height in m:'))

bmi=calculateBMI(weight,height)

print("Your BMI value is:",bmi)
print("Thank you")