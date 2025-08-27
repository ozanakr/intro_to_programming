# Edit the function to return the correct grade for different scores
def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >=80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + (len(engraving) * 10)
    else:
        cost = 50 +  (len(engraving) * 7)
    return cost

# Edit the function to return the correct bill for different values of num_gallons
def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = (num_gallons / 1000) * 5
    elif num_gallons <= 22000:
        bill = (num_gallons / 1000) * 6
    elif num_gallons <= 30000:
        bill = (num_gallons / 1000) * 7
    else :
        bill = (num_gallons / 1000) * 10
    return bill

# Edit the function to return the correct bill for different values of GB
def get_phone_bill(gb):
    if gb <= 15:
         bill = 100
    else:
        bill = 100 + ((gb - 15) * 100)
    return bill
