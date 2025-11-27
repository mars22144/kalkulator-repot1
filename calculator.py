from math import*

def clear():
    print("\n" * 30)

# function tampilan menu
def menu():
    print("=" * 10 + "Kalkulator" + "=" * 10)
    print("1. Tambah(+)")
    print("2. Kurang(-)")
    print("3. Bagi(/)")
    print("4. Sisa Bagi(%)")
    print("5. Kali(*)")
    print("6. Pangkat(**)")
    print("7. Akar")
    print("8. Tampilkan Histori")
    print("9. Keluar")

# function untuk operasinya
def operasi(pilihan, angka1, angka2=None):
    # tambah
    if pilihan == "1":
        hasil = angka1 + angka2
        operasistr = f"{angka1} + {angka2} = {hasil}"
    # kurang
    elif pilihan == "2":
        hasil = angka1 - angka2
        operasistr = f"{angka1} - {angka2} = {hasil}"
    # bagi
    elif pilihan == "3":
        # jika angka2 bukan 0 maka akan jalan ini
        if angka2 != 0:
            hasil = angka1 / angka2
            operasistr = f"{angka1} : {angka2} = {hasil}"
    # sisa bagi
    elif pilihan == "4":
        # jika angka2 bukan 0 maka akan jalan ini
        if angka2 != 0:
            hasil = angka1 % angka2
            operasistr = f"{angka1} % {angka2} = {hasil}" 
    # kali
    elif pilihan == "5":
        hasil = angka1 * angka2
        operasistr = f"{angka1} x {angka2} = {hasil}"
    # pangkat
    elif pilihan == "6":
        hasil = pow(angka1, angka2)
        operasistr = f"{angka1} ^ {angka2} = {hasil}"
    elif pilihan == "7":
        if angka1 > 0:
            hasil = sqrt(angka1)
            operasistr = f"Akar dari {angka1} = {hasil}"
        else:
            return "Angka harus positif!", None
    # jika user memasukkan pilihan yang tidak ada
    else:
        return "Pilihan tidak ada", None
    
    return operasistr, hasil

# function untuk menampilkan histori
def show_history(history):
    if not history:
        print("Kosong")
    else:
        print("\n" + "=" * 10 + " History " + "=" * 10)
        # looping untuk menampilkan seluruh history
        for i, entri in enumerate(history, 1):
            print(f"{i}. {entri}")
        print("=" * 10 + " History "  + "=" * 10 + "\n")
        
# function untuk kalkulatornya
def kalkulator():
    history_operasi = []
    # looping pemilihan menu
    while True:
        # memanggil function menu
        menu()
        pilihan = input("Pilih menu(1-9): ")
    
        # jika user memasukkan angka 8 maka akan keluar dari looping
        if pilihan == "9":
            print("Anda keluar")
            break
        # history
        elif pilihan == "8":
            show_history(history_operasi)
            continue # kembali ke loop yang awal(tampilan menu)
        # menu 1 - 7
        elif pilihan in ("1", "2", "3", "4", "5", "6", "7"):    
            while True:
                iptangka1 = input("Masukkan angka pertama: ")
                try:
                    angka1 = int(iptangka1)
                    if pilihan == "8" and angka1 < 0:
                        print("Angka harus positif!")
                        continue
                    break
                except ValueError:
                    print("HANYA ANGKA!")
                    continue # kembali ke loop masukkan angka1 jika inputan bukan angka
            
            if pilihan in ("1", "2", "3", "4", "5", "6"):
                # looping untuk angka2(jika user memasukan 0 di angka2) 
                while True:
                    iptangka2 = input("Masukkan angka kedua: ")
                    try:
                        angka2 = int(iptangka2)
                    
                        if pilihan in ("3", "4") and angka2 == 0:
                            print("Tidak bisa dibagi dengan 0")
                            continue
                        break
                    except ValueError:
                        print("HANYA ANGKA!")
                        continue # kembali ke loop masukkan angka2 jika inputan bukan angka
            else:
                angka2 = None
                    
            # perhitungan
            operasistr, hasil = operasi(pilihan, angka1, angka2)
                        
            # ketika hasil tidak sama dengan None maka akan tampil ini
            if hasil != None:
                print(f"Hasilnya: {operasistr}")
                # simpan kedalam list(history_operasi)
                history_operasi.append(operasistr)
            
            # looping untuk ingin lagi atau tidak
            while True:
                tanya = input("Ingin lagi? (y/n): ").lower()
                
                if tanya == "n":
                    print("Terimakasih, sampai jumpa")
                    return
                elif tanya == "y":
                    break
                else:
                    print("Masukkan huruf y/n saja!")
        else:
            print("Silahkan masukkan menu dari angka 1-9")
            
        clear()
            
# panggil function kalkulator untuk memulai program
kalkulator()   