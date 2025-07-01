class Mhs:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def info(self): 
        return f"Mahasiswa {self.nama} dengan nim {self.nim}"
    
    def tugas(self): 
        return f"{self.nama} sedang mengerjakan tugas kuliah."
    
    def aktivitas(self): 
        return f"{self.nama} sedang mengikuti kegiatan akademik."
    
# Subclass Teknik Informatika, overriding method tugas dan aktifitas
class MahasiswaFTD(Mhs): 
    def __init__(self, nama, nim): 
        super().__init__(nama, nim)

    def tugas(self):
        return f"{self.nama} sedang mengerjakan tugas pemrograman. "

    def aktivitas(self):
        return f"{self.nama} sedang mengikuti praktikum komputer. "
    
# Subclass Mahasiswa Ekonomi, overriding method tugas dan aktivitas
class MahasiswaFEB(Mhs):
    def __init__(self, nama, nim):
        super().__init__(nama, nim)

    def tugas(self):
        return f"{self.nama} sedang mengerjakan tugas makroekonomi. "
    
    def aktivitas(self):
        return f"{self.nama} sedang menghadiri seminar ekonomi. "
    
    # Fungsi untuk menampilkan aktivitas mahasiswa (polimorfisme)
    def tampilkan_aktifitas(mahasiswa):
        print(mahasiswa.info())
        print(mahasiswa.tugas())
        print(mahasiswa.aktivitas())
        print("_"* 40)
    
    # Objek dari berbagai kelas
    m1 = MahasiswaFTD("Budi" ,"242011284")
    m2 = MahasiswaFTD("Sari" ,"242011283")
    m3 = Mhs("Adam" ,"242011287")

    #memanggil fungsi yang sama dengan objek yang berbeda, menunjukan polimorfisme
    tampilkan_aktifitas(m1)
    tampilkan_aktifitas(m2)
    tampilkan_aktifitas(m3)