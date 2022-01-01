def Main() :
    print(10*"-"+"Menu"+"-"*10)
    bangun_datar = ["Persegi panjang", "Segitiga"]
    i = 1

    for bd in bangun_datar :
        print(f"{i}. {bd}")
        i = i+1

    print("0. Keluar")

    pilih = input("Pilih bangun datar : ")

    if pilih  != "" :
        
        if pilih.casefold() == "persegipanjang"  or pilih == "1" :
            from PersegiPanjang import PersegiPanjang
            PersegiPanjang()
        
        elif pilih.casefold() == "segitiga"  or pilih == "2" :
            from Segitiga import Segitiga
            Segitiga()

        elif pilih.casefold() == "keluar"  or pilih == "0" :
            Keluar()

        else :
            print("\nMaaf, tidak ada dalam aplikasi kami\n")
            Main()
    
    else :
        print("\nTidak boleh kosong!\n")
        Main()

def Keluar() :
    keluar = input("""Apakah anda mau keluar dari aplikasi ini?
    1. Ya | 2. Tidak
    """)

    if keluar  != "" :
        
        if keluar.casefold() == "ya"  or keluar == "1" :
            print("\nTerima Kasih :-)\n")
            exit()

        elif keluar.casefold() == "tidak"  or keluar == "2" :
            print("\nKembali ke Main utama\n")
            Main()
        
        else :
            print("\nHarus Memilih salah satu dari di atas!\n")
            Keluar()
    
    else :
        print("\nTidak boleh kosong!\n")
        Keluar()

Main()
