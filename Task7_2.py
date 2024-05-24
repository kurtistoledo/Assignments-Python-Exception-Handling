# 7. Python Exception Handling
# 2. The Recipe Ratio Adjuster

def get_servings_input(prompt):
    while True:
        try:
            servings = float(input(prompt))
            if servings <= 0:
                print("Please enter a positive number of servings.")
            else:
                return servings
        except ValueError:
            print("Please enter a valid numerical value for servings.")

def calculate_adjustment_factor(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        return adjustment_factor
    except ZeroDivisionError:
        print("Error: The original servings cannot be zero.")
        return None

def main():
    print("Welcome to the Recipe Ratio Adjuster!")
    original_servings = get_servings_input("Enter the original number of servings: ")
    desired_servings = get_servings_input("Enter the desired number of servings: ")

    adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)
    if adjustment_factor is not None:
        print(f"Adjustment factor: {adjustment_factor:.2f}")

        # Adjust recipe quantities (you can add your recipe-specific logic here)

    print("Enjoy your cooking!")

if __name__ == "__main__":
    main()
