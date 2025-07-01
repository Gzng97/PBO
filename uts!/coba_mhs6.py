class Mhs:
    __jumlah = 0
    def __init__(self, nama, nim):
        self.__nama=nama
        self.__nim=nim
        Mhs.__jumlah+=1

    @property
    def nama(self):
        return self.__nama
    
    @property
    def nim(self):
        return self.__nim
    
    @nama.setter
    def nama(self,value):
        self.__nama=value
    
    @nim.setter
    def nim(self,value):
        self.__nim=value

    @staticmethod
    def getJumlah1():
        return Mhs.__jumlah
        
mhs_asia=Mhs("Andi","2434837457")
print(mhs_asia.nama)
print(mhs_asia.nim)
mhs_asia.nama="Budi"
mhs_asia.nim="34455666"
print(mhs_asia.nama)
print(mhs_asia.nim)

print(mhs_asia.getJumlah1()) #objek
print(Mhs.getJumlah1()) #class
