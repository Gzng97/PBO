import tkinter as tk
from tkinter import messagebox
import vlc

class IPTVApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python IPTV Player")
        self.master.geometry("500x300")

        self.url_var = tk.StringVar()

        # VLC Instance
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # UI Layout
        tk.Label(master, text="Masukkan URL Streaming (.m3u8):").pack(pady=5)
        self.url_entry = tk.Entry(master, textvariable=self.url_var, width=50)
        self.url_entry.pack(pady=5)

        # Tombol kontrol
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Play", command=self.play_stream).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Pause", command=self.pause_stream).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Stop", command=self.stop_stream).grid(row=0, column=2, padx=5)

        # Preset Channel
        tk.Label(master, text="Channel Preset:").pack(pady=5)
        self.channel_listbox = tk.Listbox(master)
        self.channel_listbox.pack()
        self.channel_listbox.bind("<<ListboxSelect>>", self.select_channel)

        self.channels = {
            "NASA TV": "https://nasatv-lh.akamaihd.net/i/NASA_101@319270/master.m3u8",
            "DW News": "https://dwstream4-lh.akamaihd.net/i/dwstream4_live@124556/index_1_av-p.m3u8",
            "Al Jazeera": "https://live-hls-web-aje.getaj.net/AJE/01.m3u8"
        }

        for name in self.channels:
            self.channel_listbox.insert(tk.END, name)

    def play_stream(self):
        url = self.url_var.get()
        if not url:
            messagebox.showerror("Error", "URL tidak boleh kosong!")
            return
        media = self.instance.media_new(url)
        self.player.set_media(media)
        self.player.play()

    def pause_stream(self):
        self.player.pause()

    def stop_stream(self):
        self.player.stop()

    def select_channel(self, event):
        selected = self.channel_listbox.get(self.channel_listbox.curselection())
        self.url_var.set(self.channels[selected])
        self.play_stream()

if __name__ == "__main__":
    root = tk.Tk()
    app = IPTVApp(root)
    root.mainloop()
