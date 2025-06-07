import json
def load_staff():
    with open("data_staff.json", "r") as f:
        return json.load(f)

def validate_staff(staff_list, staff_id):
    for staff in staff_list:
        if staff["id_staff"] == staff_id:
            return staff["nama"]
    return None

def staff_activities():
    print("Aktivitas Staff :")
    print("1. Update buku")
    print("2. Cek buku")
    print("3. Keluar")

    while True:
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            print("Fitur Input Data Buku dipilih.")
        elif pilihan == "2":
            print("Fitur Update Status Buku dipilih.")
        elif pilihan == "3":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")

def main():
    print ("========== Selamat Datang di Perpustakaan Maranatha ==========")
    print ()

    print ("Silahkan pilih peran Anda : ")
    print ("1. Staff Perpustakaan")
    print ("2. Pengunjung")
    print ("3. Mahasiswa")
    print ()

    who = int(input("Masukan pilihian (1/2/3): "))

    if (who == 1):
        print ("Anda masuk sebagai Staff Perpustakaan")
        staff_list = load_staff()
        staff_id = input("Masukkan ID Staff: ")

        nama = validate_staff(staff_list, staff_id)

        if nama:
            print(f"Selamat datang, {nama}!")
            staff_activities()
        else:
            print("ID Staff tidak ditemukan. Akses ditolak.")

    elif (who == 2):
        print ("Anda masuk sebagai Pengunjung Perpustakaan")
    elif (who == 3):
        print ("Anda masuk sebagai Mahasiswa")
if __name__ == '__main__':    
    main()   