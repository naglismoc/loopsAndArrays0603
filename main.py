import random

from sympy import isprime

for i in range(5): # [0,1,2,3,4]
    print("labas")
    print("rytas")
    print(i)

print("zemiau ciklo")

num = 24
#       0  1  2   3  4
nums = [1, 2, 15, 8, 10] #masyvas
print(nums)
print(nums[0])
print(nums[2])

nums.append(14) #prideti nauja nari
print(nums)
nums[1] = 16 #pakeisti viena skaiciu kitu
print(nums)
nums.remove(16)#pasalinti nurodyta reiksme
print(nums)
#           0       1               2       3       4  - indexai visada yra vienu sk mazesni nei masyvo ilgis
games = ['zelda', 'final fantasy', 'gta', 'nfs', 'top heroes']
print(games)
print(games[3])

for number in nums:
    print(number)
print("-----------------------------")
print(len(games)) # pasako kiek yra elementu masyve
for zaidimas in games:
    print("My favorite game is " + zaidimas)

i % 10 == 0


count = 0
for i in range(50):
    print(i)
    count += 1

print("prasisuko", count)

count_prime = 0
for i in range(10,100):
    if isprime(i):
        print(i)
        count_prime += 1
print("pirminiu skaiciu radome",count_prime)


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("---------------------")

for i in range(1,10):
    if i % 4 == 0:
        break
    print(i)

#loop loop
#while

counter = 0
while True:
    counter +=1
    if counter >= 5:
        break
    print(counter)
print("------------------------")
while True:
    rnd_num = random.randint(1,6)
    if rnd_num == 1:
        break
    print(rnd_num)

print("------------------------")

is_even = False

while not is_even:
    rnd_num = random.randint(0,10)
    if rnd_num % 2 == 0:
        is_even = True
    print(rnd_num)


print("------------------------")

is_not_even = True

while is_not_even:
    rnd_num = random.randint(0,10)
    if rnd_num % 2 == 0:
        is_not_even = False
    print(rnd_num)

print("okey, o dabar testuojame gita :)")


for y in range(1, 11):#3
    for x in range(1,11):#1;2;3
        print(y * x, end=" ")
    print()
print("paslepta zinute")









