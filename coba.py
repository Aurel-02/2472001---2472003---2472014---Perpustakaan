import json

with open('json/Anggota.json', 'r', encoding='utf-8') as file:
    anggota = json.load(file)

with open('json/buku.json', 'r', encoding='utf-8') as file:
    buku = json.load(file)

with open('json/pengunjung.json', 'r', encoding='utf-8') as file:
    pengunjung = json.load(file)

with open('json/staff.json', 'r', encoding='utf-8') as file:
    staff = json.load(file)

database = {
    "anggota": anggota,
    "buku": buku,
    "pengunjung": pengunjung,
    "staff": staff
}

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
    elif (peran==1):
        login_staff ()
    elif (peran==2):
        login_pengunjung()
    else:
        print ("Maaf, pilihan tidak tersedia.")
        homepage()

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
    
    if staff_bener:
        staff_bener = database["staff"][i]
        print(f"Selamat datang, {staff_bener.get('nama', staff_bener.get('nama_staff', 'Staff'))}!")
        page_staff()
    else:
        print("ID Staff tidak ditemukan. Akses ditolak.")
        homepage()

def login_pengunjung():
    print("=== PENGUNJUNG ===")
    print("Apakah Anda mahasiswa?")
    print("1. Ya, saya mahasiswa")
    print("2. Bukan, saya tamu")
    print("0. Kembali")
    
    pilihan = input("Pilihan Anda (0-2): ")
    if pilihan == "1":
        login_mahasiswa()
    elif pilihan == "2":
        menu_tamu()
    elif pilihan == "0":
        homepage()
    else:
        print("Maaf, pilihan tidak tersedia.")
        homepage()

def login_mahasiswa():
    print ("")
    print ("=== Halo mahasiswa perpustakaan Maranatha! ===")
    inp_id = input("Silakan masukkan ID Anggota: ")

    mhs = None
    for a in database["anggota"]:
        if inp_id == a["id_anggota"]:
            mhs = a
            break
    
    if mhs:
        print(f"Selamat datang, {mhs.get('nama_anggota', 'Anggota')}!")
        page_anggota()
    else:
        print("ID anggota tidak ditemukan. Akses ditolak.")
        homepage()

def page_anggota ():
    print ("")
    print ("Silakan pilih kegiatan yang akan kamu lakukan!")
    print ("1. Pinjam Buku")
    print ("2. Pengembalian Buku")
    print ("3. Perpanjang Peminjaman")
    print ("4. Reservasi Buku")
    print ("5. Perpanjang keanggotaan")
    print ("0. Kembali")

def menu_tamu():
    print("=== MENU TAMU ===")
    print("1. Lihat Koleksi Buku")
    print("2. Daftar Akun Pengunjung")
    print("0. Kembali")
    homepage()

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

def lihat_daftar_buku():
    print("")
    print("Daftar Buku di Perpustakaan:")
    for buku in database["buku"]:
        print(f"{buku['id_buku']} - {buku['judul_buku']} ({buku['stok']})({buku['status']})")
    homepage()

def cek_jumlah_stok():
    print("")
    print("Jumlah stok buku:")
    for buku in database["buku"]:
        print(f"{buku['judul_buku']}: {buku['stok']} buah")
    homepage()

def edit_kondisi_buku():
    while True:
        id_buku = input("Masukkan ID Buku yang ingin diubah kondisinya: ")
        buku_ditemukan = False
        for buku in database["buku"]:
            if (id_buku == buku["id_buku"]):
                print(f"Kondisi saat ini: {buku['kondisi_buku']}")
                kondisi_baru = input("Masukkan kondisi baru: ")
                buku["kondisi_buku"] = kondisi_baru
                print("Kondisi buku berhasil diperbarui.")
                buku_ditemukan = True
                break
        if not buku_ditemukan:
            print("Buku tidak ditemukan.")

        lanjut = input("Ingin mengubah kondisi buku lain? (y/n): ")
        if (lanjut=="n"):
            homepage()
    
def edit_buku(data_buku):
    print ("")
    print ("Apa yang ingin kamu lakukan?")
    print ("1. Tambah buku baru")
    print ("2. Hapus buku dari database")
    pilihan = int(input("Pilihan (1/2): "))

    if (pilihan == 1):
        print("Masukkan data buku baru:")
        id_buku = str(input("ID Buku: "))
        
        for buku in data_buku:
            if (id_buku == buku["id_buku"]):
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
        cari_id = input("Masukkan ID Buku yang ingin dihapus: ")
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
                homepage()
        if (not temu):
            print("ID buku tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")
        edit_buku(database["buku"])
    homepage()

def main():
    homepage()
if __name__ == '__main__':
    main()