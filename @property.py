class Mhs:
    def __init__(self, nama, nim):
        self._nama= nama
        self._nim = nim
        
    @property
    def nama(self):
        #getter untuk atribut nama
        return self._nama

    @nama.setter
    def nama(self, value):
        #setter untuk atribut nama
        if not value:
            raise ValueError("Nama tidak boleh kosong")
        self._nama = value

    @property
    def nim(self):
        #getter untuk atribut nim
        return self._nim

    @nim.setter
    def nim(self, value):
        #setter untuk atribut nim
        self._nim = value

#contoh penggunaan :
mhs_asia = Mhs("gzng","242011288")
print(mhs_asia.nama) #output: gzng
print(mhs_asia.nim) #output: 242011288