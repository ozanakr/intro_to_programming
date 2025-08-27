# define a float
y = 1.
print(y)
print(type(y))

# convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

print(3 * True)
print(-3.1 * True)
print("abc" * False)

# complete the function
def get_expected_cost(beds, baths, has_basement):
    value = 80000 + (beds * 30000) + (baths * 10000) + (has_basement * 40000)
    return value

print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

def cost_of_project(engraving, solid_gold):
    cost = solid_gold * 100 + (not solid_gold) * 50 + len(engraving) * (7 + (3 * solid_gold))
    return cost

project_one = cost_of_project("Charlie+Denver", True)
print(project_one)