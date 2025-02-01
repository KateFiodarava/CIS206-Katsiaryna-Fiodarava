
# BMI 

weight = float(input("Enter your weight in pound: "))
height_feet = float(input("Enter your height in feet: "))
height_inches = float(input("Enter your height in inches:"))

total_height_inches = (height_feet * 12) + height_inches  
bmi = ( weight * 703 ) / (total_height_inches ** 2)
    

if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi <= 24.9:
    category = "normal weight"
elif 25 <= bmi <= 29.9:
    category = "overweight"
else:
    category = "obesity"


print(f"Your BMI is: {bmi:.1f}")
print(f"This is {category}")


