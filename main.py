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


print(sep="")


print(*[item for item in nums], sep=", ")

num = 4
arr = [1,5,10,4,8,5]

grades = [
    [1,2,3,4,4,5],# matieka
    [4,5,6],# lietuviu
    [8,5,10],# tikyba
    [4,8,8,10],#anglu
    [7,5,3,4],#fizika
    [10,4,10]#kūno kultūra
]
total_sum = 0
total_count = 0
for lesson in grades:
    sum = 0
    count = 0
    for grade in lesson:
        sum += grade
        count += 1
    total_sum += round(sum / count)
    total_count +=1
print(total_sum / total_count)


sum = 0
count = 0

for lesson in grades:
    for grade in lesson:
        sum += grade
        count += 1
print(sum,count, sum / count)


students = [
    ['Rima', ' Beitnorė', 1988, 'da'],
    ['Neringa', ' Dainauskė', 1988, 'da'],
    ['Lukas', ' Bukauskas', 1989, 'da'],
    ['Tomas', ' Strelčiūnas', 1985, 'da']
]

print(students)



# Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.
#

all_nails_count = 0
for i in range(5):
    taukst_total = 0
    taukst_count = 0
    while taukst_total < 85:
        taukst = random.randint(5,20)
        taukst_total += taukst
        taukst_count += 1
    # print(taukst_count, taukst_total)
    all_nails_count += taukst_count
# print("-----------",all_nails_count)

all_nails_count = 0
for i in range(5):
    taukst_total = 0
    taukst_count = 0
    while taukst_total < 85:
        taukst_count += 1
        if random.randint(0,1) == 1:
            taukst = random.randint(20,30)
            taukst_total += taukst
    # print(taukst_count, taukst_total)
    all_nails_count += taukst_count
# print("-----------",all_nails_count)










