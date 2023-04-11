# Midterm Project 1
# Paul Takemoto

def main():
    fat_grams = float(input('Enter amount of fat in grams: '))
    carb_grams = float(input('Enter amount of carbohydrates in grams: '))

    calories_fat = get_calories_fat(fat_grams)
    calories_carbs = get_calories_carbs(carb_grams)

    print(f'Calories from fat: {calories_fat: .1f}')
    print(f'Calories from carbohydrates: {calories_carbs: .1f}')

def get_calories_fat(grams):
    calories = grams * 9
    return calories

def get_calories_carbs(grams):
    calories = grams * 4
    return calories

# Calls main function
main()
