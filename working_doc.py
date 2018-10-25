person_1 = {'first_name':'madalyn', 'last_name':'sowar', 'city':'durham'}

print(person_1)

print('Her name is ' + person_1['first_name'].title() + " " 
+ person_1['last_name'].title() + " and she lives in "
 + person_1['city'].title() + ".")
bs = []
import random
favnums = {}
names = ['john', 'joe', 'maddy', 'bill', 'ron']
for name in names:
    favnums[name] = random.choice(list(range(1, 11)))
    
print(favnums)

for x, y in favnums.items():
    print(x.title() + "'s favorite number is " + str(y) + "!")

for a in favnums:
    print(a.title())

for b in set(favnums.values()):
    b=str(b)
    print(b.title())
    
    bs.append(b)
    

print(bs)
if len(bs) <4:
    
    print('WTF! Random my ass!')
