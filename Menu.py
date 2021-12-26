from PersegiPanjang import PersegiPanjang
from Segitiga import Segitiga


def Menu() :
    print("----------Menu----------")
    bangun_datar = ["Persegi panjang", "Segitiga"]
    i = 1
    for bd in bangun_datar :
        print(f"{i}. {bd}")
        i = i+1
    


Menu()
