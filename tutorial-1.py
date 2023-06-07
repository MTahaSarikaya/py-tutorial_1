# Python Tutorial 1
#https://www.youtube.com/watch?v=kqtD5dpn9C8

# print("hello world!") 
# print("this is a test file")


first = 10.1
second = 20

print(first + second)

#input

first = input('First: ')
second = input("Second: ")
sum = float(first) + float(second)
print (sum)

#if statement

age = 17
if age >= 18:
    print("tebrikler, ince ye oy verebilirsin :D")
else: print("üzgünüm, bir daha ki secime")

#kg/lbs calculator

weight = int(input('Weight: '))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

#while loops

i = 1
while i <= 7:
    print(i * 's') # 's' yi 7 ye kadar calistir
    i = i + 1

# lists

names = ['lebron', 'jordan', 'kobe', 'curry', 'kd' ]
names[0] = 'LeBron' # listedeki ismi degistirmek icin
print(names[0:3]) # x:y baslangic ve bitis sayilari icin kullanilir
names.append("Taha") # listeye ekleme
names += [274927, "Kyrie"]  # listeye birden fazla item ekleme / ayni zamanda names.extend() kullanilabilir
names.remove("jordan") # listeden item silmek
names.insert(2,"sjsjasj") # belirtilen siraya item eklemek

# tuple in listeden farki icindeki itemlerle oynanilamaz olmasidir!


# for loops 

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

i=0
while i < len(numbers):
   print(numbers[i])
   i = i + 1

# range function 

numbers = range(9, 21, 3) # range(x, y, z) // x = baslangic sayisi // y= bitis sayisi (yazili sayinin bir eksigi) // z = sayi araligi
for number in numbers:
    print(number)


