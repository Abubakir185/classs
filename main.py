class Hayvon:
    def __init__(self, nomi, yosh, turi):
        self.nomi = nomi
        self.yosh = yosh
        self.turi = turi

    def info(self):
        print(f"mening ismim {self.nomi}, mening yoshim {self.yosh}da, men {self.turi}man")



hayvon_1 = Hayvon("Shamshod", 4, "kuchuk")
hayvon_2 = Hayvon("Yolbars", 6, "mushuk")

hayvon_1.info()
hayvon_2.info()


