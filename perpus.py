# Nama file : perpus.py

# Nama Penulis :
# 2472001 - Aurellia Yemima Tomy
# 2472003 - Maria Mayang Prihariyanti Panduwardani
# 2472014 - Archangela Sheilla Hariyanto Sundjaya

# Tujuan Program:
# Program ini adalah program sistem perpustakaan sederhana yang memungkinkan 
# pengguna (Staff, Anggota perpustakaan, pengunjung) untuk melakukan berbagai
# kegiatan seperti peminjaman buku, pengembalian buku, reservasi buku, dan 
# perpanjangan keanggotaan.

# Program ini menggunakan file JSON sebagai database untuk menyimpan data anggota,
# buku, pengunjung, staff, peminjaman, dan reservasi. 

import json
import datetime
import sys

with open('json/Anggota.json', 'r', encoding='utf-8') as file:
    anggota = json.load(file)

with open('json/buku.json', 'r', encoding='utf-8') as file:
    buku = json.load(file)

with open('json/pengunjung.json', 'r', encoding='utf-8') as file:
    pengunjung = json.load(file)

with open('json/staff.json', 'r', encoding='utf-8') as file:
    staff = json.load(file)

with open('json/peminjaman.json', 'r', encoding='utf-8') as file:
    peminjaman = json.load(file)

with open('json/reservasi.json', 'r', encoding='utf-8') as file:
    reservasi = json.load(file)

database = {
    "anggota": anggota,
    "buku": buku,
    "pengunjung": pengunjung,
    "staff": staff,
    "peminjaman": peminjaman,
    "reservasi": reservasi
}

# Fungsi untuk menampilkan homepage perpustakaan
# Fungsi ini akan menampilkan pilihan peran pengguna (Staff atau Pengunjung) 
# dan mengarahkan ke fungsi login yang sesuai.
# peran : var. input untuk memilih peran pengguna (int)
def homepage():
    print ("="*50)
    print (" === Selamat datang di perpustakaan Maranatha! === ")
    print ("="*50)
    print ("")
    print ("Silakan pilih peran Anda:")
    print ("1. Staff")
    print ("2. Pengunjung")
    print ("0. Keluar")
    
    peran = int(input("Pilihan Anda (0-2): "))

    if (peran==0):
        print ("Terima kasih telah mengunjungi perpustakaan Maranatha!")
        sys.exit()
    elif (peran==1):
        login_staff ()
    elif (peran==2):
        login_pengunjung()
    else:
        print ("Maaf, pilihan tidak tersedia.")
        homepage()

# Fungsi untuk login staff perpustakaan
# inp_id : var. input utk ID staff (str)
# staff_bener : var. boolean untuk mengecek apakah ID staff benar (boolean)
# i : var. index untuk iterasi (int)
# N : var. jumlah staff dalam database (int)    
def login_staff():
    print ("")
    print ("=== Halo staff perpustakaan Maranatha! ===")
    inp_id = str(input ("Silakan masukkan ID Staff: "))

    staff_bener = False
    i = 0
    N = len(database["staff"])

    while (i < N and not staff_bener):
        if (database["staff"][i]["id_staff"] == inp_id):
            staff_bener = True
        else:
            i += 1
    
    if (staff_bener):
        staff_bener = database["staff"][i]
        print(f"Selamat datang, {staff_bener.get('nama', staff_bener.get('nama_staff', 'Staff'))}!")
        page_staff()
    else:
        print("ID Staff tidak ditemukan. Akses ditolak.")
        homepage()

# Fungsi untuk login pengunjung 
# pilihan : var. input utk memilih apakah pengunjung mahasiswa atau tamu (str)
def login_pengunjung():
    print("=== PENGUNJUNG ===")
    print("Apakah Anda mahasiswa?")
    print("1. Ya, saya mahasiswa")
    print("2. Bukan, saya tamu")
    print("0. Kembali")
    
    pilihan = input("Pilihan Anda (0-2): ")
    if (pilihan == "1"):
        login_mahasiswa()
    elif (pilihan == "2"):
        menu_tamu()
    elif (pilihan == "0"):
        homepage()
    else:
        print("Maaf, pilihan tidak tersedia.")
        homepage()

