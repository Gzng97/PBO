import vlc
import time
import os

# Masukkan path lengkap ke folder VLC yang berisi libvlc.dll
vlc_path = r"C:\Program Files (x86)\VideoLAN\VLC\libvlc.dll"  # Ubah sesuai lokasi VLC-mu
os.add_dll_directory(vlc_path)

# Buat instance dengan path tersebut
instance = vlc.Instance()
player = instance.media_player_new()

# URL M3U stream (ganti dengan yang valid)
m3u_url = "bit.ly/41HlTKx"

# Load media dari M3U
media = instance.media_new(m3u_url)
player.set_media(media)

# Mulai putar
print("Memulai streaming...")
player.play()

# Tetap hidup agar streaming berjalan
while True:
    time.sleep(1)
