def data ():
    global Buku, Peminjam, ID_Anggota
    i = 0

    print ("Ketik 9999 untuk selesai !")
    id_buku = int(input("Masukkan ID buku : "))

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
        
        id_buku = int(input("Masukkan ID buku : "))
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