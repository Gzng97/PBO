from UASPBO import KaryawanTetap, KaryawanKontrak, Manajemen

def tambah_karyawan(manajemen):
    while True:
        print("\nMenambah Karyawan Baru")
        print("Pilih jenis karyawan:")
        print("1. Tetap")
        print("2. Kontrak")
        pilihan_karyawan = input("Masukkan pilihan (1/2): ")
        
        if pilihan_karyawan == "1":
            jenis_karyawan = "tetap"
        elif pilihan_karyawan == "2":
            jenis_karyawan = "kontrak"
        else:
            print("Pilihan tidak valid, silakan ulangi.")
            continue

        # Validasi nama
        while True:
            nama = input("Masukkan nama karyawan: ")
            if not all(c.isalpha() or c.isspace() for c in nama):
                print("Nama tidak valid. Silakan masukkan ulang.")
                continue
            break

        # Validasi ID unik
        while True:
            id_karyawan = input("Masukkan ID karyawan: ")
            if not id_karyawan.isdigit():
                print("ID karyawan harus berupa angka. Silakan masukkan ulang.")
                continue
            id_sama = any(k.get_id_karyawan() == id_karyawan for k in manajemen.karyawan_list)
            if id_sama:
                print("ID sama dengan karyawan lain. Masukkan ulang.")
            else:
                break

        # Ambil nama departemen dari manajemen aktif
        departemen_pilih = manajemen.get_nama_departemen()

        if jenis_karyawan == "tetap":
            karyawan = KaryawanTetap(nama, id_karyawan, departemen_pilih)
        else:
            karyawan = KaryawanKontrak(nama, id_karyawan, departemen_pilih)

        manajemen.tambah_karyawan(karyawan)
        print(f"Karyawan {nama} berhasil ditambahkan ke departemen {departemen_pilih}.\n")
        break

def absensi_karyawan(manajemen):
    print("\nMencatat Absensi Karyawan")
    for idx, karyawan in enumerate(manajemen.karyawan_list):
        if isinstance(karyawan, KaryawanTetap):
            jenis = "Tetap"
        else:
            jenis = "Kontrak"
        print(f"{idx + 1}. {karyawan.get_nama()} - ID: {karyawan.get_id_karyawan()} - Departemen: {karyawan.get_departemen()} - Jenis: {jenis}")
    
    try:
        pilihan = int(input("Pilih karyawan yang ingin melakukan absensi (masukkan nomor): ")) - 1
        if 0 <= pilihan < len(manajemen.karyawan_list):
            manajemen.karyawan_list[pilihan].absen()
            print(f"Absensi untuk {manajemen.karyawan_list[pilihan].get_nama()} berhasil dicatat.\n")
        else:
            print("Pilihan karyawan tidak valid.")
    except ValueError:
        print("Input tidak valid.\n")

def laporan_bulanan(manajemen):
    print("\nLaporan Bulanan Departemen")
    print(manajemen.laporan_manajemen())

def penaikan_gaji(manajemen):
    print("\nPenaikan Gaji Karyawan")
    id_karyawan = input("Masukkan ID Karyawan yang ingin dinaikkan gajinya: ")
    try:
        jumlah = float(input("Masukkan jumlah kenaikan gaji: "))
    except ValueError:
        print("Input jumlah tidak valid.")
        return
    karyawan = next((k for k in manajemen.karyawan_list if k.get_id_karyawan() == id_karyawan), None)
    
    if karyawan:
        gaji_baru = karyawan.get_gaji_pokok() + jumlah
        karyawan.set_gaji_pokok(gaji_baru)
        print(f"Gaji {karyawan.get_nama()} berhasil dinaikkan menjadi: {gaji_baru}")
    else:
        print("Karyawan tidak ditemukan.")

def pecat_karyawan(manajemen):
    print("\nDaftar Karyawan:")
    if not manajemen.karyawan_list:
        print("Belum ada karyawan yang terdaftar.")
        return
    for idx, karyawan in enumerate(manajemen.karyawan_list):
        print(f"{idx + 1}. {karyawan.get_nama()} - ID: {karyawan.get_id_karyawan()} - Departemen: {karyawan.get_departemen()}")
    try:
        pilihan = int(input("Masukkan nomor karyawan yang akan dipecat: ")) - 1
        if 0 <= pilihan < len(manajemen.karyawan_list):
            nama = manajemen.karyawan_list[pilihan].get_nama()
            del manajemen.karyawan_list[pilihan]
            print(f"Karyawan {nama} berhasil dipecat.\n")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input tidak valid.\n")

def main():
    manajemen_pemasaran = Manajemen("Pemasaran")
    manajemen_ti = Manajemen("TI")
    manajemen_sdm = Manajemen("SDM")

    manajemen_dict = {
        "1": manajemen_pemasaran,
        "2": manajemen_ti,
        "3": manajemen_sdm
    }

    while True:
        print("\nPilih Departemen yang akan dikelola:")
        print("1. Pemasaran")
        print("2. TI")
        print("3. SDM")
        print("4. Keluar")
        dep_pilihan = input("Masukkan pilihan (1/2/3/4): ")
        if dep_pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        if dep_pilihan not in manajemen_dict:
            print("Pilihan tidak valid.")
            continue

        manajemen = manajemen_dict[dep_pilihan]

        while True:
            print(f"\nMenu Manajemen Karyawan Departemen {manajemen.get_nama_departemen()}")
            print("1. Tambah Karyawan")
            print("2. Absensi Karyawan")
            print("3. Laporan Bulanan")
            print("4. Penaikan Gaji")
            print("5. Pecat Karyawan")
            print("6. Kembali ke Pilihan Departemen")

            try:
                pilihan = int(input("Pilih menu (1/2/3/4/5/6): "))
                if pilihan == 1:
                    tambah_karyawan(manajemen)
                elif pilihan == 2:
                    absensi_karyawan(manajemen)
                elif pilihan == 3:
                    laporan_bulanan(manajemen)
                elif pilihan == 4:
                    penaikan_gaji(manajemen)
                elif pilihan == 5:
                    pecat_karyawan(manajemen)
                elif pilihan == 6:
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Harap pilih angka yang benar.\n")
                
if __name__ == "__main__":
    main()
