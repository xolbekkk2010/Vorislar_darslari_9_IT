"""
    for loop sikl yaratishda ishlatiladi
"""


oquvchilar = ["kamoltoy","bobur","atxam","izzat","laziz","mirkomil"]

# print(f"assalomun alaykum hurmatli {oquvchilar[0]}, ishlar qanday")
# print(f"assalomun alaykum hurmatli {oquvchilar[1]}, ishlar qanday")
# print(f"assalomun alaykum hurmatli {oquvchilar[2]}, ishlar qanday")
# print(f"assalomun alaykum hurmatli {oquvchilar[3]}, ishlar qanday")
# print(f"assalomun alaykum hurmatli {oquvchilar[4]}, ishlar qanday")
# print(f"assalomun alaykum hurmatli {oquvchilar[5]}, ishlar qanday")


# for ism in oquvchilar:
#     print(f"assalomu alaykum {ism.title}")
#     print(f"xayr hurmatli{ism.upper}")


# raqamlar = list((1,5,9,-8,63))

# for son in raqamlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# raqamlar1 = range(30,91)
# for son in raqamlar:
#     print(f"{son} sonlarni 9 ga bolganda javob:", {son/9})

raqamlar2 = range(27,54,7)
daraja = []
print(f"asl royhat :{raqamlar2}")
for son in raqamlar2:
    daraja.append(son**4)
print(f"4-darajaga oshgan royhat {daraja}")