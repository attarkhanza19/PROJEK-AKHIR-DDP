import json
import os
import pwinput
import time
from prettytable import PrettyTable
from datetime import datetime

user_saat_ini = None

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                               FUNGSI BACA & SIMPAN JSON                                                |"
"|                                                                                                                        |"
"+========================================================================================================================+"

# FUNGSI UNTUK DATA PANITIA
def baca_data_panitia():
    file_path = "PA/data_panitia.json"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_data_panitia(data):
    file_path = "PA/data_panitia.json"
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# FUNGSI UNTUK DATA USER
def baca_data_user():
    file_path = "PA/data_user.json"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_data_user(data):
    file_path = "PA/data_user.json"
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# FUNGSI UNTUK DATA KONSER
def baca_data_konser():
    file_path = "PA/data_konser.json"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_data_konser(data):
    file_path = "PA/data_konser.json"
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# FUNGSI UNTUK DATA TIKET
def baca_data_tiket():
    file_path = "PA/data_tiket.json"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_data_tiket(data):
    file_path = "PA/data_tiket.json"
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# FUNGSI UNTUK DATA HISTORI KONSER
def baca_data_histori():
    file_path = "PA/data_histori_konser.json"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_data_histori(data):
    file_path = "PA/data_histori_konser.json"
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                       FUNGSI CLEAR                                                     |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def clear():
    os.system('cls')

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                            FUNGSI REORDER NOMOR KONSER                                                 |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def reorder_nomor_konser(data_konser):
    nomor = 1
    for konser in data_konser:
        konser["nomor_konser"] = nomor
        nomor += 1
    return data_konser

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI LOGIN PANITIA                                                  |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def login_panitia():
    clear()
    data_panitia = baca_data_panitia()
    percobaan_login = 3
    
    while percobaan_login > 0:
        print("\n+-----------------------------------+")
        print("|                                   |")
        print("|           LOGIN PANITIA           |")
        print("|                                   |")
        print("+-----------------------------------+")
        print("|  Tekan enter pada input username  |")
        print("|       jika ingin kembali...       |")
        print("+-----------------------------------+")
        print(f"|       Sisa percobaan: {percobaan_login} kali      |")
        print("+-----------------------------------+\n")

        try:
            username = input("Masukkan username: ").strip().lower()
            if username == "":
                clear()
                return
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue

        try:
            password = pwinput.pwinput(prompt="Masukkan password: ", mask="*").strip()
            if not password:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue

        for p in data_panitia:
            if p["username"].lower() == username.lower() and p["password"] == password:
                clear()
                print(f"\n+-----------------------------------+")
                print(f" Login berhasil!                   ")
                print(f" Selamat datang {username}!        ")
                print(f"+-----------------------------------+\n")
                input("Tekan enter untuk melanjutkan...")
                menu_panitia()
                continue
        
        percobaan_login -= 1
        
        if percobaan_login > 0:
            clear()
            print("\n+-----------------------------------+")
            print(" Username atau password salah!     ")
            print(f" Sisa percobaan: {percobaan_login} kali")
            print("+-----------------------------------+\n")
        else:
            clear()
            print("\n+-------------------------------------------+")
            print("|   Username atau password salah!           |")
            print("|   Percobaan login habis!                  |")
            print("|   Silakan coba lagi dalam 10 detik...     |")
            print("+-------------------------------------------+\n")
            
            try:
                for i in range(10, 0, -1):
                    print(f"\rMenunggu {i} detik...", end="", flush=True)
                    time.sleep(1)
                print("\r" + " "*30 + "\r", end="")
            except KeyboardInterrupt:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh CTRL + C!    |")
                print("+-----------------------------------+\n")
                input("Tekan enter untuk kembali...")
            
            clear()
            return

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                               FUNGSI PILIH REGISTRASI                                                  |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def pilih_registrasi():
    clear()
    while True:
        try:
            print("\n+-----------------------------------------+")
            print("|      Tekan enter pada input pilihan     |")
            print("|          jika ingin kembali...          |")
            print("+-----------------------------------------+\n")
            pilih_regis = input("Apakah anda sudah memiliki akun (ya/tidak)? ").strip().lower()

            if pilih_regis == "":
                clear()
                return
            elif pilih_regis == "ya":
                login_user()
                return
            elif pilih_regis == "tidak":
                registrasi_user()
                return
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Input tidak valid!         |")
                print("+-----------------------------------+\n")

        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|     Input tidak boleh CTRL + C!   |")
            print("+-----------------------------------+\n")

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI LOGIN USER                                                     |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def login_user():
    clear()
    global user_saat_ini
    data_user = baca_data_user()
    percobaan_login = 3
    
    while percobaan_login > 0:
        print("\n+-----------------------------------+")
        print("|                                   |")
        print("|           LOGIN USER              |")
        print("|                                   |")
        print("+-----------------------------------+")
        print("|  Tekan enter pada input username  |")
        print("|       jika ingin kembali...       |")
        print("+-----------------------------------+")
        print(f"|       Sisa percobaan: {percobaan_login} kali      |")
        print("+-----------------------------------+\n")

        try:
            username = input("Masukkan username: ").strip().lower()
            if username == "":
                clear()
                return
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue

        try:
            password = pwinput.pwinput(prompt="Masukkan password: ", mask="*").strip()
            if not password:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue

        user_ditemukan = None
        for user in data_user:
            if user["Nama"].lower() == username.lower() and user["Password"] == password:
                user_ditemukan = user
                break

        if user_ditemukan:
            user_saat_ini = user_ditemukan
            clear()
            print("\n+-----------------------------------+")
            print(f" Selamat datang, {username}!       ")
            print("+-----------------------------------+\n")
            input("Tekan enter untuk melanjutkan...")
            menu_user()
            return
        
        percobaan_login -= 1
        
        if percobaan_login > 0:
            clear()
            print("\n+-----------------------------------+")
            print("|  Username atau password salah!    |")
            print(f"|  Sisa percobaan: {percobaan_login} kali           |")
            print("+-----------------------------------+\n")
        else:
            clear()
            print("\n+-------------------------------------------+")
            print("|   Username atau password salah!           |")
            print("|   Percobaan login habis!                  |")
            print("|   Silakan coba lagi dalam 10 detik...     |")
            print("+-------------------------------------------+\n")
            
            try:
                for i in range(10, 0, -1):
                    print(f"\rMenunggu {i} detik...", end="", flush=True)
                    time.sleep(1)
                print("\r" + " "*30 + "\r", end="")
            except KeyboardInterrupt:
                clear()
                print("\n+-----------------------------------+")
                print("|  Input tidak boleh CTRL + C!      |")
                print("+-----------------------------------+\n")
                input("Tekan enter untuk kembali...")
            
            clear()
            return

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                FUNGSI REGISTRASI AKUN                                                  |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def registrasi_user():
    clear()
    global user_saat_ini
    data_user = baca_data_user()
    
    while True:
        try:
            print("\n+-----------------------------------+")
            print("|                                   |")
            print("|              BUAT AKUN            |")
            print("|                                   |")
            print("+-----------------------------------+")
            print("|  Tekan enter pada input username  |")
            print("|       jika ingin kembali...       |")
            print("+-----------------------------------+\n")
            username = input("Masukkan username (3-10 karakter): ").strip()
            
            if username == "":
                clear()
                return
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue

        # Validasi panjang username
        if len(username) < 3:
            clear()
            print("\n+-----------------------------------+")
            print("|   Username minimal 3 karakter!    |")
            print("+-----------------------------------+\n")
            continue
        elif len(username) > 10:
            clear()
            print("\n+-----------------------------------+")
            print("|   Username maksimal 10 karakter!  |")
            print("+-----------------------------------+\n")
            continue

        user_ada = False
        for u in data_user:
            if u["Nama"].lower() == username.lower():
                user_ada = True
                break
        
        if user_ada:
            print("\n+-----------------------------------+")
            print("|    Username sudah terpakai!       |")
            print("+-----------------------------------+\n")
            pilih = input(f"Ingin login ke {username} (ya/tidak)? ").strip().lower()
            if pilih == "ya":
                login_user()
                return
            elif pilih == "tidak":
                clear()
                print("\n+-----------------------------------+")
                print("|    Silahkan pilih username lain   |")
                print("+-----------------------------------+\n")
                continue
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Input tidak valid!         |")
                print("+-----------------------------------+\n")
                continue

        try:
            pw_user = pwinput.pwinput(prompt="Masukkan Password (3-10 karakter): ", mask="*").strip()
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue
        
        # Validasi password
        if len(pw_user) < 3:
            clear()
            print("\n+-----------------------------------+")
            print("|   Password minimal 3 karakter!    |")
            print("+-----------------------------------+\n")
            continue
        elif len(pw_user) > 10:
            clear()
            print("\n+-----------------------------------+")
            print("|   Password maksimal 10 karakter!  |")
            print("+-----------------------------------+\n")
            continue
        
        # Buat user baru dan simpan
        user_baru = {
            "Nama": username,
            "Password": pw_user,
            "Saldo": 0
        }
        data_user.append(user_baru)
        simpan_data_user(data_user)
        
        user_saat_ini = user_baru
        
        clear()
        print("\n+-----------------------------------+")
        print(f" Hai {username}!                      ")
        print(" Akun berhasil diregistrasi!           ")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk melanjutkan...")
        menu_user()

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                               FUNGSI MENU MANAJEMEN PANITIA                                            |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def menu_panitia():
    clear()
    while True:
        try:
            print("\n+-----------------------------------+")
            print("|                                   |")
            print("|            MENU PANITIA           |")
            print("|                                   |")
            print("+-----------------------------------+")
            print("|                                   |")
            print("|     1. Manajemen Konser           |")
            print("|     2. Manajemen Tiket            |")
            print("|     3. Lihat Histori Konser       |")
            print("|     4. Kembali ke Menu Awal       |")
            print("|                                   |")
            print("+-----------------------------------+\n")
            pilih = input("Pilih menu 1/2/3/4: ").strip()
            
            if not pilih:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue
                
            if pilih == "1":
                manajemen_konser()
            elif pilih == "2":
                manajemen_tiket()
            elif pilih == "3":
                lihat_histori_konser()
            elif pilih == "4":
                clear()
                return menu_utama()
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Pilihan tidak valid!       |")
                print("+-----------------------------------+\n")
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                               FUNGSI MENU MANAJEMEN KONSER                                             |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def manajemen_konser():
    clear()
    while True:
        try:
            print("\n+-----------------------------------+")
            print("|                                   |")
            print("|          MANAJEMEN KONSER         |")
            print("|                                   |")
            print("+-----------------------------------+")
            print("|                                   |")
            print("|     1. Tambah Konser              |")
            print("|     2. Lihat Konser               |")
            print("|     3. Ubah Tanggal & Waktu       |")
            print("|     4. Hapus Konser               |")
            print("|     5. Kembali ke Menu Panitia    |")
            print("|                                   |")
            print("+-----------------------------------+\n")
            pilih = input("Pilih menu 1/2/3/4/5: ").strip()

            if not pilih:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue

            if pilih == "1":
                tambah_konser()
            elif pilih == "2":
                lihat_konser()
            elif pilih == "3":
                ubah_tanggal_waktu_konser()
            elif pilih == "4":
                hapus_konser()
            elif pilih == "5":
                clear()
                return menu_panitia()
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Pilihan tidak valid!       |")
                print("+-----------------------------------+\n")
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                          FUNGSI UBAH TANGGAL & WAKTU KONSER                                            |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def ubah_tanggal_waktu_konser():
    clear()
    data_konser = baca_data_konser()
    
    while True:
        if not data_konser:
            print("\n+-----------------------------------+")
            print("|    Belum ada konser terdaftar!    |")
            print("+-----------------------------------+\n")
            input("Tekan enter untuk kembali...")
            clear()
            return
        
        print("============================================================================================================================")
        print("                                                    KONSER SUATIS FEST                                                      ")
        print("============================================================================================================================")

        table = PrettyTable()
        table.field_names = [
            "No", "Nama Konser", "Tanggal", "Waktu Konser",
            "VVIP", "VIP", "Festival",
            "Stok VVIP", "Stok VIP", "Stok Festival"
        ]

        for konser in data_konser:
            waktu_mulai = konser["Waktu_konser"]["Waktu_mulai"]
            waktu_selesai = konser["Waktu_konser"]["Waktu_selesai"]
            waktu_konser = f"{waktu_mulai} - {waktu_selesai}"
            
            table.add_row([
                konser["nomor_konser"],
                konser["nama_konser"],
                konser.get("Tanggal", "-"),
                waktu_konser,
                f"Rp{konser['Harga']['VVIP']:,}",
                f"Rp{konser['Harga']['VIP']:,}",
                f"Rp{konser['Harga']['Festival']:,}",
                konser["Stok"]["VVIP"],
                konser["Stok"]["VIP"],
                konser["Stok"]["Festival"]
            ])

        print(table)
        
        print("\n+-----------------------------------+")
        print("|   Tekan enter pada input nomor    |")
        print("|   konser jika ingin kembali...    |")
        print("+-----------------------------------+\n")
        
        try:
            nomor_input = input("Masukkan nomor konser yang ingin diubah: ").strip()

            if nomor_input == "":
                clear()
                return
            else:
                nomor_konser = int(nomor_input)
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|          Input tidak valid        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue
        
        konser_dipilih = None
        for k in data_konser:
            if k["nomor_konser"] == nomor_konser:
                konser_dipilih = k
                break
        
        if konser_dipilih is None:
            clear()
            print("\n+-----------------------------------+")
            print("|      Konser tidak ditemukan!      |")
            print("+-----------------------------------+\n")
            continue
        
        waktu_str = f"{konser_dipilih['Waktu_konser']['Waktu_mulai']} - {konser_dipilih['Waktu_konser']['Waktu_selesai']}"
        
        print("\n+-----------------------------------+")
        print(f" Konser: {konser_dipilih['nama_konser']}")
        print(f" Tanggal: {konser_dipilih.get('Tanggal', '-')}")
        print(f" Waktu: {waktu_str}")
        print("+-----------------------------------+")
        print("|  Format: DD-MM-YYYY (25-12-2025)  |")
        print("+-----------------------------------+")
        print("|   Tekan enter jika tidak ingiin   |")
        print("|           merubah data..          |")
        print("+-----------------------------------+\n")
        
        try:
            tanggal_baru = input("Tanggal baru: ").strip()
            # Jika kosong, gunakan tanggal lama
            if not tanggal_baru:
                tanggal_baru = konser_dipilih.get('Tanggal', '-')
            else:
                # Validasi format tanggal jika ada input
                try:
                    datetime.strptime(tanggal_baru, "%d-%m-%Y")
                except ValueError:
                    clear()
                    print("\n+-----------------------------------+")
                    print("|  Format tanggal tidak valid!      |")
                    print("|  Gunakan format: DD-MM-YYYY       |")
                    print("+-----------------------------------+\n")
                    continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue
        
        print("\n+-----------------------------------+")
        print("|       Format: HH:MM (19:00)       |")
        print("+-----------------------------------+")
        print("|   Tekan enter jika tidak ingiin   |")
        print("|           merubah data..          |")
        print("+-----------------------------------+\n")
        
        try:
            waktu_mulai_baru = input("Waktu mulai baru: ").strip()
            # Jika kosong, gunakan waktu lama
            if not waktu_mulai_baru:
                waktu_mulai_baru = konser_dipilih['Waktu_konser']['Waktu_mulai']
            else:
                # Validasi format waktu jika ada input
                try:
                    datetime.strptime(waktu_mulai_baru, "%H:%M")
                except ValueError:
                    clear()
                    print("\n+-----------------------------------+")
                    print("|    Format waktu tidak valid!      |")
                    print("|    Gunakan format: HH:MM          |")
                    print("+-----------------------------------+\n")
                    continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue

        try:
            waktu_selesai_baru = input("Waktu selesai baru: ").strip()
            # Jika kosong, gunakan waktu lama
            if not waktu_selesai_baru:
                waktu_selesai_baru = konser_dipilih['Waktu_konser']['Waktu_selesai']
            else:
                # Validasi format waktu jika ada input
                try:
                    datetime.strptime(waktu_selesai_baru, "%H:%M")
                except ValueError:
                    clear()
                    print("\n+-----------------------------------+")
                    print("|    Format waktu tidak valid!      |")
                    print("|    Gunakan format: HH:MM          |")
                    print("+-----------------------------------+\n")
                    continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue
        
        # Update tanggal dan waktu
        konser_dipilih['Tanggal'] = tanggal_baru
        konser_dipilih['Waktu_konser']['Waktu_mulai'] = waktu_mulai_baru
        konser_dipilih['Waktu_konser']['Waktu_selesai'] = waktu_selesai_baru
        
        # Simpan perubahan
        simpan_data_konser(data_konser)
        
        clear()
        print("\n+-----------------------------------+")
        print(" Tanggal & waktu berhasil diubah! ")
        print(f" Tanggal: {tanggal_baru}")
        print(f" Waktu: {waktu_mulai_baru} - {waktu_selesai_baru}")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return
    