# Fungsi untuk login mahasiswa
# inp_id : var. input untuk ID anggota (str)
# mhs : var. untuk menyimpan data mahasiswa yang ditemukan (dict)
# a : var. index untuk iterasi (int)

def login_mahasiswa():  
    print ("")
    print ("=== Halo mahasiswa perpustakaan Maranatha! ===")
    inp_id = str(input("Silakan masukkan ID Anggota: "))

    mhs = None
    for a in range (len(database["anggota"])):
        if inp_id == database["anggota"][a]["id_anggota"]:
            mhs = database["anggota"][a]
            break
    
    if (mhs):
        print(f"Selamat datang, {mhs.get('nama_anggota', 'Anggota')}!")
        page_anggota()
    else:
        print("ID anggota tidak ditemukan. Akses ditolak.")
        login_pengunjung()

# Fungsi untuk menampilkan halaman anggota perpustakaan
# pilihan : var. input untuk memilih kegiatan yang akan dilakukan (int)
def page_anggota ():
    print ()
    print ("Silakan pilih kegiatan yang akan kamu lakukan!")
    print ("1. Pinjam Buku")
    print ("2. Pengembalian Buku")
    print ("3. Perpanjang Peminjaman")
    print ("4. Reservasi Buku")
    print ("5. Perpanjang keanggotaan")
    print ("0. Kembali")
    pilihan = int(input("Pilihan Anda (0-5): "))

    if (pilihan == 1):
        pinjam_buku(database["buku"], database["peminjaman"], database["reservasi"])
    elif (pilihan == 2):
        pengembalian_buku(database["buku"], database["peminjaman"])
    elif (pilihan == 3):
        perpanjang_peminjaman(database["peminjaman"], database["reservasi"])
    elif (pilihan == 4):
        reservasi_buku(database["buku"], database["reservasi"])
    elif (pilihan == 5):
        perpanjang_anggota()
    if (pilihan==0):
        homepage()

