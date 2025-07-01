import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid  # Import the uuid module for generating unique IDs

# Kelas KaryawanTetap
class KaryawanTetap:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.id = str(uuid.uuid4())  # Generate unique UUID for each employee
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok
        self.absensi = 0
        self.jenis = "Tetap"  # Menambahkan jenis "Tetap" untuk karyawan tetap
        print(f"ID Karyawan Kontrak: {self.id}")  # Print the unique ID for debugging

    def absen(self):
        self.absensi += 1

# Kelas KaryawanKontrak
class KaryawanKontrak:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.id = str(uuid.uuid4())  # Generate unique UUID for each employee
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok
        self.absensi = 0
        self.jenis = "Kontrak"  # Menambahkan jenis "Kontrak" untuk karyawan kontrak
        print(f"ID Karyawan Kontrak: {self.id}")  # Print the unique ID for debugging

    def absen(self):
        self.absensi += 1

# Kelas Departemen yang menangani daftar karyawan
class Departemen:
    def __init__(self, nama):
        self.nama = nama
        self.karyawan_list = []  # Menyimpan daftar karyawan

    def tambah_karyawan(self, karyawan):
        self.karyawan_list.append(karyawan)

# Kelas utama aplikasi manajemen karyawan
class ManajemenKaryawanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Karyawan Perusahaan")
        self.departemen = Departemen("Teknologi")

        # Menambahkan label untuk judul
        self.label = tk.Label(root, text="Manajemen Karyawan", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Frame untuk tampilan utama
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        # Tombol untuk opsi yang ada
        self.tambah_button = tk.Button(self.main_frame, text="Tambah Karyawan", width=20, height=2, command=self.tambah_karyawan_gui)
        self.tambah_button.grid(row=0, column=0, padx=10, pady=10)

        self.absen_button = tk.Button(self.main_frame, text="Absensi Karyawan", width=20, height=2, command=self.absensi_karyawan_gui)
        self.absen_button.grid(row=0, column=1, padx=10, pady=10)

        self.laporan_button = tk.Button(self.main_frame, text="Laporan Bulanan", width=20, height=2, command=self.laporan_bulanan_gui)
        self.laporan_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def tambah_karyawan_gui(self):
        def submit_karyawan():
            jenis_karyawan = jenis_karyawan_var.get().lower()
            nama = nama_var.get()
            id_karyawan = id_var.get()
            try:
                gaji_pokok = float(gaji_var.get())
            except ValueError:
                messagebox.showerror("Input Error", "Gaji harus berupa angka.")
                return

            if jenis_karyawan == "tetap":
                karyawan = KaryawanTetap(nama, id_karyawan, gaji_pokok)
            elif jenis_karyawan == "kontrak":
                karyawan = KaryawanKontrak(nama, id_karyawan, gaji_pokok)
            else:
                messagebox.showerror("Input Error", "Jenis karyawan tidak sesuai.")
                return

            self.departemen.tambah_karyawan(karyawan)
            messagebox.showinfo("Success", f"Karyawan {nama} berhasil ditambahkan!")
            self.laporan_bulanan_gui()  # Refresh the employee table after adding employee
            self.clear_main_frame()  # Clear the form after submission
            self.show_main_buttons()  # Recreate and show main buttons after the form submission

        self.clear_main_frame()

        # Form untuk menambah karyawan
        tk.Label(self.main_frame, text="Jenis Karyawan (Tetap/Kontrak):").grid(row=0, column=0)
        jenis_karyawan_var = tk.StringVar()
        tk.Entry(self.main_frame, textvariable=jenis_karyawan_var).grid(row=0, column=1)

        tk.Label(self.main_frame, text="Nama Karyawan:").grid(row=1, column=0)
        nama_var = tk.StringVar()
        tk.Entry(self.main_frame, textvariable=nama_var).grid(row=1, column=1)

        tk.Label(self.main_frame, text="ID Karyawan:").grid(row=2, column=0)
        id_var = tk.StringVar()
        tk.Entry(self.main_frame, textvariable=id_var).grid(row=2, column=1)

        tk.Label(self.main_frame, text="Gaji Pokok:").grid(row=3, column=0)
        gaji_var = tk.StringVar()
        tk.Entry(self.main_frame, textvariable=gaji_var).grid(row=3, column=1)

        tk.Button(self.main_frame, text="Tambah", command=submit_karyawan).grid(row=4, column=0, columnspan=2, pady=10)

    def absensi_karyawan_gui(self):
        if not self.departemen.karyawan_list:
            messagebox.showerror("Error", "Tidak ada karyawan yang terdaftar untuk absensi.")
            return

        def submit_absensi():
            try:
                karyawan_idx = int(karyawan_var.get().split('.')[0]) - 1
                if 0 <= karyawan_idx < len(self.departemen.karyawan_list):
                    print(f"Catat absensi untuk karyawan: {karyawan_idx}")
                    self.departemen.karyawan_list[karyawan_idx].absen()
                    messagebox.showinfo("Success", f"Absensi untuk {self.departemen.karyawan_list[karyawan_idx].nama} berhasil dicatat!")
                    self.laporan_bulanan_gui()  # Refresh the employee table after attendance
                    self.clear_main_frame()  # Clear the form after submission
                    self.show_main_buttons()  # Recreate and show main buttons after the form submission
                else:
                    messagebox.showerror("Input Error", "Karyawan tidak ditemukan.")
            except ValueError:
                messagebox.showerror("Input Error", "Masukkan nomor karyawan yang valid.")

        self.clear_main_frame()

        # Form untuk absensi karyawan
        tk.Label(self.main_frame, text="Pilih Karyawan untuk Absensi:").grid(row=0, column=0)

        karyawan_list = [f"{idx+1}. {k.nama}" for idx, k in enumerate(self.departemen.karyawan_list)]
        if karyawan_list:
            karyawan_var = tk.StringVar()
            karyawan_menu = tk.OptionMenu(self.main_frame, karyawan_var, *karyawan_list)
            karyawan_menu.grid(row=0, column=1)
            tk.Button(self.main_frame, text="Catat Absensi", command=submit_absensi).grid(row=1, column=0, columnspan=2, pady=10)

    def laporan_bulanan_gui(self):
        self.clear_main_frame()

        # Membuat tabel untuk laporan bulanan
        tree = ttk.Treeview(self.main_frame, columns=("ID", "Nama", "Jenis", "Gaji", "Absensi"), show="headings")
        tree.heading("ID", text="ID Karyawan")
        tree.heading("Nama", text="Nama Karyawan")
        tree.heading("Jenis", text="Jenis Karyawan")
        tree.heading("Gaji", text="Gaji Pokok")
        tree.heading("Absensi", text="Jumlah Absensi")

        for idx, karyawan in enumerate(self.departemen.karyawan_list, 1):
            tree.insert("", "end", values=(idx, karyawan.nama, karyawan.jenis, karyawan.gaji_pokok, karyawan.absensi))

        tree.pack(padx=10, pady=10)

        # Tombol kembali ke menu utama
        tk.Button(self.main_frame, text="Kembali", command=self.go_back_to_main).pack(pady=10)

    def go_back_to_main(self):
        self.clear_main_frame()  # Clear current view
        self.show_main_buttons()  # Recreate and show main buttons again

    def clear_main_frame(self):
        # Menghapus widget di frame utama
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_main_buttons(self):
        # Menampilkan tombol-tombol utama kembali setelah clear
        self.tambah_button = tk.Button(self.main_frame, text="Tambah Karyawan", width=20, height=2, command=self.tambah_karyawan_gui)
        self.tambah_button.grid(row=0, column=0, padx=10, pady=10)

        self.absen_button = tk.Button(self.main_frame, text="Absensi Karyawan", width=20, height=2, command=self.absensi_karyawan_gui)
        self.absen_button.grid(row=0, column=1, padx=10, pady=10)

        self.laporan_button = tk.Button(self.main_frame, text="Laporan Bulanan", width=20, height=2, command=self.laporan_bulanan_gui)
        self.laporan_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Menjalankan aplikasi GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ManajemenKaryawanApp(root)
    root.mainloop()
