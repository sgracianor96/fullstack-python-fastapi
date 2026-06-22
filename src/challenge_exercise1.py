weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
while weight < 1 or weight > 500 or height < 0.5 or height > 2.5:
    print("Invalid weight or height. Please enter a weight between 1-500 kg and a height between 0.5-2.5 meters.")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}. You are obese.")