# Python Tutorial 2
# https://youtu.be/VchuKL44s6E

# Data Types

# DT 1 = Int // pozitif veya negatif tam sayi
1472912472
-28947275

# DT 2 = Float // virgüllü sayi 
32785.7
-23752.3

# DT 3 = String // tek veya cift tirnak icine yazilan her sey (sayida olabilir)
'31'
"Hello World!"

# DT 4 = Bool 
True
False


# Printing sth on the screen
print("Hello", 'end', 87, False, end='\n') # sondaki komut bir sonraki satira gecmesini soyluyor
print('Hello')


# Variables
name = 'Taha'
print(name)


# User Input
user_name = input("Type your name: ")  # yazilan isim user_name string i olarak kaydedilecek
user_age = input("Type your age: ")
print("Hello " + user_name + ", you are " + user_age + " years old." )


# Arithmetic Operators 
# + , * , / , - 
# ** (karekök) , // (sonuc ne olursa olsun küsüratsiz cevap verir) , % (bölme isleminden sonra artan sayiyi gosterir)

x = 20.9
y = 12948
result = x + y
print(result)

# Conditional Operators 

# == (esittir)  
# != (esit degildir) 
# <= (kucuk yada esit) 
# >= (büyük yada esit) 
# < (kucuktur) 
# > (buyuktur)

goals = 100
assists = 55
print (goals != assists)


# If/elif/else
name = input("Name: ")

if name == 'Taha':
    print('You are great!')
elif name == 'Joe':
    print('Bye Joe')
elif name == 'Curry':
    print('GOAT')
else:
    print('ok')


# For loops

for i in range(10):  # parantez icine 3 sayi girilebilir // 1 - baslangic / 2 - bitis / 3 - aralik // tek bir sayi girersen, o sayi bitis sayisi olur
    print(i)     # 0 dan 9 a kadar sayilari yazar

# Comprehensions

a = [[0 for x in range(100)] for x in range(5)]    # listeyi komut ile olusturmak
print(a)


# Functions

def func(x, y):
    print('Run' , x, y)

func(5, 6)


# F string

tom = 57

g = f'Hello, {18 * 8} {tom}'









