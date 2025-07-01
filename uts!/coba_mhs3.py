class mhs():
    def __init__(self, nim , nama, gender, prodi):
        self.nim=nim
        self.nama=nama
        self.gender=gender
        self.prodi=prodi

saya=mhs("242011103","Septa","laki-laki","TI")
temanku_1=mhs("242013987","Taufik","Laki-laki","Manajemen")
temanku_2=mhs("242015987","Wati","Perempuan","DkV")
print("Aku seorang "+saya.gender+" bernama "+saya.nama+' Kuliah di Institut Asia Malang di prodi '+saya.prodi+" mempunyai teman di prodi "+temanku_1.prodi+" namanya "+temanku_1.nama)
print("Aku juga punya teman "+temanku_2.gender+" di prodi "+temanku_2.prodi+" namanya "+temanku_2.nama)
print("NIM kami bertiga adalah : "+saya.nim+" , "+temanku_1.nim+" , "+temanku_2.nim)