# What do we want to collaborate on?
#
#Hi Sam. Thought I would check to see if you had made any changes overnight and you had! Very good!
#
#
# Sam's Functions go here
#
def oldest_age_calc(eolia, ian, sam, jenny):
    if eolia > ian and eolia > sam and eolia > jenny:
        return 'Eolia'
    elif ian > eolia and ian > sam and ian > jenny:
        return 'Ian'
    elif sam > eolia and sam > ian and sam > jenny:
        return 'Sam'
    elif jenny > eolia and jenny > ian and jenny > sam:
        return 'Jenny'
    else:
        return 'Error!!!!!!'
#
# Ian's Functions go here
#
#
#
eolia_age = 23
ian_age = 50
sam_age = 22
jenny_age = 53

oldest_age = oldest_age_calc(eolia_age, ian_age, sam_age, jenny_age)

combined_age = sam_age + ian_age +eolia_age + jenny_age
print (combined_age)
print ("Ian is " +str(ian_age))
print ("Sam is " +str(sam_age))
print ("Eolia is " +str(eolia_age))
print ("Jenny is " +str(jenny_age))

print ("The oldest is " + oldest_age)


family_ages = {eolia_age: 23, ian_age: 50, sam_age: 22, jenny_age: 53}
total_age = 0

for ages in family_ages.values():
    total_age += ages

print('Their combined age is ' + str(total_age))