# Fungsi untuk meminjam buku
# id_anggota : var. input untuk ID anggota (str)
# sudah_pinjam : var. boolean untuk mengecek apakah anggota 
# sudah meminjam buku (boolean)
# pilihan : var. input utk menampung pilihan mengembalikan buku (str)
# id_buku : var. input utk ID Buku (str)
# buku_ditemukan : var. boolean untuk mengecek apakah buku ditemukan (boolean)
# durasi : var. input untuk lama peminjaman (int)
# tanggal_input : var. input untuk tanggal pinjam (str)
# tanggal_pinjam : var. untuk menyimpan tanggal pinjam (date)
# tanggal_kembali : var. untuk menyimpan tanggal kembali (date)
# tanggal_pinjam_list : var. untuk menyimpan tanggal pinjam dalam list (list)
# tanggal_kembali_list : var. untuk menyimpan tanggal kembali dalam list (list)
# data_baru : var. untuk menyimpan data peminjaman baru (dict)
# pinjam : var. index untuk iterasi (int)
# opsi : var. input untuk pilihan reservasi buku (int)
def pinjam_buku(data_buku, data_peminjaman, data_reservasi):
    print()
    print("=== PINJAM BUKU ===")
    id_anggota = str(input("Masukkan ID Anggota: "))

    sudah_pinjam = False
    for pinjam in range(len(data_peminjaman)):
        if data_peminjaman[pinjam]["id_anggota"] == id_anggota:
            sudah_pinjam = True

    if (sudah_pinjam):
        print("Anda masih memiliki buku yang sedang dipinjam.")
        pilihan = str(input("Apakah Anda ingin mengembalikan buku terlebih dahulu? (Ya/Tidak): "))
        if pilihan.lower() == "ya":
            pengembalian_buku(data_buku, data_peminjaman)
        else:
            print("Silakan kembalikan buku terlebih dahulu sebelum meminjam yang baru.")
        page_anggota()
        return  # keluar agar tidak lanjut ke bagian bawah

    while True:
        id_buku = str(input("Masukkan ID Buku: "))
        buku_ditemukan = False

        for buku in range(len(data_buku)):
            if id_buku == data_buku[buku]["id_buku"]:
                buku_ditemukan = True
                if data_buku[buku]["status"] == "Tersedia":
                    durasi = int(input("Masukkan lama peminjaman (maksimal 14 hari): "))
                    if durasi > 14:
                        print("Durasi melebihi 14 hari, diset ke 14 hari.")
                        durasi = 14

                    tanggal_input = input("Masukkan tanggal pinjam (dd-mm-yyyy): ")
                    hari, bulan, tahun = map(int, tanggal_input.split('-'))
                    tanggal_pinjam = datetime.date(tahun, bulan, hari)
                    tanggal_kembali = tanggal_pinjam + datetime.timedelta(days=durasi)

                    tanggal_pinjam_list = [tanggal_pinjam.day, tanggal_pinjam.month, tanggal_pinjam.year]
                    tanggal_kembali_list = [tanggal_kembali.day, tanggal_kembali.month, tanggal_kembali.year]

                    data_baru = {
                        "id_buku": id_buku,
                        "id_anggota": id_anggota,
                        "tanggal_pinjam": tanggal_pinjam_list,
                        "tanggal_kembali": tanggal_kembali_list,
                        "durasi": durasi,
                        "sudah_perpanjang": False
                    }

                    data_peminjaman.append(data_baru)

                    with open('json/peminjaman.json', 'w', encoding='utf-8') as file:
                        json.dump(data_peminjaman, file, indent=4, ensure_ascii=False)

                    data_buku[buku]["status"] = "Dipinjam"
                    with open('json/buku.json', 'w', encoding='utf-8') as file:
                        json.dump(data_buku, file, indent=4, ensure_ascii=False)

                    print(f"Buku '{data_buku[buku]['judul_buku']}' berhasil dipinjam selama {durasi} hari.")
                    print("Data peminjaman berhasil disimpan.")
                    break  

                else:
                    print(f"Buku '{data_buku[buku]['judul_buku']}' saat ini sedang dipinjam.")
                    print("1. Reservasi buku")
                    print("2. Memilih buku lain")
                    print("3. Tidak jadi pinjam")
                    opsi = int(input("Pilihan Anda (1/2/3): "))

                    if opsi == 1:
                        reservasi_buku(data_buku, data_reservasi, id_anggota, id_buku)
                    elif opsi == 2:
                        break  
                    elif opsi == 3:
                        print("Peminjaman dibatalkan.")
                        break 
                    else:
                        print("Tidak ada opsi pilihan")
                        break

        if not buku_ditemukan:
            print("ID Buku tidak ditemukan.")
        else:
            break  

    page_anggota()  

