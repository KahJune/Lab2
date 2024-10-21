def main(): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    num_list = get_user_input()
    a = calc_average(num_list)
    b = find_min_max(num_list)
    c = sort_temperature(num_list)
    d = calc_median_temperature(c)
    print("The average is: ", a)
    print("The minimum is: ", b[0])
    print("The maximum is: ", b[1])
    print("The sorted list is: ", c)
    print("The median is: ", d)

def display_main_menu(): 
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    x = x.split(',')
    y = []
    for i in x:
        y.append(float(i))
    return y

def calc_average(num_list):
    i = 0
    totals = 0
    for total in num_list:
        totals += total
        i+=1
    average = totals / i
    return average

def find_min_max(num_list):
    min = num_list[0]
    for i in num_list:
        if i < min:
            min = i
    max = 0
    for i in num_list:
        if i > max:
            max = i
    return [min, max]

def sort_temperature(num_list):
    num_list.sort()
    return num_list

def calc_median_temperature(num_list):
    i = len(num_list)
    if i%2 == 0:
        median = (num_list[i//2] + num_list[i//2 - 1]) / 2
    else:
        median = num_list[i//2]
    return [median]

if __name__ == "__main__": main()