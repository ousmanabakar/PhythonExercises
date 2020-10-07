"""Bu projede ise 4 tane sınıfı oluşturun.
Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait
ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait
ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait
ek özellikler ve metodlar ekleyin.

"""
class Hayvan():
    def __init__(self,isim,renk,tür,hareket):
        print("Hayvan sınıfın init functionu")
        self.isim = isim
        self.renk = renk
        self.tür = tür
        self.hareket = hareket
    def bilgigoster(self):
        print(f"""
        Ad : {self.isim}
        
        Renk : {self.renk}

        Tür : {self.tür}

        Hareket şekli : {self.hareket} 

        Ureme şekli : {self.uremeSekli}
        
            """)

class Kopek(Hayvan):
    def __init__(self, isim,renk,tür,hareket, ses):
        print("kopek sınıfın initi")
        super().__init__(isim,renk,tür,hareket)
        self.ses = ses

class Kus(Hayvan):
    def __init__(self,isim,renk,tür,hareket,uremeSekli):
        print("Kuş sınıfın initi")
        self.uremeSekli = uremeSekli
        super().__init__(isim,renk,tür,hareket)
    def __str__(self):
        return f"""
        Ad : {self.isim}
        
        Renk : {self.renk}

        Tür : {self.tür}

        Hareket şekli : {self.hareket} 

        Ureme şekli : {self.uremeSekli}
        
            """

class At(Hayvan):
    def __init__(self,isim,renk,tür,hareket,ses):
        print("At sınıfın initi")
        self.ses = ses
        super().__init__(isim,renk,tür,hareket)

    def __str__(self):


            return f"""
            Ad : {self.isim}

            Renk : {self.renk}

            Tür : {self.tür}

            Hareket şekli : {self.hareket} 
            
            Sesi : {self.ses}

            """




#hayvan = Hayvan("Aslan","Sarışın","omurgalı","koşar veya yürür")
#hayvan.bilgigoster()
#kus = Kus("Deve kuşu","siyah beyaz","Aves","Yürür","Yumurtalar")
#print(kus)
at = At("Eşek","siyah beyaz","Yabani","koşar ve yürür","anırmak")
print(at)