# Fungsi untuk mengembalikan buku
# id_buku : var. input untuk ID Buku yang ingin dikembalikan (str)
# id_anggota : var. input untuk ID Anggota (str)
# index_peminjaman : var. untuk menyimpan index peminjaman yang ditemukan (int)
# tanggal_kembali : var. untuk menyimpan tanggal kembali (list)
# tanggal_kembali_obj : var. untuk menyimpan tanggal kembali sebagai 
# objek date (date)
# hari_ini : var. input untuk tanggal pengembalian (str)
# h, b, t : var. untuk menyimpan hari, bulan, tahun dari tanggal 
# pengembalian (int)
# tanggal_pengembalian : var. untuk menyimpan tanggal pengembalian sebagai
# selisih_hari : var. untuk menyimpan selisih hari antara tanggal pengembalian
def pengembalian_buku(data_buku, data_peminjaman):
    print()
    print("=== PENGEMBALIAN BUKU ===")
    id_buku = str(input("Masukkan ID Buku yang ingin dikembalikan: "))
    id_anggota = str(input("Masukkan ID Anggota: "))

    index_peminjaman = -1

    for i in range(len(data_peminjaman)):  
        pinjam = data_peminjaman[i]
        if (pinjam["id_buku"] == id_buku) and (pinjam["id_anggota"] == id_anggota):
            index_peminjaman = i
            break

    if (index_peminjaman == -1):
        print("Data peminjaman tidak ditemukan.")
        return

    tanggal_kembali = data_peminjaman[index_peminjaman]["tanggal_kembali"]
    tanggal_kembali_obj = datetime.date(tanggal_kembali[2], tanggal_kembali[1], tanggal_kembali[0])

    hari_ini = input("Masukkan tanggal pengembalian (dd-mm-yyyy): ")
    h, b, t = map(int, hari_ini.split('-'))
    tanggal_pengembalian = datetime.date(t, b, h)

    selisih_hari = (tanggal_pengembalian - tanggal_kembali_obj).days

    if (selisih_hari > 0):
        denda = selisih_hari * 5000
        print(f"Terlambat {selisih_hari} hari. Anda harus membayar denda Rp {denda:,}")
    else:
        print("Buku dikembalikan tepat waktu. Tidak ada denda.")

    for i in range(len(data_buku)):
        if data_buku[i]["id_buku"] == id_buku:
            data_buku[i]["status"] = "Tersedia"
            break

    data_peminjaman.pop(index_peminjaman)

    with open('json/buku.json', 'w', encoding='utf-8') as file:
        json.dump(data_buku, file, indent=4, ensure_ascii=False)

    with open('json/peminjaman.json', 'w', encoding='utf-8') as file:
        json.dump(data_peminjaman, file, indent=4, ensure_ascii=False)

    print("Pengembalian buku berhasil.")
    page_anggota()

# Fungsi untuk reservasi buku
# id_anggota : var. input untuk ID Anggota (str)
# id_buku : var. input untuk ID Buku yang ingin direservasi (str)
# buku_ditemukan : var. boolean untuk mengecek apakah buku ditemukan (boolean)
# sudah_reservasi : var. boolean untuk mengecek apakah anggota sudah
def reservasi_buku(data_buku, data_reservasi, id_anggota=None, id_buku=None):
    print("=== RESERVASI BUKU ===")
    if (not id_anggota):
        id_anggota = str(input("Masukkan ID Anggota: "))
    if (not id_buku):
        id_buku = str(input("Masukkan ID Buku yang ingin direservasi: "))
        
    buku_ditemukan = False

    for i in range(len(data_buku)):
        if (id_buku == data_buku[i]["id_buku"]):
            buku_ditemukan = True
            if (data_buku[i]["status"] == "Dipinjam"):
                sudah_reservasi = False
                for j in range(len(data_reservasi)):
                    if (data_reservasi[j]["id_buku"] == id_buku) and (data_reservasi[j]["id_anggota"] == id_anggota):
                        sudah_reservasi = True
                        break


                if (sudah_reservasi):
                    print("Anda sudah melakukan reservasi untuk buku ini.")
                else:
                    data_baru = {
                        "id_buku": id_buku,
                        "id_anggota": id_anggota
                    }
                    data_reservasi.append(data_baru)

                    with open('json/reservasi.json', 'w', encoding='utf-8') as file:
                        json.dump(data_reservasi, file, indent=4, ensure_ascii=False)

                    print(f"Reservasi buku '{buku['judul_buku']}' berhasil disimpan.")
            else:
                print("Buku saat ini tersedia. Silakan pinjam langsung.")
            

    if (not buku_ditemukan):
        print("ID Buku tidak ditemukan.")
        page_anggota()
    
    page_anggota()

# Fungsi untuk menampilkan menu tamu
# pilihan : var. input untuk memilih apakah ingin melihat koleksi 
# buku atau kembali (int)
def menu_tamu():
    print("")
    print("=== MENU TAMU ===")
    print("1. Lihat Koleksi Buku")
    print("0. Kembali")

    pilihan = int(input("Pilihan Anda (0/1): "))

    if (pilihan==1):
        lihat_daftar_buku()
    elif (pilihan==0):
        print ("Terima kasih sudah berkunjung ke perpustakaan Maranatha!")
        homepage()
    else: 
        print ("Maaf, pilihan tidak tersedia")
        menu_tamu()
    homepage()

