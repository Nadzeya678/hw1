# Walle
txt1 = input()
l = len(txt1)
print(txt1.lower)
print(l)
cnt = txt1.count('Earth')
print(cnt)
txt2 = txt1.replace("WALLE", "WALL-E")
print(txt2)

# Високосный год
a = input('Введите номер года:')
a = float(a)
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Год високосный')
else:
    print('Год не високосный')

# Индекс массы тела
wht = input('Введите массу тела, кг:')
hgt = input('Введите рост,м:')
age = input('Введите возраст, полных лет:')
wht = float(wht)
hgt = float(hgt)
age = float(age)
ind = wht/hgt**2
print('ИМТ=',(ind))
if age < 45:
    if ind < 22:
        print('Недостаточная масса тела')
    elif 22 < ind < 26.99:
        print('Норма')
    elif 27 < ind < 31.99:
        print('Избыточная масса тела')
    elif ind >= 32:
        print('Ожирение')
elif age >= 45:
    if ind < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 < ind < 24.99:
        print('Норма')
    elif 25 < ind < 29.99:
        print('Избыточная масса тела')
    elif ind >= 30:
        print('Ожирение')
