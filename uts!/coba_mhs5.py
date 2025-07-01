def cetak_hiasan(func):
    def wrapper(*args, **kwargs):
        print("======= Data Mahasiswa ======")
        func(*args, **kwargs)
        print("=============================")
    return wrapper

class Mahasiswa:
    def __init__(self,nama, nim):
        self.nama = nama
        self.nim = nim

    @cetak_hiasan
    def tampilkan_info(self):
        print(f"Nama : {self.nama}, NIM : {self.nim}")

mhs = Mahasiswa("Budi","34535466")
mhs.tampilkan_info()