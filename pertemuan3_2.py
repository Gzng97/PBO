class mhs():
    def __init__(self, nim, nama, gender, prodi) :
        self.nim = nim
        self.nama = nama
        self.gender = gender
        self.prodi = prodi
    
saya = mhs("242011288", "gesang", "Laki-laki", "Teknik Informatika")
temanku1 = mhs("242011289", "budi", "Laki-laki", "manajemen")
temanku2 = mhs("242011290", "siti", "Perempuan", "Akuntansi")

print('nama saya:', saya.nama)
print('kuliah di asia malang dengan NIM:', saya.nim)
print('nama teman saya:', temanku1.nama, "dengan NIM:", temanku1.nim, "gender :", temanku1.gender, "prodi :", temanku1.prodi)
print('nama teman saya:', temanku2.nama, "dengan NIM:", temanku2.nim, "gender :", temanku2.gender, "prodi :", temanku2.prodi)