# Mavzu: Sinflar bilan tanishish - hayvonlarni yaratish 1. “Hayvon” sinfini yarating: - Sizning sinfingiz 
# hayvonning nomi, yoshi va turi uchun atributlarga (o'zgaruvchilar) ega bo'lishi kerak. - Hayvon haqidagi 
# ma'lumotni ko'rsatish uchun usul (funktsiya) qo'shing, masalan: ""Mening ismim [ism], men [yosh] yoshdaman va 
# men [hayvon turi]"". 


class Odam:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type


hayvon_1 = ("Temur", "5", "kuchuk")
hayvon_2 = ("Shamshod", "4", "mushuk")


print(hayvon_1)
print(hayvon_2)


