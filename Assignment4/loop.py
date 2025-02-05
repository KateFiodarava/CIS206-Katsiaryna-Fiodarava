def calculate_bmi(weight, height_feet, height_inches):
    """ Calculates BMI using weight in pounds and height in feet/inches"""
    total_height_inches = (height_feet * 12) + height_inches  
    if total_height_inches == 0:
        raise ValueError("Height cannot be zero.")  # Validation check
    bmi = (weight * 703) / (total_height_inches ** 2)
    return bmi


def determine_bmi_category(bmi):
    """ Determines the BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"


def get_valid_input(prompt, min_value, max_value):
    """ Gets a valid numeric input within a specified range """
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            return None  # Allows user to exit

        try:
            value = float(user_input)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_bmi_table():
    """ Displays a BMI table with height (58-76 inches) and weight (100-250 lbs)."""
    print("BMI Reference Table")
    print("   " + "   ".join(f"{h}in" for h in range(58, 77, 2)))
    
    for weight in range(100, 251, 10):
        row = [f"{weight}lb"]
        for height in range(58, 77, 2):
            bmi = (weight * 703) / (height ** 2)
            row.append(f"{bmi:.1f}")
        print("  ".join(row))


def main():
    """ Main function to run the BMI calculator with input validation and exit option."""
    print("BMI Calculator (Type 'exit' anytime to quit)")

    while True:
        weight = get_valid_input("Enter your weight in pounds: ", 30, 600)
        if weight is None:
            print("Exiting BMI Calculator.")
            break

        height_feet = get_valid_input("Enter your height in feet: ", 2, 8)
        if height_feet is None:
            print("Exiting BMI Calculator.")
            break

        height_inches = get_valid_input("Enter your height in inches: ", 0, 11)
        if height_inches is None:
            print("Exiting BMI Calculator.")
            break

        bmi = calculate_bmi(weight, height_feet, height_inches)
        category = determine_bmi_category(bmi)
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Category: {category}")

        again = input("Would you like to calculate another BMI? (yes/no): ")
        if again != "yes":
            break

    display_bmi_table()


main()
