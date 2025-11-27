from math import*

# function tampilan menu
def menu():
    print("=" * 10 + "Kalkulator" + "=" * 10)
    print("1. Tambah(+)")
    print("2. Kurang(-)")
    print("3. Bagi(/)")
    print("4. Sisa Bagi(%)")
    print("5. Kali(*)")
    print("6. Pangkat(**)")
    print("7. Tampilkan Histori")
    print("8. Keluar")

# function untuk operasinya
def operasi(pilihan, angka1, angka2):
    if pilihan == "1":
        hasil = angka1 + angka2
        operasistr = f"{angka1} + {angka2} = {hasil}"
    elif pilihan == "2":
        hasil = angka1 - angka2
        operasistr = f"{angka1} - {angka2} = {hasil}"
    elif pilihan == "3":
        if angka2 != 0:
            hasil = angka1 / angka2
            operasistr = f"{angka1} : {angka2} = {hasil}"
    elif pilihan == "4":
        if angka2 != 0:
            hasil = angka1 % angka2
            operasistr = f"{angka1} % {angka2} = {hasil}" 
    elif pilihan == "5":
        hasil = angka1 * angka2
        operasistr = f"{angka1} x {angka2} = {hasil}"
    elif pilihan == "6":
        hasil = angka1 ** angka2
        operasistr = f"{angka1} ^ {angka2} = {hasil}"
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
        menu()
        pilihan = input("Pilih menu(1-8): ")
    
        if pilihan == "8":
            print("Anda keluar")
            break
        
        elif pilihan == "7":
            show_history(history_operasi)
            continue 
        elif pilihan in ("1", "2", "3", "4", "5", "6"):
            while True:
                iptangka1 = input("Masukkan angka pertama: ")
                try:
                    angka1 = int(iptangka1)
                    break
                except ValueError:
                    print("HANYA ANGKA!")
                    continue
            
            while True:
                iptangka2 = input("Masukkan angka kedua: ")
                try:
                    angka2 = int(iptangka2)
                    
                    if pilihan in ("3", "4") and angka2 == 0:
                        print("Tidak bisa dibagi dengan 0")
                        continue
                    break
                except ValueError:
                    print("PASTIKAN HANYA ANGKA!")
                    continue
            
            # perhitungan
            operasistr, hasil = operasi(pilihan, angka1, angka2)
            
            if hasil != None:
                print(f"Hasilnya: {operasistr}")
                # simpan kedalam list(history_operasi)
                history_operasi.append(operasistr)
            
            # looping untuk ingin lagi atau tidak
            while True:
                tanya = input("Ingin lagi? (y/n): ").lower()
                
                if tanya == "n":
                    print("Terimakasih, sampai jumpa!")
                    return
                elif tanya == "y":
                    break
                else:
                    print("Masukkan huruf y/n saja!")
        else:
            print("Silahkan masukkan menu dari angka 1-7")
            
# panggil function kalkulator untuk memulai program
kalkulator()   