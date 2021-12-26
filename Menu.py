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

Menu()
