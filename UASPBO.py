from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama, id_karyawan, departemen):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__departemen = departemen
        self.__absensi = 0 
        self.__gaji_pokok = 0
        self.__tunjangan_terakhir = 0
        self.set_gaji_pokok()
    
    # Getter untuk departemen
    def get_departemen(self):
        return self.__departemen
    
    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama):
        self.__nama = nama

    # Getter untuk ID Karyawan
    def get_id_karyawan(self):
        return self.__id_karyawan

    # Setter untuk ID Karyawan
    def set_id_karyawan(self, id_karyawan):
        self.__id_karyawan = id_karyawan

    # Getter untuk gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk gaji pokok (tambahkan parameter)
    def set_gaji_pokok(self, gaji_baru=None):
        if gaji_baru is not None:
            self.__gaji_pokok = gaji_baru
        else:
            dep = self.__departemen.lower()
            if dep == "pemasaran":
                self.__gaji_pokok = 3500000 if isinstance(self, KaryawanTetap) else 2000000
            elif dep == "ti":
                self.__gaji_pokok = 3300000 if isinstance(self, KaryawanTetap) else 2300000
            elif dep == "sdm":
                self.__gaji_pokok = 3400000 if isinstance(self, KaryawanTetap) else 2300000

    # Getter untuk absensi
    def get_absensi(self):
        return self.__absensi

    # Metode untuk mencatat absensi
    def absen(self):
        self.__absensi += 1
        self.check_tunjangan()  # Mengecek tunjangan otomatis

    def check_tunjangan(self):
        # Tunjangan otomatis untuk karyawan tetap: 50.000 setiap 5 absensi
        if isinstance(self, KaryawanTetap):
            tunjangan_baru = (self.__absensi // 5) * 50000
            tambahan = tunjangan_baru - self.__tunjangan_terakhir
            if tambahan > 0:
                self.__gaji_pokok += tambahan
                self.__tunjangan_terakhir = tunjangan_baru


    # Metode abstrak untuk menghitung gaji
    @abstractmethod
    def hitung_gaji(self):
        pass

    # Metode abstrak untuk laporan bulanan
    @abstractmethod
    def laporan_bulanan(self):
        pass


class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, departemen):
        super().__init__(nama, id_karyawan, departemen)

    def hitung_gaji(self):
        # Gaji karyawan tetap = gaji pokok (sudah termasuk tunjangan otomatis)
        return self.get_gaji_pokok()

    def laporan_bulanan(self):
        return f"Laporan Karyawan Tetap: {self.get_nama()}, ID: {self.get_id_karyawan()}, Gaji: {self.hitung_gaji()}, Absensi: {self.get_absensi()}"


class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, departemen):
        super().__init__(nama, id_karyawan, departemen)

    def hitung_gaji(self):
        # Karyawan kontrak hanya mendapatkan gaji pokok tanpa bonus
        return self.get_gaji_pokok()

    def laporan_bulanan(self):
        return f"Laporan Karyawan Kontrak: {self.get_nama()}, ID: {self.get_id_karyawan()}, Gaji: {self.hitung_gaji()}, Absensi: {self.get_absensi()}"


class Manajemen:
    def __init__(self, nama_departemen):
        self.__nama_departemen = nama_departemen
        self.karyawan_list = []

    def tambah_karyawan(self, karyawan):
        self.karyawan_list.append(karyawan)

    def get_nama_departemen(self):
        return self.__nama_departemen
    
    def laporan_manajemen(self):
        laporan = f"Laporan Departemen: {self.__nama_departemen}\n"
        for karyawan in self.karyawan_list:
            laporan += karyawan.laporan_bulanan() + "\n"
        return laporan
    
    def penaikan_gaji(self, karyawan, persen):
        # Fitur penaikan gaji berdasarkan persen untuk karyawan tetap
        if isinstance(karyawan, KaryawanTetap):
            gaji_baru = karyawan.get_gaji_pokok() * (1 + persen / 100)
            karyawan.set_gaji_pokok(gaji_baru)
            print(f"Penaikan gaji {karyawan.get_nama()} berhasil menjadi: {gaji_baru}")
        else:
            print("Penaikan gaji hanya untuk karyawan tetap.")