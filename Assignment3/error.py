def calculate_bmi(weight, height_feet, height_inches):
    total_height_inches = (height_feet * 12) + height_inches  
    if total_height_inches == 0:  # 3 Validation
        raise ValueError("Height cannot be zero.")
    bmi = (weight * 703) / (total_height_inches ** 2)
    return bmi


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi <= 24.9:
        return "normal weight"
    elif 25 <= bmi <= 29.9:
        return "overweight"
    else:
        return "obesity"


def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))  # 1 Data type validation
            if min_value <= value <= max_value:  # 3 Range validation 
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.") 
        except ValueError:
            print("Please enter a numeric value.")  #2 Exception handling


def main():
    print("BMI Calculator")
    # Range and constraint validation
    weight = get_valid_input("Enter your weight in pounds: ", 30, 600)  
    height_feet = get_valid_input("Enter your height in feet: ", 2, 8)  
    height_inches = get_valid_input("Enter your height in inches: ", 0, 11)  

    bmi = calculate_bmi(weight, height_feet, height_inches)
    category = determine_bmi_category(bmi)
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"This is categorized as {category}.")


main()