# Fungsi untuk menampilkan halaman staff perpustakaan
# pilihan : var. input untuk memilih kegiatan yang akan dilakukan (int)
def page_staff():
    print("")
    print("Silakan pilih kegiatan yang akan kamu lakukan:")
    print("1. Lihat daftar buku")
    print("2. Cek jumlah stok buku")
    print("3. Edit kondisi buku")
    print("4. Edit buku")
    print("0. Keluar")
    pilihan = int(input("Masukkan pilihan (0-4): "))

    if (pilihan == 1):
        lihat_daftar_buku() 
    elif (pilihan == 2):
        cek_jumlah_stok()  
    elif (pilihan == 3):
        edit_kondisi_buku() 
    elif (pilihan == 4):
        edit_buku(database["buku"])
    elif (pilihan == 0):
        print("Terima kasih, sampai jumpa kembali!")
        homepage()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        page_staff()

    page_staff()

# Fungsi untuk melihat daftar buku
# Ini akan menampilkan daftar buku yang ada di perpustakaan
def lihat_daftar_buku():
    print("")
    print("Daftar Buku di Perpustakaan:")
    for i in range(len(database["buku"])):
        buku = database["buku"][i]
        print(f"{buku['id_buku']} - {buku['judul_buku']} ({buku['stok']})({buku['status']})")
    print()

# Fungsi untuk mengecek jumlah stok buku
def cek_jumlah_stok():
    print("")
    print("Jumlah stok buku:")
    for i in range(len(database["buku"])):
        buku = database["buku"][i]
        print(f"{buku['id_buku']} - {buku['judul_buku']}: {buku['stok']} buah")
    page_staff()

# Fungsi untuk mengedit kondisi buku
# id_buku : var. input untuk ID Buku yang ingin diubah kondisinya (str)
# buku_ditemukan : var. boolean untuk mengecek apakah buku ditemukan (boolean)
# lanjut : var. input untuk menanyakan apakah ingin mengubah 
# kondisi buku lain (str)
def edit_kondisi_buku():
    while True:
        id_buku = str(input("Masukkan ID Buku yang ingin diubah kondisinya: "))
        buku_ditemukan = False
        for i in range(len(database["buku"])):
            if (id_buku == database["buku"][i]["id_buku"]):
                buku = database["buku"][i] 
                print(f"Kondisi saat ini: {buku['kondisi_buku']}")
                kondisi_baru = input("Masukkan kondisi baru: ")
                buku["kondisi_buku"] = kondisi_baru
                print("Kondisi buku berhasil diperbarui.")

                with open('json/buku.json', 'w', encoding='utf-8') as file:
                    json.dump(database["buku"], file, indent=4, ensure_ascii=False)

                buku_ditemukan = True
                break

        if (not buku_ditemukan):
            print("Buku tidak ditemukan.")

        lanjut = str(input("Ingin mengubah kondisi buku lain? (y/n): "))
        if (lanjut.lower() != "y"):
            break

    page_staff()
    
