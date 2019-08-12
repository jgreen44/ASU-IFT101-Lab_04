#   Filename:           Lab 4
#   Created by:         jasongreen
#   Date:               Wednesday, January 30, 2019
#   Time of Creation:   17:45
#   ---

paintPerGallon = 100
roomArea = (2 * (12 * 8)) + (2 * (10 * 8))
window1_Area = 5 * 3
window2_Area = 6 * 2

totalAreaToPaint = (roomArea - window1_Area - window2_Area) / paintPerGallon
print(str(totalAreaToPaint) + ' gallons')


import math

paper_per_ream = 500
report_pages = 140
people_in_attendance = 25

reams_to_get = math.ceil(((people_in_attendance + 5) * report_pages) / paper_per_ream)
print(reams_to_get)


grade = int(input("What grade did you get? "))

if grade > 89:
    print("You received an A.")
elif 79 < grade <= 89:
    print("You received a B.")
elif 69 < grade <= 79:
    print("You received a C.")
elif 59 < grade <= 69:
    print("You received a D.")
else:
    print("You received an F.")


a = 10
b = 20
c = 30

if a > b and a > c:
    print("{} is greater than {} and {}".format(a, b, c))
elif b > a and b > c:
    print("{} is greater than {} and {}".format(b, a, c))
else:
    print("{} is greater than {} and {}".format(c, a, b))



a = 30
b = 40
c = 10

if a > b and a > c:
    if b > c:
        print(a, b, c, "a, b, c")
    else:
        print (a, c, b, "a, c, b")
elif b > a and b > c:
    if a > c:
        print(b, a, c, "b, a, c")
    else:
        print(b, c, a, "b, c, a")
else:
    if a > b:
        print(c, a, b, "c, a, b")
    else:
        print(c, b, a, "c, b, a")

def employee_pay():
    hourlyRate = 15
    overtimeRate = 20
    salaryRate = 500
    hourlyPay = 0

    if category == "Y" or category == "y":
        if hours >= 40:
            hourlyPay = (hourlyRate * 40 ) + ((hours - 40) * overtimeRate)
            print("You made ${} this week!".format(hourlyPay))
        else:
            hourlyPay = hourlyRate * hours
            print("You made ${} this week!".format(hourlyPay))
    else:
        print("You made your salary rate of ${}!".format(salaryRate))


category = input("Are you paid hourly? (y/n): ")
if category == "Y" or category == "y":
    hours = int(input("How many hours did you work? "))
    employee_pay()
else:
    employee_pay()




