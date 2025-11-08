# For sikl operatoriga oid masalalar
# For6.
#1.2 kg dan 2 kg gacha bo'lgan narxlarni chiqarish
# narx = int(input("1 kg konfetni narxini kiriting"))
# for i in range(12, 21, 2):
#      print(i/10 * narx)

# For7.
# a = int(input("a ni kiriting"))
# b = int(input("b ni kiriting"))
# son = list(range(a, b+1))
# print(sum(son))

# # For8.
# a = int(input("a ni kiriting : "))
# b = int(input("b ni kiriting : "))
# kopaytma = 1
# sonlar = list(range(a, b+1))
# print(f"Royhat : {sonlar}")
# for i in sonlar:
#     kopaytma *= i # kopaytma = kopaytma * i
# print(f"Royhatning kopaytmasi : {kopaytma}")

# For9.
# a = int(input("a ni kiriting : "))
# b = int(input("b ni kiriting : "))
# sonlar = list(range(a, b**2))
# print(f"Royhat : {sonlar}")
# for i in sonlar:
#     sonlar*= i
# print(f"Royhatning kvadrati : {sonlar}")


# For10.
# n = int(input("n = "))
# S = 0
# for i in range(1, n + 1):
#     S += 1 / i
# print("Yig'indi =", S)


# For11
# n = int(input("n = "))
# S = 0
# for i in range(1, n + 1):
#     S += (i + n) ** 2
# print("Yig'indi =", S)

# For12
# n = int(input("n = "))
# P = 1
# for i in range(1, n + 1):
#     P *= i
# print(f"{n}! =", P)


# For13
# n = int(input("n = "))
# S = 0
# ishora = 1
# for i in range(1, n + 1):
#     S += ishora * i
#     ishora *= -1
# print("Natija =", S)

# # For14
# n = int(input("n = "))
# S = 0
# for i in range(1, n + 1):
#     S += 2 * i - 1
#     print(f"{i} ning kvadrati: {S}")

# # For15
# a = float(input("a = "))
# n = int(input("n = "))
# natija = 1
# for i in range(n):
#     natija *= a
# print("Natija:", natija)

# # For16
# a = float(input("a = "))
# n = int(input("n = "))
# for i in range(1, n + 1):
#     print(f"{i}-daraja: {a ** i}")

#     # For17
# a = float(input("a = "))
# n = int(input("n = "))
# S = 0
# for i in range(1, n + 1):
#     S += a ** i
# print("Yig'indi =", S)

# # For18
# a = float(input("a = "))
# n = int(input("n = "))
# S = 0
# for i in range(1, n + 1):
#     S += (-1) ** (i + 1) * a ** i
# print("Yig'indi =", S)


# # For19
# n = int(input("n = "))
# P = 1
# for i in range(1, n + 1):
#     P *= i
# print(f"{n}! =", P)

# # For20
# n = int(input("n = "))
# S = 0
# f = 1
# for i in range(1, n + 1):
#     f *= i
#     S += f
# print("Yig'indi =", S)


# # For21
# n = int(input("n = "))
# S = 1
# f = 1
# for i in range(1, n + 1):
#     f *= i
#     S += 1 / f
# print("Yig'indi (e ga yaqinlashadi) =", S)

# # For22
# x = float(input("x = "))
# n = int(input("n = "))
# S = 1
# f = 1
# for i in range(1, n + 1):
#     f *= i
#     S += x ** i / f
# print("Yig'indi (e^x ga yaqinlashadi) =", S)

# # For23
# x = float(input("x = "))
# n = int(input("n = "))
# S = 0
# for i in range(n + 1):
#     S += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
# print("Yig'indi (sin(x) ga yaqinlashadi) =", S)

# # For24
# x = float(input("x = "))
# n = int(input("n = "))
# S = 0
# for i in range(n + 1):
#     S += ((-1) ** i) * (x ** (2 * i)) / (2 * i)!
# print("Yig'indi (cos(x) ga yaqinlashadi) =", S)

# # For25
# import math
# x = float(input("x = "))
# n = int(input("n = "))
# S = 0
# for i in range(1, n + 1):
#     S += ((-1) ** (i - 1)) * (x ** i) / i
# print("Yig'indi (ln(1+x) ga yaqinlashadi) =", S)