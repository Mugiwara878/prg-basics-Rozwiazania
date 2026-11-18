###
# Prints the weekly meal plan along with day names
#
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

def day_meal_plan(meal_plan, day_number):
    day = meal_plan[day_number-1]
    return f"{day[0]}, {day[1]}, {day[2]}"

print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")
for i in range(1, 8):
    print(f"{weekday(i)}: {day_meal_plan(meal_plan, i)}")