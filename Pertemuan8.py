from abc import ABC, abstractmethod

class mahasiswa(ABC):
    def __init__(self, nama, nim, prodi):
        self.__nama = nama          #atribut privat dengan __ (enkapsulasi)
        self.__nim = nim
        self.__prodi = prodi

    #enkapsulasi dengan getter dan setter menggunakan decorator
    @property
    def nama(self):
        return self.__nama
    
    @nama.setter
    def nama(self, value):
        if not value:
            raise ValueError("Nama tidak boleh kosong")
        self.__nama = value

    @property
    def nim(self):
        return self.__nim
    
    @nim.setter
    def nim(self, input):
        if len(input) != 9:
            raise ValueError("NIM institut Asia harus 9 digit")
        self.__nim = input

    @property
    def prodi(self):
        return self.__prodi
    
    @prodi.setter
    def prodi(self, input):
        self.__prodi = input

    @abstractmethod
    def info_mahasiswa(self):
        pass

    @abstractmethod
    def hitung_ipk(self):
        pass

    @abstractmethod
    def status_aktif(self):
        pass

    #subclass 1: MahasiswaReguler
class MahasiswaReguler(mahasiswa):
    def __init__(self, nama, nim, prodi, ipk):
        super().__init__(nama, nim, prodi)
        self.__ipk = ipk

    def info_mahasiswa(self):
        return f"Reguler: NIM : {self.nim}, Nama : {self.nama}, Program Studi : {self.prodi}"

    def hitung_ipk(self):
        print(f"IPK sekarang: {self.__ipk}")

    def status_aktif(self):
        return "Aktif"
        
#subclass 2: MahasiswaKaryawan
class MahasiswaKaryawan(mahasiswa):
    def __init__(self, nama, nim, prodi, ipk, jam_kerja):
        super().__init__(nama, nim, prodi)
        self.__ipk = ipk
        self.__jam_kerja = jam_kerja #jam kerja per minggu

    def info_mahasiswa(self):
        return f"Karyawan: NIM : {self.nim}, Nama : {self.nama}, Program Studi : {self.prodi}, Jam Kerja: {self.__jam_kerja}"

    def hitung_ipk(self):
        #misal mahasiswa karyawan biasanya dapat beban kerja berkurang
        faktor = 0.9 if self.__jam_kerja > 20 else 1
        print(f"IPK sekarang: {self.__ipk * faktor}")

    def status_aktif(self):
        return "Aktif"
    
#subclass 3: MahasiswaRPL
class MahasiswaRPL(mahasiswa):
    def __init__(self, nama, nim, prodi, IPKasses, IPKasia):
        super().__init__(nama, nim, prodi)
        self.__IPKasses = IPKasses
        self.__IPKasia = IPKasia
    
    def info_mahasiswa(self):
        return (f"Rekognisi Pembelajaran Lampau : NIM : {self.nim}, Nama : {self.nama},"
                f" Program Studi : {self.prodi}, IPK Assesmen : {self.__IPKasses},"
                f" IPK Asia : {self.__IPKasia}")
    
    def hitung_ipk(self):
        #bisa ada aturan kusus untuk mahasiswa RPL
        self._ipk= (self.__IPKasses + self.__IPKasia) / 2
        print(f"IPK sekarang: {round(self._ipk, 2)}")
    
    def status_aktif(self):
        return "Aktif"
    
# Contoh penggunaan
m1 = MahasiswaReguler("Budi", "123456789", "Teknik Informatika", 3.75)
m2 = MahasiswaKaryawan("Siti", "987654321", "Sistem Informasi", 3.4, 25)
m3 = MahasiswaRPL("Andi", "112233445", "Rekayasa Perangkat Lunak", 3.6, 3.12)

print(m1.info_mahasiswa())
m1.hitung_ipk()
print(m1.status_aktif())


print(m2.info_mahasiswa())
m2.hitung_ipk()
print(m2.status_aktif())

print(m3.info_mahasiswa())
m3.hitung_ipk()
print(m3.status_aktif())