"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                               FUNGSI MENU MANAJEMEN TIKET                                              |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def manajemen_tiket():
    clear()
    while True:
        try:
            print("\n+-----------------------------------+")
            print("|                                   |")
            print("|          MANAJEMEN TIKET          |")
            print("|                                   |")
            print("+-----------------------------------+")
            print("|                                   |")
            print("|     1. Ubah Harga Tiket           |")
            print("|     2. Lihat Semua Tiket Terjual  |")
            print("|     3. Kembali ke Menu Panitia    |")
            print("|                                   |")
            print("+-----------------------------------+\n")
            pilih = input("Pilih menu 1/2/3: ").strip()

            if not pilih:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue

            if pilih == "1":
                ubah_harga_tiket()
            elif pilih == "2":
                lihat_semua_tiket()
            elif pilih == "3":
                clear()
                return menu_panitia()
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Pilihan tidak valid!       |")
                print("+-----------------------------------+\n")
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI TAMBAH KONSER                                                  |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def tambah_konser():
    clear()
    data = baca_data_konser()
    
    while True:
        print("\n+-----------------------------------+")
        print("|          TAMBAH KONSER            |")
        print("+-----------------------------------+")
        print("|    Tekan enter pada input nama    |")
        print("|    konser jika ingin kembali...   |")
        print("+-----------------------------------+\n")

        try:
            nama = input("Nama konser: ").strip()
            if nama == "":
                clear()
                return
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue
        
        # Input tanggal
        try:
            print("\n+-----------------------------------+")
            print("| Format tanggal: DD-MM-YYYY        |")
            print("| Contoh: 25-12-2025                |")
            print("+-----------------------------------+\n")
            tanggal = input("Tanggal konser: ").strip()
            if not tanggal:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue
        
        # Validasi format tanggal
        try:
            datetime.strptime(tanggal, "%d-%m-%Y")
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Format tanggal tidak valid!      |")
            print("|  Gunakan format: DD-MM-YYYY       |")
            print("+-----------------------------------+\n")
            continue
        
        # Input waktu mulai
        try:
            print("\n+-----------------------------------+")
            print("| Format waktu: HH:MM               |")
            print("| Contoh: 19:00                     |")
            print("+-----------------------------------+\n")
            waktu_mulai = input("Waktu mulai: ").strip()
            if not waktu_mulai:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue

        # Validasi format waktu mulai
        try:
            datetime.strptime(waktu_mulai, "%H:%M")
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|    Format waktu tidak valid!      |")
            print("|    Gunakan format: HH:MM          |")
            print("+-----------------------------------+\n")
            continue

        # Input waktu selesai
        try:
            waktu_selesai = input("Waktu selesai: ").strip()
            if not waktu_selesai:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue

        # Validasi format waktu selesai
        try:
            datetime.strptime(waktu_selesai, "%H:%M")
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|    Format waktu tidak valid!      |")
            print("|    Gunakan format: HH:MM          |")
            print("+-----------------------------------+\n")
            continue

        # Input harga VVIP
        try:
            print("\n+-----------------------------------+")
            print("| Harga minimal: Rp100.000          |")
            print("| Harga maksimal: Rp10.000.000      |")
            print("+-----------------------------------+\n")
            harga_vvip = int(input("Harga VVIP: "))
            if harga_vvip < 100000 or harga_vvip > 10000000:
                clear()
                print("\n+-----------------------------------+")
                print("|  Harga minimal Rp100.000!         |")
                print("|  Harga maksimal Rp10.000.000!     |")
                print("+-----------------------------------+\n")
                continue
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input harus berupa angka!        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue
        
        # Input harga VIP
        try:
            print("\n+-----------------------------------+")
            print("| Harga minimal: Rp70.000           |")
            print("| Harga maksimal: Rp9.000.000       |")
            print("+-----------------------------------+\n")
            harga_vip = int(input("Harga VIP: "))
            if harga_vip < 70000 or harga_vip > 9000000:
                clear()
                print("\n+-----------------------------------+")
                print("|  Harga minimal Rp70.000!          |")
                print("|  Harga maksimal Rp9.000.000!      |")
                print("+-----------------------------------+\n")
                continue
            if harga_vip > harga_vvip:
                clear()
                print("\n+-----------------------------------+")
                print("|  Harga VIP tidak boleh lebih      |")
                print("|  tinggi dari harga VVIP!          |")
                print("+-----------------------------------+\n")
                continue
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input harus berupa angka!        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue
                
        # Input harga Festival
        try:
            print("\n+-----------------------------------+")
            print("| Harga minimal: Rp50.000           |")
            print("| Harga maksimal: Rp8.000.000       |")
            print("+-----------------------------------+\n")
            harga_festival = int(input("Harga Festival: "))
            if harga_festival < 50000 or harga_festival > 8000000:
                clear()
                print("\n+-----------------------------------+")
                print("|  Harga minimal Rp50.000!          |")
                print("|  Harga maksimal Rp8.000.000!      |")
                print("+-----------------------------------+\n")
                continue
            if harga_festival > harga_vip:
                clear()
                print("\n+-----------------------------------+")
                print("|  Harga Festival tidak boleh       |")
                print("|  lebih tinggi dari harga VIP!     |")
                print("+-----------------------------------+\n")
                continue
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input harus berupa angka!        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue

        # Input stok tiket
        print("\n+-----------------------------------+")
        print("|         INPUT STOK TIKET          |")
        print("+-----------------------------------+\n")
        
        try:
            stok_vvip = int(input("Stok VVIP: "))
            if stok_vvip < 0:
                clear()
                print("\n+-----------------------------------+")
                print("|  Stok tidak boleh negatif!        |")
                print("+-----------------------------------+\n")
                continue
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input harus berupa angka!        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue

        try:
            stok_vip = int(input("Stok VIP: "))
            if stok_vip < 0:
                clear()
                print("\n+-----------------------------------+")
                print("|  Stok tidak boleh negatif!        |")
                print("+-----------------------------------+\n")
                continue
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input harus berupa angka!        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue

        try:
            stok_festival = int(input("Stok Festival: "))
            if stok_festival < 0:
                clear()
                print("\n+-----------------------------------+")
                print("|  Stok tidak boleh negatif!        |")
                print("+-----------------------------------+\n")
                continue
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input harus berupa angka!        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue

        # Tentukan nomor konser baru
        if len(data) == 0:
            nomor_baru = 1
        else:
            nomor_terbesar = max([k["nomor_konser"] for k in data])
            nomor_baru = nomor_terbesar + 1

        konser_baru = {
            "nomor_konser": nomor_baru,
            "nama_konser": nama,
            "Tanggal": tanggal,
            "Waktu_konser": {"Waktu_mulai": waktu_mulai, "Waktu_selesai": waktu_selesai},
            "Kategori": ["VVIP", "VIP", "Festival"],
            "Harga": {"VVIP": harga_vvip, "VIP": harga_vip, "Festival": harga_festival},
            "Stok": {"VVIP": stok_vvip, "VIP": stok_vip, "Festival": stok_festival}
        }

        data.append(konser_baru)
        simpan_data_konser(data)

        clear()
        print("\n+-----------------------------------+")
        print(f" Konser '{nama}' berhasil ditambahkan! ")
        print(f" Tanggal: {tanggal}")
        print(f" Waktu: {waktu_mulai} - {waktu_selesai}")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI LIHAT KONSER                                                   |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def lihat_konser():
    clear()
    data_konser = baca_data_konser()
    
    if not data_konser:
        print("\n+-----------------------------------+")
        print("|    Belum ada konser terdaftar!    |")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return

    print("============================================================================================================================")
    print("                                                    KONSER SUATIS FEST                                                      ")
    print("============================================================================================================================")

    table = PrettyTable()
    table.field_names = [
        "No", "Nama Konser", "Tanggal", "Waktu Konser",
        "VVIP", "VIP", "Festival",
        "Stok VVIP", "Stok VIP", "Stok Festival"
    ]

    for konser in data_konser:
        waktu_mulai = konser["Waktu_konser"]["Waktu_mulai"]
        waktu_selesai = konser["Waktu_konser"]["Waktu_selesai"]
        waktu_konser = f"{waktu_mulai} - {waktu_selesai}"
        
        table.add_row([
            konser["nomor_konser"],
            konser["nama_konser"],
            konser.get("Tanggal", "-"),
            waktu_konser,
            f"Rp{konser['Harga']['VVIP']:,}",
            f"Rp{konser['Harga']['VIP']:,}",
            f"Rp{konser['Harga']['Festival']:,}",
            konser["Stok"]["VVIP"],
            konser["Stok"]["VIP"],
            konser["Stok"]["Festival"]
        ])

    print(table)
    print()
    input("Tekan enter untuk kembali...")
    clear()

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI LIHAT KONSER USER                                              |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def lihat_konser_user():
    clear()
    data_konser = baca_data_konser()
    
    if not data_konser:
        print("\n+-----------------------------------+")
        print("|    Belum ada konser terdaftar!    |")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return

    print("============================================================================================================================")
    print("                                                    KONSER SUATIS FEST                                                      ")
    print("============================================================================================================================")

    table = PrettyTable()
    table.field_names = [
        "No", "Nama Konser", "Tanggal", "Waktu Konser",
        "VVIP", "VIP", "Festival",
        "Stok VVIP", "Stok VIP", "Stok Festival"
    ]

    for konser in data_konser:
        waktu_mulai = konser["Waktu_konser"]["Waktu_mulai"]
        waktu_selesai = konser["Waktu_konser"]["Waktu_selesai"]
        waktu_konser = f"{waktu_mulai} - {waktu_selesai}"
        
        table.add_row([
            konser["nomor_konser"],
            konser["nama_konser"],
            konser.get("Tanggal", "-"),
            waktu_konser,
            f"Rp{konser['Harga']['VVIP']:,}",
            f"Rp{konser['Harga']['VIP']:,}",
            f"Rp{konser['Harga']['Festival']:,}",
            konser["Stok"]["VVIP"],
            konser["Stok"]["VIP"],
            konser["Stok"]["Festival"]
        ])

    print(table)
    print()
    input("Tekan enter untuk kembali...")
    clear()

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                      HAPUS KONSER                                                      |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def hapus_konser():
    clear()
    data_konser = baca_data_konser()
    data_histori = baca_data_histori()
    
    while True:
        if not data_konser:
            clear()
            print("\n+-----------------------------------+")
            print("|   Belum ada konser terdaftar!     |")
            print("+-----------------------------------+\n")
            input("Tekan enter untuk kembali...")
            clear()
            return

        print("============================================================================================================================")
        print("                                                    KONSER SUATIS FEST                                                      ")
        print("============================================================================================================================")

        table = PrettyTable()
        table.field_names = [
            "No", "Nama Konser", "Tanggal", "Waktu Konser",
            "VVIP", "VIP", "Festival",
            "Stok VVIP", "Stok VIP", "Stok Festival"
        ]

        for konser in data_konser:
            waktu_mulai = konser["Waktu_konser"]["Waktu_mulai"]
            waktu_selesai = konser["Waktu_konser"]["Waktu_selesai"]
            waktu_konser = f"{waktu_mulai} - {waktu_selesai}"
            
            table.add_row([
                konser["nomor_konser"],
                konser["nama_konser"],
                konser.get("Tanggal", "-"),
                waktu_konser,
                f"Rp{konser['Harga']['VVIP']:,}",
                f"Rp{konser['Harga']['VIP']:,}",
                f"Rp{konser['Harga']['Festival']:,}",
                konser["Stok"]["VVIP"],
                konser["Stok"]["VIP"],
                konser["Stok"]["Festival"]
            ])

        print(table)

        print("\n+-----------------------------------+")
        print("|   Tekan enter pada input nomor    |")
        print("|   konser jika ingin kembali...    |")
        print("+-----------------------------------+\n")

        try:
            nomor_input = input("Masukkan nomor konser yang ingin dihapus: ").strip()
            if nomor_input == "":
                clear()
                return
            
            nomor_konser = int(nomor_input)
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|          Input tidak valid        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue
        
        konser_dipilih = None
        for k in data_konser:
            if k["nomor_konser"] == nomor_konser:
                konser_dipilih = k
                break
        
        if konser_dipilih is None:
            clear()
            print("\n+-----------------------------------+")
            print("|      Konser tidak ditemukan!      |")
            print("+-----------------------------------+\n")
            continue

        # Simpan ke histori
        konser_dihapus = konser_dipilih.copy()
        konser_dihapus['waktu_dihapus'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        data_histori.append(konser_dihapus)

        # Hapus konser dari data
        data_konser.remove(konser_dipilih)
        
        # Reorder nomor konser
        data = reorder_nomor_konser(data_konser)

        simpan_data_konser(data)
        simpan_data_histori(data_histori)
        
        clear()
        print("\n+-----------------------------------+")
        print(f" Konser '{konser_dihapus['nama_konser']}' berhasil dihapus! ")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                FUNGSI LIHAT HISTORI KONSER                                             |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def lihat_histori_konser():
    clear()
    data_histori = baca_data_histori()
    
    if not data_histori:
        print("\n+-----------------------------------+")
        print("|    Belum ada histori konser       |")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return
    
    print("===============================================================================================================================================")
    print( "                                                            HISTORI KONSER                                                                    ")
    print("===============================================================================================================================================")

    
    table = PrettyTable()
    table.field_names = [
        "Nama Konser", "Tanggal", "Waktu",
        "VVIP", "VIP", "Festival",
        "Stok VVIP", "Stok VIP", "Stok Festival",
        "Waktu Dihapus"
    ]
    
    for konser in data_histori:
        waktu_mulai = konser["Waktu_konser"]["Waktu_mulai"]
        waktu_selesai = konser["Waktu_konser"]["Waktu_selesai"]
        waktu_str = f"{waktu_mulai} - {waktu_selesai}"
        
        table.add_row([
            konser["nama_konser"],
            konser.get("Tanggal", "-"),
            waktu_str,
            f"Rp{konser['Harga']['VVIP']:,}",
            f"Rp{konser['Harga']['VIP']:,}",
            f"Rp{konser['Harga']['Festival']:,}",
            konser["Stok"]["VVIP"],
            konser["Stok"]["VIP"],
            konser["Stok"]["Festival"],
            konser.get("waktu_dihapus", "-")
        ])
    
    print(table)
    print("===============================================================================================================================================")
    print(f"Total Konser dalam Histori: {len(data_histori)}")
    print("===============================================================================================================================================")
    print()
    input("Tekan enter untuk kembali...")
    clear()


"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI UBAH HARGA TIKET                                               |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def ubah_harga_tiket():
    clear()
    data_konser = baca_data_konser()
    
    while True:
        if not data_konser:
            print("\n+-----------------------------------+")
            print("|    Belum ada konser terdaftar!    |")
            print("+-----------------------------------+\n")
            input("Tekan enter untuk kembali...")
            clear()
            return
        
        print("============================================================================================================================")
        print("                                                    KONSER SUATIS FEST                                                      ")
        print("============================================================================================================================")

        table = PrettyTable()
        table.field_names = [
            "No", "Nama Konser", "Tanggal", "Waktu Konser",
            "VVIP", "VIP", "Festival",
            "Stok VVIP", "Stok VIP", "Stok Festival"
        ]

        for konser in data_konser:
            waktu_mulai = konser["Waktu_konser"]["Waktu_mulai"]
            waktu_selesai = konser["Waktu_konser"]["Waktu_selesai"]
            waktu_konser = f"{waktu_mulai} - {waktu_selesai}"
            
            table.add_row([
                konser["nomor_konser"],
                konser["nama_konser"],
                konser.get("Tanggal", "-"),
                waktu_konser,
                f"Rp{konser['Harga']['VVIP']:,}",
                f"Rp{konser['Harga']['VIP']:,}",
                f"Rp{konser['Harga']['Festival']:,}",
                konser["Stok"]["VVIP"],
                konser["Stok"]["VIP"],
                konser["Stok"]["Festival"]
            ])

        print(table)
        print()
        
        print("+-----------------------------------+")
        print("|   Tekan enter pada input nomor    |")
        print("|   konser jika ingin kembali...    |")
        print("+-----------------------------------+\n")
        
        try:
            nomor_input = input("Masukkan nomor konser yang ingin diubah harganya: ").strip()
            if nomor_input == "":
                clear()
                return
            
            nomor_konser = int(nomor_input)
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|   Input harus berupa angka!       |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            continue
        
        konser_dipilih = None
        for k in data_konser:
            if k["nomor_konser"] == nomor_konser:
                konser_dipilih = k
                break
        
        if konser_dipilih is None:
            clear()
            print("\n+-----------------------------------+")
            print("|      Konser tidak ditemukan!      |")
            print("+-----------------------------------+\n")
            continue
        
        print(f"\n+-----------------------------------+")
        print(f" UBAH HARGA: {konser_dipilih['nama_konser']}")
        print("+-----------------------------------+")
        print(" Harga saat ini:")
        print(f" VVIP: Rp{konser_dipilih['Harga']['VVIP']:,}")
        print(f" VIP: Rp{konser_dipilih['Harga']['VIP']:,}")
        print(f" Festival: Rp{konser_dipilih['Harga']['Festival']:,}")
        print("+-----------------------------------+\n")
        
        try:
            print("+-----------------------------------+")
            print("| Harga minimal: Rp100.000          |")
            print("| Harga maksimal: Rp10.000.000      |")
            print("| Tekan enter untuk skip/lewati     |")
            print("+-----------------------------------+\n")
            harga_vvip_input = input("Harga VVIP baru: ").strip()
            if not harga_vvip_input:
                harga_vvip = konser_dipilih['Harga']['VVIP']
            else:
                harga_vvip = int(harga_vvip_input)
                if harga_vvip < 100000 or harga_vvip > 10000000:
                    clear()
                    print("\n+-----------------------------------+")
                    print("|  Harga minimal Rp100.000!         |")
                    print("|  Harga maksimal Rp10.000.000!     |")
                    print("+-----------------------------------+\n")
                    continue
                
            print("\n+-----------------------------------+")
            print("| Harga minimal: Rp70.000           |")
            print("| Harga maksimal: Rp9.000.000       |")
            print("| Tekan enter untuk skip/lewati     |")
            print("+-----------------------------------+\n")
            harga_vip_input = input("Harga VIP baru: ").strip()
            if not harga_vip_input:
                harga_vip = konser_dipilih['Harga']['VIP']
            else:
                harga_vip = int(harga_vip_input)
                if harga_vip < 70000 or harga_vip > 9000000:
                    clear()
                    print("\n+-----------------------------------+")
                    print("|  Harga minimal Rp70.000!          |")
                    print("|  Harga maksimal Rp9.000.000!      |")
                    print("+-----------------------------------+\n")
                    continue
            
            if harga_vip > harga_vvip:
                clear()
                print("\n+-----------------------------------+")
                print("|  Harga VIP tidak boleh lebih      |")
                print("|  tinggi dari harga VVIP!          |")
                print("+-----------------------------------+\n")
                continue
                
            print("\n+-----------------------------------+")
            print("| Harga minimal: Rp50.000           |")
            print("| Harga maksimal: Rp8.000.000       |")
            print("| Tekan enter untuk skip/lewati     |")
            print("+-----------------------------------+\n")
            harga_festival_input = input("Harga Festival baru: ").strip()
            if not harga_festival_input:
                harga_festival = konser_dipilih['Harga']['Festival']
            else:
                harga_festival = int(harga_festival_input)
                if harga_festival < 50000 or harga_festival > 8000000:
                    clear()
                    print("\n+-----------------------------------+")
                    print("|  Harga minimal Rp50.000!          |")
                    print("|  Harga maksimal Rp8.000.000!      |")
                    print("+-----------------------------------+\n")
                    continue
            
            if harga_festival > harga_vip:
                clear()
                print("\n+-----------------------------------+")
                print("|  Harga Festival tidak boleh       |")
                print("|  lebih tinggi dari harga VIP!     |")
                print("+-----------------------------------+\n")
                continue
                
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input harus berupa angka!      |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            continue
        
        konser_dipilih['Harga']['VVIP'] = harga_vvip
        konser_dipilih['Harga']['VIP'] = harga_vip
        konser_dipilih['Harga']['Festival'] = harga_festival
        
        simpan_data_konser(data_konser)
        
        clear()
        print("\n+-----------------------------------+")
        print("|   Harga tiket berhasil diubah!    |")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return
    
"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                              FUNGSI LIHAT SEMUA TIKET TERJUAL                                          |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def lihat_semua_tiket():
    clear()
    data_tiket = baca_data_tiket()
    
    if not data_tiket:
        print("\n+-----------------------------------+")
        print("|   Belum ada tiket yang terjual!   |")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return
    
    print("===============================================================================================================")
    print("                                              SEMUA TIKET TERJUAL                                              ")
    print("===============================================================================================================")
    
    table = PrettyTable()
    table.field_names = [
        "Username", "Nama Konser", "Tanggal", "Waktu",
        "Kategori", "Jumlah", "Total Harga", "Waktu Pembelian"
    ]
    
    total_pendapatan = 0
    
    for tiket in data_tiket:
        waktu_mulai = tiket["waktu_konser"]["Waktu_mulai"]
        waktu_selesai = tiket["waktu_konser"]["Waktu_selesai"]
        waktu_str = f"{waktu_mulai} - {waktu_selesai}"
        
        table.add_row([
            tiket.get("username", "-"),
            tiket.get("nama_konser", "-"),
            tiket.get("tanggal_konser", "-"),
            waktu_str,
            tiket.get("kategori", "-"),
            tiket.get("jumlah", "-"),
            f"Rp{tiket.get('total_harga', 0):,}",
            tiket.get("waktu_pembelian", "-")
        ])
        total_pendapatan += tiket.get('total_harga', 0)
    
    print(table)
    print("===============================================================================================================")
    print(f" Total Tiket Terjual: {len(data_tiket)} tiket")
    print(f" Total Pendapatan   : Rp{total_pendapatan:,}")
    print("===============================================================================================================\n")
    input("Tekan enter untuk kembali...")
    clear()

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI MENU USER                                                      |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def menu_user():
    clear()
    while True:
        try:
            print("\n+-----------------------------------+")
            print("|                                   |")
            print("|             MENU USER             |")
            print("|                                   |")
            print("+-----------------------------------+")
            print("|                                   |")
            print("|     1. Lihat Konser               |")
            print("|     2. Beli Tiket                 |")
            print("|     3. Lihat Tiket Saya           |")
            print("|     4. Top Up Saldo               |")
            print("|     5. Cek Saldo                  |")
            print("|     6. Kembali ke Menu Awal       |")
            print("|                                   |")
            print("+-----------------------------------+\n")
            pilih = input("Pilih menu 1/2/3/4/5/6: ").strip()

            if not pilih:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue

            if pilih == "1":
                lihat_konser_user()
            elif pilih == "2":
                beli_tiket()
            elif pilih == "3":
                lihat_tiket_user()
            elif pilih == "4":
                top_up_saldo()
            elif pilih == "5":
                cek_saldo()
            elif pilih == "6":
                clear()
                return menu_utama()
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Pilihan tidak valid!       |")
                print("+-----------------------------------+\n")
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI BELI TIKET                                                     |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def beli_tiket():
    clear()
    global user_saat_ini
    data_konser = baca_data_konser()
    data_tiket = baca_data_tiket()
    data_user = baca_data_user()
    
    while True:
        if not data_konser:
            print("\n+-----------------------------------+")
            print("|    Belum ada konser tersedia!     |")
            print("+-----------------------------------+\n")
            input("Tekan enter untuk kembali...")
            clear()
            return
        
        print("============================================================================================================================")
        print("                                                    KONSER SUATIS FEST                                                      ")
        print("============================================================================================================================")

        table = PrettyTable()
        table.field_names = [
            "No", "Nama Konser", "Tanggal", "Waktu Konser",
            "VVIP", "VIP", "Festival",
            "Stok VVIP", "Stok VIP", "Stok Festival"
        ]

        for konser in data_konser:
            waktu_mulai = konser["Waktu_konser"]["Waktu_mulai"]
            waktu_selesai = konser["Waktu_konser"]["Waktu_selesai"]
            waktu_konser = f"{waktu_mulai} - {waktu_selesai}"
            
            table.add_row([
                konser["nomor_konser"],
                konser["nama_konser"],
                konser.get("Tanggal", "-"),
                waktu_konser,
                f"Rp{konser['Harga']['VVIP']:,}",
                f"Rp{konser['Harga']['VIP']:,}",
                f"Rp{konser['Harga']['Festival']:,}",
                konser["Stok"]["VVIP"],
                konser["Stok"]["VIP"],
                konser["Stok"]["Festival"]
            ])

        print(table)
        
        print("\n+-----------------------------------+")
        print("|   Tekan enter pada input nomor    |")
        print("|   konser jika ingin kembali...    |")
        print("+-----------------------------------+\n")
        
        try:
            nomor_konser_input = input("Masukkan nomor konser yang ingin dibeli: ").strip()
            if nomor_konser_input == "":
                clear()
                return

            nomor_konser = int(nomor_konser_input)
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input harus berupa angka!        |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")
            continue
        
        konser_dipilih = None
        for k in data_konser:
            if k["nomor_konser"] == nomor_konser:
                konser_dipilih = k
                break
        
        if konser_dipilih is None:
            clear()
            print("\n+-----------------------------------+")
            print("|      Konser tidak ditemukan!      |")
            print("+-----------------------------------+\n")
            continue
        
        print("\n+-----------------------------------+")
        print(f" Konser: {konser_dipilih['nama_konser']}")
        print(f" Tanggal: {konser_dipilih['Tanggal']}")
        print(f" Waktu: {konser_dipilih['Waktu_konser']['Waktu_mulai']} - {konser_dipilih['Waktu_konser']['Waktu_selesai']}")
        print("+-----------------------------------+\n")
        
        table = PrettyTable()
        table.field_names = ["No", "Kategori", "Harga", "Stok Tersedia"]
        
        table.add_row([
            "1",
            "VVIP",
            f"Rp{konser_dipilih['Harga']['VVIP']:,}",
            konser_dipilih['Stok']['VVIP']
        ])
        table.add_row([
            "2",
            "VIP",
            f"Rp{konser_dipilih['Harga']['VIP']:,}",
            konser_dipilih['Stok']['VIP']
        ])
        table.add_row([
            "3",
            "Festival",
            f"Rp{konser_dipilih['Harga']['Festival']:,}",
            konser_dipilih['Stok']['Festival']
        ])
        
        print(table)
        
        try:
            pilih_kategori = input("\nPilih kategori 1/2/3: ").strip()
            
            if pilih_kategori == "1":
                kategori = "VVIP"
            elif pilih_kategori == "2":
                kategori = "VIP"
            elif pilih_kategori == "3":
                kategori = "Festival"
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Pilihan tidak valid!       |")
                print("+-----------------------------------+\n")
                continue
            
            jumlah = int(input(f"Jumlah tiket {kategori}: "))
            
            if jumlah <= 0:
                clear()
                print("\n+-----------------------------------+")
                print("| Jumlah tiket harus lebih dari 0!  |")
                print("+-----------------------------------+\n")
                continue
            
            if jumlah > konser_dipilih['Stok'][kategori]:
                clear()
                print("\n+-----------------------------------+")
                print("|        Stok tidak mencukupi!      |")
                print("+-----------------------------------+\n")
                continue
            
            total_harga = konser_dipilih['Harga'][kategori] * jumlah
            
            print(f"\n+-----------------------------------+")
            print(f" Total harga: Rp{total_harga:,}")
            print(f" Saldo Anda: Rp{user_saat_ini['Saldo']:,}")
            print("+-----------------------------------+\n")
            
            if user_saat_ini['Saldo'] < total_harga:
                clear()
                print("\n+-----------------------------------+")
                print("|         Saldo tidak cukup!        |")
                print("+-----------------------------------+\n")
                input("Tekan enter untuk kembali...")
                clear()
                return
            
            konfirmasi = input("Konfirmasi pembelian (ya/tidak)? ").strip().lower()
            if not konfirmasi:
                clear()
                print("\n+-----------------------------------+")
                print("|      Input tidak boleh kosong!    |")
                print("+-----------------------------------+\n")
                continue
            if konfirmasi != "ya":
                clear()
                print("\n+-----------------------------------+")
                print("|      Pembelian dibatalkan!        |")
                print("+-----------------------------------+\n")
                input("Tekan enter untuk kembali...")
                clear()
                return
            
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input harus berupa angka!      |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|  Input tidak boleh CTRL + C!      |")
            print("+-----------------------------------+\n")
            continue
        
        # Kurangi saldo user
        user_saat_ini['Saldo'] -= total_harga
        
        # Update saldo di data_user
        for u in data_user:
            if u['Nama'] == user_saat_ini['Nama']:
                u['Saldo'] = user_saat_ini['Saldo']
                break
        
        # Kurangi stok tiket
        konser_dipilih['Stok'][kategori] -= jumlah
        
        # Simpan data tiket
        tiket_baru = {
            "username": user_saat_ini['Nama'],
            "nama_konser": konser_dipilih['nama_konser'],
            "tanggal_konser": konser_dipilih['Tanggal'],
            "waktu_konser": konser_dipilih['Waktu_konser'],
            "kategori": kategori,
            "jumlah": jumlah,
            "total_harga": total_harga,
            "waktu_pembelian": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        
        data_tiket.append(tiket_baru)
        
        # Simpan semua perubahan
        simpan_data_konser(data_konser)
        simpan_data_tiket(data_tiket)
        simpan_data_user(data_user)
        
        clear()
        print("\n+-----------------------------------+")
        print("|  PEMBELIAN TIKET BERHASIL!        |")
        print("+-----------------------------------+")
        print(f" Konser      : {konser_dipilih['nama_konser']}")
        print(f" Tanggal     : {konser_dipilih['Tanggal']}")
        print(f" Waktu Konser: {waktu_mulai} - {waktu_selesai}")
        print(f" Kategori    : {kategori}")
        print(f" Jumlah      : {jumlah} tiket")
        print(f" Total       : Rp{total_harga:,}")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                              FUNGSI LIHAT TIKET USER                                                   |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def lihat_tiket_user():
    clear()
    global user_saat_ini
    data_tiket = baca_data_tiket()
    
    tiket_user = [t for t in data_tiket if t.get('username') == user_saat_ini['Nama']]
    
    if not tiket_user:
        print("\n+-----------------------------------+")
        print("|    Anda belum membeli tiket!      |")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return
    
    print("====================================================================================================")
    print("                                            TIKET SAYA                                              ")
    print("====================================================================================================")

    table = PrettyTable()
    table.field_names = [
        "Nama Konser", "Tanggal", "Waktu",
        "Kategori", "Jumlah", "Total Harga", "Waktu Pembelian"
    ]
    
    total_pembelian = 0
    
    for tiket in tiket_user:
        waktu_mulai = tiket["waktu_konser"]["Waktu_mulai"]
        waktu_selesai = tiket["waktu_konser"]["Waktu_selesai"]
        waktu_konser = f"{waktu_mulai} - {waktu_selesai}"
        
        table.add_row([
            tiket['nama_konser'],
            tiket['tanggal_konser'],
            waktu_konser,
            tiket['kategori'],
            tiket['jumlah'],
            f"Rp{tiket['total_harga']:,}",
            tiket['waktu_pembelian']
        ])
        total_pembelian += tiket['total_harga']
    
    print(table)
    print("\n+-----------------------------------+")
    print(f" Total Pembelian: Rp{total_pembelian:,}")
    print("+-----------------------------------+\n")
    input("Tekan enter untuk kembali...")
    clear()

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI TOP UP SALDO                                                   |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def top_up_saldo():
    clear()
    global user_saat_ini
    data_user = baca_data_user()
    
    while True:
        print("\n+-----------------------------------+")
        print("|            TOP UP SALDO           |")
        print("+-----------------------------------+")
        print("|   Top up minimal: Rp50.000        |")
        print("|   Top up maksimal: Rp2.000.000    |")
        print("+-----------------------------------+")
        print("|   Tekan enter pada input jumlah   |")
        print("|   jika ingin kembali...           |")
        print("+-----------------------------------+\n")
        print(f"Saldo saat ini: Rp{user_saat_ini['Saldo']:,}\n")
        
        try:
            jumlah_input = input("Masukkan jumlah top up: Rp").strip()
            if jumlah_input == "":
                clear()
                return
            
            jumlah = int(jumlah_input)
            
            if jumlah < 50000 or jumlah > 2000000:
                clear()
                print("\n+-----------------------------------+")
                print("| Top up minimal Rp50.000!          |")
                print("| Top up maksimal Rp2.000.000!      |")
                print("+-----------------------------------+\n")
                continue
            
        except ValueError:
            clear()
            print("\n+-----------------------------------+")
            print("|   Input harus berupa angka int!     |")
            print("+-----------------------------------+\n")
            continue
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|     Input tidak boleh CTRL + C!   |")
            print("+-----------------------------------+\n")
            continue
        
        user_saat_ini['Saldo'] += jumlah
        
        # Update saldo di data_user
        for u in data_user:
            if u['Nama'] == user_saat_ini['Nama']:
                u['Saldo'] = user_saat_ini['Saldo']
                break
        
        simpan_data_user(data_user)
        
        clear()
        print("\n+-----------------------------------+")
        print(" Top up berhasil!                  ")
        print(f" Saldo baru: Rp{user_saat_ini['Saldo']:,}")
        print("+-----------------------------------+\n")
        input("Tekan enter untuk kembali...")
        clear()
        return

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI CEK SALDO                                                      |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def cek_saldo():
    clear()
    global user_saat_ini
    
    print("\n+-----------------------------------+")
    print("|             SALDO ANDA            |")
    print("+-----------------------------------+")
    print(f" Saldo Anda: Rp{user_saat_ini['Saldo']:,}")
    print("+-----------------------------------+\n")
    
    try:
        input("Tekan enter untuk kembali...")
        clear()
    except KeyboardInterrupt:
        clear()
        print("\n+-----------------------------------+")
        print("|  Input tidak boleh CTRL + C!      |")
        print("+-----------------------------------+\n")

"+========================================================================================================================+"
"|                                                                                                                        |"
"|                                                  FUNGSI MENU UTAMA                                                     |"
"|                                                                                                                        |"
"+========================================================================================================================+"

def menu_utama():
    clear()
    while True:
        try:
            print("\n+-------------------------------------------+")
            print("|                                           |")
            print("|               SUATIS FEST                 |")
            print("|                                           |")
            print("+-------------------------------------------+")
            print("|                                           |")
            print("|          1. Login sebagai Panitia         |")
            print("|          2. Login sebagai User            |")
            print("|          3. Keluar                        |")
            print("|                                           |")
            print("+-------------------------------------------+\n")
            
            pilih = input("Pilih menu 1/2/3: ").strip()
            
            if not pilih:
                clear()
                print("\n+-----------------------------------+")
                print("|    Input tidak boleh kosong!      |")
                print("+-----------------------------------+\n")
                continue
                
            if pilih == "1":
                login_panitia()
            elif pilih == "2":
                pilih_registrasi()
            elif pilih == "3":
                clear()
                print("\n+-------------------------------------------+")
                print("|  Terima kasih telah menggunakan program!  |")
                print("+-------------------------------------------+\n")
                break
            else:
                clear()
                print("\n+-----------------------------------+")
                print("|        Pilihan tidak valid!       |")
                print("+-----------------------------------+\n")
        except KeyboardInterrupt:
            clear()
            print("\n+-----------------------------------+")
            print("|    Input tidak boleh CTRL + C!    |")
            print("+-----------------------------------+\n")

menu_utama()