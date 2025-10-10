'''def pyramid_volume():
    b=int(input ("Enter breadth"))
    h=int(input("enter height"))
    volume= (b ** 2 * h)/3
    return round (volume, 2)
print("volume of pyramid:", pyramid_volume())

import math
def volume_cone():
    h=int(input("Enter height:"))
    r= int(input("Enter r:"))
    volume=math.pi*(r**2 * h)/3
    return round(volume, 2)

print ("Volume of a cone is:", volume_cone())


def pointers_basket():
    twopointers=int(input("enter number of teo points"))
    threepointers=int(input("enter number of teo points"))
    final_points=2 * twopointers+ 3 * threepointers
    return round(final_points)
print("Final points is:", pointers_basket())


def total_batteries():
   

# Get input from user
    e_dolls = int(input("Enter number of electronic dolls: "))
    rc_cars = int(input("Enter number of remote-controlled cars: "))
    robo_dogs = int(input("Enter number of robot dogs: "))
    total=    ( e_dolls * 2) + (rc_cars * 4) + (robo_dogs * 6)
    return round(total)

# Print total batteries
print("Total batteries needed =", total_batteries())




def avg_ath():
    age=int(input("enter age"))
    athl_goal=input("enter below average or above")
    if 20<= age <= 39:
        rate= "47-72" if athl_goal=="Above Average" else "73-93"
    if 40<= age <= 59:
        rate= "46-71" if athl_goal=="Above Average" else "72-94"
    return (rate)
print("Your atheticc goal is:", avg_ath())


def pool_time():
    grade= input("enter your grade")
    time=input("enter time:")
    if grade=='k' or grade in ['1', '2', '3']:
        pool="9am" if time=="Morning" else "1pm"
    elif grade in ['4', '2', '8']:
        pool="10 am" if time=="Morning" else "2pm"
    elif grade in ['9', '10', '11', '12']:
        pool="11am" if time=="Morning" else "3pm"
    return pool
print("Your pool time is:", pool_time())


def traffic_light():
    light_color= input("enter the colour red/green/yellow")
    if light_color=="green":
        color="go"
    elif light_color=="red":
        color="stop"
    elif light_color=="yellow":
        color="yield"
    else:
        color="invalid entry"
    return color
print (traffic_light())

'''