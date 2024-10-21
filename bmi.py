def calculate_bmi(height, weight):
    print("Height = " + str(height)) 
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    
calculate_bmi(weight=57, height=1.73) 