def edit_buku(data_buku):
    print ("")
    print ("Apa yang ingin kamu lakukan?")
    print ("1. Tambah buku baru")
    print ("2. Hapus buku dari database")
    pilihan = int(input("Pilihan (1/2): "))

    if (pilihan == 1):
        print("Masukkan data buku baru:")
        id_buku = str(input("ID Buku: "))
        
        for i in range(len(data_buku)):
            if (id_buku == data_buku[i]["id_buku"]):
                print("ID Buku sudah digunakan. Gunakan ID yang lain.")
                return
        
        judul = str(input("Judul Buku: "))
        tipe = str(input("Tipe buku (Buku/Buku Digital/Skripsi/Jurnal): "))
        stok = int(input("Stok awal: "))
        kondisi = str(input("Kondisi awal buku (Baik/Rusak): "))
        jenis = str(input("Jenis Buku (Pendidikan/Novel/Jurnal/Komik/Majalah): "))
        status = str(input("Status (Tersedia/Dipinjam): "))
        pengarang = str(input("Pengarang: "))

        buku_baru = {
            "id_buku": id_buku,
            "judul_buku": judul,
            "tipe":tipe,
            "stok": stok,
            "kondisi_buku": kondisi,
            "jenis": jenis,
            "status": status,
            "pengarang": pengarang
        }

        data_buku.append(buku_baru)
        with open('json/buku.json', 'w', encoding='utf-8') as file:
            json.dump(database["buku"], file, indent=4, ensure_ascii=False)

        print("Buku baru berhasil ditambahkan ke database.")

    elif (pilihan == 2):
        cari_id = str(input("Masukkan ID Buku yang ingin dihapus: "))
        temu = False
        for buku in data_buku:
            if (cari_id == buku["id_buku"]):
                print(f"Judul: {buku['judul_buku']}")
                konfirmasi = str(input("Yakin ingin menghapus buku ini? (y/n): "))
                if (konfirmasi== "y"):
                    data_buku.remove(buku)
                    with open('json/buku.json', 'w', encoding='utf-8') as file:
                        json.dump(database["buku"], file, indent=4, ensure_ascii=False)

                    print("Buku berhasil dihapus dari database.")
                else:
                    print("Penghapusan dibatalkan.")
                temu = True
                page_staff()
        if (not temu):
            print("ID buku tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")
        edit_buku(database["buku"])
    page_staff()

# Fungsi untuk menambahkan tanggal
# total_hari : var. untuk menghitung total hari dari tahun, 
# bulan, hari, dan durasi (int)
# tahun_baru : var. untuk menyimpan tahun baru setelah penambahan (int)
# sisa_hari : var. untuk menyimpan sisa hari setelah pembagian (int)
# bulan_baru : var. untuk menyimpan bulan baru setelah penambahan (int)
# hari_baru : var. untuk menyimpan hari baru setelah penambahan (int)
def tambah_tanggal(hari, bulan, tahun, durasi):
    total_hari = tahun * 365 + bulan * 30 + hari + durasi
    tahun_baru = total_hari // 365
    sisa_hari = total_hari % 365
    bulan_baru = sisa_hari // 30
    hari_baru = sisa_hari % 30
    if (hari_baru == 0):
        hari_baru = 1
    return hari_baru, bulan_baru, tahun_baru

# Fungsi untuk menampilkan tanggal dalam format dd-mm-yyyy
def tampilkan_tanggal(tgl):
    return f"{tgl[0]:02d}-{tgl[1]:02d}-{tgl[2]}"

# Fungsi untuk mencari peminjaman berdasarkan
def cari_peminjaman(peminjaman, id_buku, id_anggota):
    for i in range(len(peminjaman)):
        if (peminjaman[i] is not None):
            if (peminjaman[i]["id_buku"] == id_buku ) and (peminjaman[i]["id_anggota"] == id_anggota):
                return i
    return -1

# Fungsi untuk mengecek apakah ada reservasi lain untuk buku yang sama
def ada_reservasi_lain(reservasi, id_buku, id_anggota):
    for i in range(len(reservasi)):
        if (reservasi[i]["id_buku"] == id_buku) and (reservasi[i]["id_anggota"] != id_anggota):
            return True
    return False

