# #input operatoridan foydalanb masala ishlash
# #a = int(input("istalgan son kiriting men uni kub ildizini aniqlab beramn: "))
# # n = a * a * a
# # print("siz kiritgan soning kub ildizi: ", n)

# #kvadratning tomoni berilgan uning perimetirini aniqlash dasturini yozing

# #k_tomoni = int(input("kvadratning tomonini kiriting: "))

# #p = k_tomoni * 4

# #print("kvadratning perimetiri: P = ", p)

# # a = int(input("kvadratni tomonini kiriting men uni yuzini aniqlab beramn : "))
# # n = a * a
# # print(" kvadrat yuzi: s =  ", n)



# # masalalar
# # 6-masala: Paralelepipedning hajmi va sirtini topish

# def paralelepiped_hajm_sirt(a, b, c):
#     hajm = a * b * c
#     sirt = 2 * (a * b + b * c + a * c)
#     return hajm, sirt

# # Misol uchun qiymatlar:
# a = 3
# b = 4
# c = 5

# V, S = paralelepiped_hajm_sirt(a, b, c)

import math

# # 15-masala: Aylana yuzasidan radius va diametrni topish
# def aylana_radius_diametr(S, pi=3.14):
#     R = math.sqrt(S / pi)
#     d = 2 * R
#     return R, d

# # Misol uchun:
# S = 78.5

# radius, diametr = aylana_radius_diametr(S)
# print(f"Radius (R): {radius}")
# print(f"Diametr (d): {diametr}")
# # 24-masala
# # A, B va C sonlari berilgan
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# C = int(input("C ni kiriting: "))

# # Qiymatlarni almashtirish
# temp = A
# A = C
# C = B
# B = temp

# # Natijani chiqarish
# print("Yangi A:", A)
# print("Yangi B:", B)
# print("Yangi C:", C)

# 2 manfiy bo'lmagan son berilgan. ularning o'rta arifmetigini toping
#a = int(input("0 ga va manfiy qiymatga  teng bo'lmagan son kiriting son1 =  "))
# b = int(input("0 ga va manfiy qiymatga teng bo'lmagan son kiriting son2 =  "))
# n = math.sqrt(a * b)
# print("sonlarning o'rta giametrik: ", n)

#A  B VA C sonlari berilgan. A ni B ga, B ni C ga, C ni A ga almashtiring
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: ")) 
# C = int(input("C ni kiriting: "))

# Qiymatlarni almashtirish
# temp = A
# A = C
# C = B
# B = temp
# Natijani chiqarish
#print("Yangi A:", A)
#print("Yangi B:", B)
#print("Yangi C:", C)



