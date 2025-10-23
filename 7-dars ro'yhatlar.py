"""
21.10.2025
Pyhton List Operations
"""

# ism = 'Ali'
# uy_manzili = 'Toshkent shaxri, Chilonzor tumani'

# print(ism.capitalize())
# print(ism.upper())
# print(uy_manzili.capitalize())
# print(uy_manzili.title())


# # Pyhtonda List (ro'yhat) bilan ishlash

# hayvonlar = ['mushuk', 'it', 'quyon', 'tovuq', 'sigir']
# oila = ['Ota', 40, 'Ona',38, 'Aka',17, 'Opa',15, 'Bola',10]
# mashinalar = ['Toyota', 'BMW', 'Mercedes', 'Kia', 'Supra']

# hayvonlar = ['mushuk', 'it', 'quyon', 'tovuq', 'sigir']
# # index      :      0        1      2        3        4

# print(hayvonlar) # mushuk
# qiymat = hayvonlar[3]
# print(qiymat)

# mashinalar = ['Toyota', 'BMW', 'Mercedes', 'Kia', 'Supra']
# # index             0       1           2      3       4
# print(mashinalar[0]) 
# print(mashinalar[-1])
# print(mashinalar[1].title())
# print(mashinalar[-2].upper())


davlatlar = ['ozbekiston','portugaliya','angentina','fransiya','ispaniya','meksika','niderlandiya','xorvatiya']
# index                 0            1           2          3           4       5               6           7
print(davlatlar) # ispaniya
print(davlatlar[-4].title())
print(davlatlar[-1].title())
print(davlatlar[-2].title())
print(davlatlar[-3].title())
print(davlatlar[-5].title())
print(davlatlar[-6].title())
print(davlatlar[-7].title())
print(davlatlar[-8].title())



It_oquvchilar = []

It_oquvchilar.append('kamolbek')
It_oquvchilar.append('elbek')
It_oquvchilar.append('zuhriddin')
It_oquvchilar.append('umid')
It_oquvchilar.append('bahtiyor')
print(It_oquvchilar)

It_oquvchilar.insert(2,'elbek')
It_oquvchilar.insert(0,'kamolbek')
print(It_oquvchilar)