#instance variable

class Mhs:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    #geter untuk nama
    def get_nama(self):
        return self.__nama
    
    #setter untuk nama
    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    #getter untuk umur
    def get_umur(self):
        return self.__umur
    
    #setter untuk umur
    def set_umur(self, umur_baru):
        if umur_baru > 0: #validasi sederhana
            self.__umur = umur_baru
        else:
            print("Umur Harus Positip")

#creating object
mhs_asia = Mhs("andi", 20)

#mengakses data menggunakan getter
print(mhs_asia.get_nama()) #output: andi
print(mhs_asia.get_umur()) #output: 28

#mengubah data menggunakan setter
mhs_asia.set_nama("budi")
mhs_asia.set_umur(21)

#melihat hasil perubahan
print(mhs_asia.get_nama()) #output: budi
print(mhs_asia.get_umur()) #output: 21