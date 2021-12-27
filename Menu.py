from PersegiPanjang import PersegiPanjang
from Segitiga import Segitiga


def Menu() :
    print(10*"-"+"Menu"+"-"*10)
    bangun_datar = ["Persegi panjang", "Segitiga"]
    i = 1

    for bd in bangun_datar :
        print(f"{i}. {bd}")
        i = i+1

    pilih = input("Pilih bangun datar : ")

    if pilih  != "" :
        
        if pilih.casefold() == "persegipanjang"  or pilih == "1" :
            PersegiPanjang()
        
        elif pilih.casefold() == "segitiga"  or pilih == "2" :
            Segitiga()

        else :
            print("\nMaaf, tidak ada dalam aplikasi kami\n")
            Menu()
    
    else :
        print("\nTidak boleh kosong\n")
        Menu()

def Keluar() :
    keluar = input("""Apakah anda mau keluar dari aplikasi ini?
    1. Ya | 2. Tidak
    """)

    if keluar  != "" :
        
        if keluar.casefold() == "ya"  or keluar == 1 :
            print("\nTerima Kasih ;-)\n")
            exit()

        elif keluar.casefold() == "tidak"  or keluar == "2" :
            print("\nKembali ke menu utama\n")
            Menu()
        
        else :
            print("\nHarus Memilih salah satu dari di atas!\n")
            Keluar()
    
    else :
        print("\nTidak boleh kosong!\n")
        Keluar()

Menu()
