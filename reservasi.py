import json

def cek_anggota(id_anggota):
    with open("json/Anggota.json") as file:
        data = json.load(file)
        for anggota in data:
            if anggota["id"] == id_anggota:
                return True
    return False

def cek_buku(id_buku):
    with open("json/buku.json") as file:
        data = json.load(file)
        for buku in data:
            if buku["id"] == id_buku:
                return True
    return False

def data ():
    global Buku, Peminjam, ID_Anggota
    i = 0

    print ("Ketik 9999 untuk selesai !")
    id_buku = str(input("Masukkan ID buku : "))

    while (id_buku != 9999):
        nama = str(input("Masukkan Nama Peminjam : "))
        kartu = str(input("Memiliki kartu anggota ? (Yes / NO) "))

        if (kartu == "Yes"):
            Buku[i] = id_buku
            Peminjam[i] = nama
            ID_Anggota[i] = int(input("Masukkan ID Anggota : "))
            i = i + 1
        else:
            print("Daftar sebagai anggota untuk reservasi !")
    return i 

def reservasi (N):
    global Buku, Peminjam, ID_Anggota

    print("==== Reservasi Buku yang ingin dipinjam ====")
    print()
    for i in range (0,N,1):
        print("ID buku : ", Buku[i])
        print("Nama Peminjam : ", Peminjam[i])
        print("ID Anggota : ", ID_Anggota[i])
        print("---------------------------------------")
    return

def main ():
    N = data ()
    reservasi (N)    

if __name__ == '__main__':
    global Nmax, Buku, Peminjam, ID_Anggota
    Nmax = 100
    Buku = Nmax * [None]
    Peminjam = Nmax * [None]
    ID_Anggota = Nmax * [None]
    main()