# Fungsi untuk memperpanjang peminjaman buku
# id_buku : var. input untuk ID Buku yang dipinjam (str)
# id_anggota : var. input untuk ID Anggota peminjam (str)
# i : var. untuk menyimpan index peminjaman yang ditemukan (int)
# durasi : var. input untuk durasi perpanjangan (int)
def perpanjang_peminjaman(peminjaman, reservasi):
    print("")
    print("=== PERPANJANGAN PEMINJAMAN ===")
    id_buku = str(input("ID Buku yang dipinjam  : "))
    id_anggota = str(input("ID Anggota peminjam    : "))

    i = cari_peminjaman(peminjaman, id_buku, id_anggota)
    if (i == -1):
        print("Data peminjaman tidak ditemukan.")
    else:
        if peminjaman[i]["sudah_perpanjang"]:
            print("Peminjaman ini sudah pernah diperpanjang.")
        elif ada_reservasi_lain(reservasi, id_buku, id_anggota):
            print("Tidak bisa diperpanjang: buku sudah direservasi anggota lain.")
        else:
            print("Tanggal kembali sebelumnya :", tampilkan_tanggal(peminjaman[i]["tanggal_kembali"]))
            durasi = int(input("Durasi perpanjangan (maks 7): "))
            if (durasi > 7):
                print("Durasi melebihi 7 hari! Diset ke 7.")
                durasi = 7
            h, b, t = peminjaman[i]["tanggal_kembali"]
            hk, bk, tk = tambah_tanggal(h, b, t, durasi)
            peminjaman[i]["tanggal_kembali"] = (hk, bk, tk)
            peminjaman[i]["sudah_perpanjang"] = True
            print("Perpanjangan berhasil.")
            print("Tanggal kembali baru       :", tampilkan_tanggal(peminjaman[i]["tanggal_kembali"]))
            with open('json/peminjaman.json', 'w', encoding='utf-8') as file:
                json.dump(peminjaman, file, indent=4)
    
    page_anggota()

# Fungsi untuk menambahkan bulan pada tanggal
# tahun : var. untuk menyimpan tahun dari tanggal (int)
# bulan : var. untuk menyimpan bulan dari tanggal (int)
# hari : var. untuk menyimpan hari dari tanggal (int)
# hari_maks : var. untuk menyimpan jumlah hari maksimum pada bulan (int)
def tambah_bulan(tanggal, durasi_bulan):
    tahun = tanggal.year
    bulan = tanggal.month + durasi_bulan
    hari = tanggal.day

    tahun += (bulan - 1) // 12
    bulan = ((bulan - 1) % 12) + 1

    hari_maks = [31, 29 if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0) else 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31][bulan - 1]
    if (hari > hari_maks):
        hari = hari_maks

    return datetime(tahun, bulan, hari)

# Fungsi untuk memperpanjang keanggotaan
# id_anggota : var. input untuk ID Anggota (str)
# nama : var. input untuk nama Anggota (str)
# durasi : var. input untuk durasi perpanjangan (int)
# anggota_ditemukan : var. boolean untuk mengecek apakah 
# anggota ditemukan (boolean)
# exp_lama : var. untuk menyimpan tanggal kadaluarsa lama (date)
# perpanjang_sampai : var. untuk menyimpan tanggal perpanjangan (date)
def perpanjang_anggota():
    print()
    print("=== PERPANJANGAN KEANGGOTAAN ===")
    id_anggota = str(input("Masukkan ID Anggota: "))
    nama = str(input("Masukkan Nama Anggota: "))
    durasi = int(input("Durasi perpanjangan (dalam bulan): "))

    anggota_ditemukan = False

    for anggota in range (database["anggota"]):
        if (id_anggota == anggota["id_anggota"]) and (nama == anggota["nama_anggota"]):
            anggota_ditemukan = True

            exp_lama = datetime.strptime(anggota["exp_kartu"], "%Y-%m-%d")
            perpanjang_sampai = tambah_bulan(exp_lama, durasi)

            anggota["exp_kartu"] = perpanjang_sampai.strftime("%Y-%m-%d")
            print("Perpanjangan berhasil!")
            print(f"Keanggotaan berhasil diperpanjang hingga {perpanjang_sampai.strftime('%d-%m-%Y')}.")

            with open('json/Anggota.json', 'w', encoding='utf-8') as file:
                json.dump(database["anggota"], file, indent=4, ensure_ascii=False)
            break

    if (not anggota_ditemukan):
        print("ID atau nama anggota tidak cocok! Perpanjangan gagal.")
    page_anggota()

# Fungsi utama untuk menjalankan program
def main():
    homepage()
if __name__ == '__main__':
    main()