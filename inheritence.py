class mhs :
    def __init__(self, nim, nama):
        self.__nim = nim
        self.__nama = nama

    @property
    def nim(self):
        return self.__nim 
    
    @property
    def nama(self):
        return self.__nama
    
    @nim.setter
    def nim(self, input):
        self.__nim = input

    @nama.setter
    def nama(self, input):
        self.__nama = input

class Mhs_S1(mhs):
    def __init__(self, nim, nama):
            super().__init__(nim, nama)
            self.jenjang = "sarjana"
            self.max_semester = 14

class Mhs_S2(mhs):
    def __init__(self, nim, nama):
            super().__init__(nim, nama)
            self.jenjang = "pascasarjana"
            self.max_semester = 8

mhs_asia1= Mhs_S1("12345656", "Budi")
mhs_asia2= Mhs_S2("33445666", "Wati")
#mencetak mahasiswa s1 dan s2
print(f"Nama : {mhs_asia1.nama}, NIM : {mhs_asia1.nim}, Jenjang : {mhs_asia1.jenjang}, Max Semester : {mhs_asia1.max_semester}")
print(f"Nama : {mhs_asia2.nama}, NIM : {mhs_asia2.nim}, Jenjang : {mhs_asia2.jenjang}, Max Semester : {mhs_asia2.max_semester}")
#merubah atribut mahasiswa s1
mhs_asia1.nim = "12345678"
mhs_asia1.nama = "Budi Santoso"
#menampilkan hasil perubahan atribut mahasiswa s1
print(f"Nama : {mhs_asia1.nama}, NIM : {mhs_asia1.nim}, Jenjang : {mhs_asia1.jenjang}, Max Semester : {mhs_asia1.max_semester}")