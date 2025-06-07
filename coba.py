import json
import datetime

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
    
    if (staff_bener):
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
    if (pilihan == "1"):
        login_mahasiswa()
    elif (pilihan == "2"):
        menu_tamu()
    elif (pilihan == "0"):
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
        if (inp_id == a["id_anggota"]):
            mhs = a
            break
    
    if (mhs):
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
    pilihan = int(input("Pilihan Anda (0-5): "))

    if pilihan == 1:
        pinjam_buku(database["buku"], database["peminjaman"], database["reservasi"])
    elif pilihan == 2:
        pengembalian_buku(database["buku"], database["peminjaman"])
    elif pilihan == 3:
        perpanjang_peminjaman(database["peminjaman"], database["reservasi"])
    elif pilihan == 4:
        reservasi_buku(database["buku"], database["reservasi"])
    elif (pilihan == 5):
        perpanjang_anggota()

def pinjam_buku(data_buku, data_peminjaman, data_reservasi):
    print("")
    print("=== PINJAM BUKU ===")
    id_anggota = input("Masukkan ID Anggota: ")

    sudah_pinjam = False
    for pinjam in data_peminjaman:
        if (pinjam["id_anggota"] == id_anggota):
            sudah_pinjam = True
            break

    if (sudah_pinjam):
        print("Anda masih memiliki buku yang sedang dipinjam.")
        pilihan = input("Apakah Anda ingin mengembalikan buku terlebih dahulu? (Ya/Tidak): ")
        if (pilihan.lower() == "ya"):
            pengembalian_buku(data_buku, data_peminjaman)
        else:
            print("Silakan kembalikan buku terlebih dahulu sebelum meminjam yang baru.")
        return

    while True:
        id_buku = input("Masukkan ID Buku: ")
        buku_ditemukan = False

        for buku in data_buku:
            if (id_buku == buku["id_buku"]):
                buku_ditemukan = True
                if (buku["status"] == "Tersedia"):
                    durasi = int(input("Masukkan lama peminjaman (maksimal 14 hari): "))
                    if (durasi > 14):
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

                    buku["status"] = "Dipinjam"
                    with open('json/buku.json', 'w', encoding='utf-8') as file:
                        json.dump(data_buku, file, indent=4, ensure_ascii=False)

                    print(f"Buku '{buku['judul_buku']}' berhasil dipinjam selama {durasi} hari.")
                    print("Data peminjaman berhasil disimpan.")
                    return

                else:
                    print(f"Buku '{buku['judul_buku']}' saat ini sedang dipinjam.")
                    print("1. Reservasi buku")
                    print("2. Memilih buku lain")
                    print("3. Tidak jadi pinjam")
                    opsi = int(input("Pilihan Anda (1/2/3): "))

                    if (opsi == 1):
                        reservasi_buku(data_buku, data_reservasi, id_anggota, id_buku)
                        return
                    elif (opsi == 2):
                        continue
                    elif (opsi == 3):
                        print("Peminjaman dibatalkan.")
                        return
                    else: 
                        print ("Tidak ada opsi pilihan")
                    
        if (not buku_ditemukan):
            print("ID Buku tidak ditemukan.")
            homepage()


def pengembalian_buku(data_buku, data_peminjaman):
    print("")
    print("=== PENGEMBALIAN BUKU ===")
    id_buku = str(input("Masukkan ID Buku yang ingin dikembalikan: "))
    id_anggota = str(input("Masukkan ID Anggota: "))

    index_peminjaman = -1

    for i, pinjam in enumerate(data_peminjaman):
        if (pinjam["id_buku"] == id_buku and pinjam["id_anggota"] == id_anggota):
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

    for buku in data_buku:
        if (buku["id_buku"] == id_buku):
            buku["status"] = "Tersedia"
            break

    data_peminjaman.pop(index_peminjaman)

    with open('json/buku.json', 'w', encoding='utf-8') as file:
        json.dump(data_buku, file, indent=4, ensure_ascii=False)

    with open('json/peminjaman.json', 'w', encoding='utf-8') as file:
        json.dump(data_peminjaman, file, indent=4, ensure_ascii=False)

    print("Pengembalian buku berhasil.")
    homepage()

def reservasi_buku(data_buku, data_reservasi, id_anggota=None, id_buku=None):
    print("=== RESERVASI BUKU ===")
    if (not id_anggota):
        id_anggota = input("Masukkan ID Anggota: ")
    if (not id_buku):
        id_buku = input("Masukkan ID Buku yang ingin direservasi: ")
        
    buku_ditemukan = False

    for buku in data_buku:
        if (buku["id_buku"] == id_buku):
            buku_ditemukan = True
            if (buku["status"] == "Dipinjam"):
                sudah_reservasi = False
                for reservasi in data_reservasi:
                    if (reservasi["id_buku"] == id_buku and reservasi["id_anggota"] == id_anggota):
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
        homepage()
    
    homepage()

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

    homepage()

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
        if (not buku_ditemukan):
            print("Buku tidak ditemukan.")

        lanjut = input("Ingin mengubah kondisi buku lain? (y/n): ")
        if (lanjut=="n"):
            homepage()

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

def tambah_tanggal(hari, bulan, tahun, durasi):
    total_hari = tahun * 365 + bulan * 30 + hari + durasi
    tahun_baru = total_hari // 365
    sisa_hari = total_hari % 365
    bulan_baru = sisa_hari // 30
    hari_baru = sisa_hari % 30
    if hari_baru == 0:
        hari_baru = 1
    return hari_baru, bulan_baru, tahun_baru

def tampilkan_tanggal(tgl):
    return f"{tgl[0]:02d}-{tgl[1]:02d}-{tgl[2]}"

def cari_peminjaman(peminjaman, id_buku, id_anggota):
    for i in range(len(peminjaman)):
        if peminjaman[i] is not None:
            if peminjaman[i]["id_buku"] == id_buku and peminjaman[i]["id_anggota"] == id_anggota:
                return i
    return -1

def ada_reservasi_lain(reservasi, id_buku, id_anggota):
    for r in reservasi:
        if r["id_buku"] == id_buku and r["id_anggota"] != id_anggota:
            return True
    return False

def perpanjang_peminjaman(peminjaman, reservasi):
    print("")
    print("=== PERPANJANGAN PEMINJAMAN ===")
    id_buku = input("ID Buku yang dipinjam  : ")
    id_anggota = input("ID Anggota peminjam    : ")

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
    
    homepage()

def perpanjang_anggota():
    print("\n=== PERPANJANGAN KEANGGOTAAN ===")
    id_anggota = input("Masukkan ID Anggota: ")
    nama = input("Masukkan Nama Anggota: ")
    durasi = input("Durasi perpanjangan (contoh: 12 bulan): ")

    anggota_ditemukan = False

    for anggota in database["anggota"]:
        if anggota["id_anggota"] == id_anggota and anggota["nama_anggota"].lower() == nama.lower():
            anggota_ditemukan = True

    if anggota_ditemukan:
        print("Perpanjangan berhasil selama ", durasi)
    else:
        print("ID tidak terdaftar.")

def main():
    homepage()
if __name__ == '__main__':
    main()