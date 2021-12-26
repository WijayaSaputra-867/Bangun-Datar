def UlangLuas() :
    ulang = input("""Apakah anda mau menghitung ulang lagi?
    1. Ya | 2. Tidak
    3. Menghitung keliling dengan sisi : keliling
    """)

    if ulang.casefold() == "ya" or ulang == "1" :
        HitungLuasSegitiga()

    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()

    elif ulang == "keliling" or ulang == "3" :
        HitungKelilingSegitiga()

    else :
        print("\nHarus memilih salah satu yang ada di atas!\n")

def UlangKeliling() :
    ulang = input("""Apakah anda mau menghitung ulang lagi?
    1. Ya | 2. Tidak
    3. Menghitung luas dengan alas dan tinggi : luas
    """)

    if ulang.casefold() == "ya" or ulang == "1" :
        HitungKelilingSegitiga()

    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()

    elif ulang == "luas" or ulang == "3" :
        HitungLuasSegitiga()

    else :
        print("\nHarus memilih salah satu yang ada di atas!\n")

def HitungLuasSegitiga() :
    inputAlas = input("\nMasukan alas : ")
    inputTinggi = input("Masukan tinggi : ")

    if inputAlas != '' and inputTinggi != '' :
        
        if inputAlas.isdigit() & inputTinggi.isdigit() :
            alas = int(inputAlas)
            tinggi = int(inputTinggi)

            if alas != 0 and tinggi != 0 :
               luas = int(alas * tinggi * 0.5)
               print(f"Luas = ½ * alas * tinggi\nLuas = ½ * {alas} * {tinggi}")
               print(f"Luasnya adalah = {luas}")
               UlangLuas()

            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungLuasSegitiga()

        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            HitungLuasSegitiga()

    else :
        print("\nKeduanya harus di isi!\n")
        HitungLuasSegitiga()

def HitungKelilingSegitiga() :
    segitiga = PilihSegitiga()

    if segitiga == "sisi" :
        inputSisi = input("Masukan 3 sisi yang sama : ")

        if inputSisi != '' :
            
            if inputSisi.isdigit() :
                sisi = int(inputSisi)
                
                if sisi  != 0 :
                    keliling = sisi * 3
                    print(f"Keliling = sisi + sisi + sisi\nKeliling = {sisi} + {sisi} + {sisi}")
                    print(f"Kelilingnya adalah = {keliling}")
                    UlangKeliling()

                else :
                    print("\nSisi tidak boleh sam dengan 0!\n")
                    HitungKelilingSegitiga()
            
            else :
                print("\nSisi harus menggunakan bilangan bulat!\n")
                HitungKelilingSegitiga()
        
        else :
            print("\nSisi tidak boleh kosong!\n")
            HitungKelilingSegitiga()

    elif segitiga == "kaki" :
        inputSisi = input("Masukan 2 sisi  yang sama : ")
        inputBeda = input("Masukan 1 sisi yang berbeda : ")

        if inputSisi != '' and inputBeda != '' :
            
            if inputSisi.isdigit() & inputBeda.isdigit() :
                sisi = int(inputSisi)
                beda = int(inputBeda)
                
                if sisi  != 0 & beda != 0 :
                    keliling = (sisi * 2) + beda
                    print(f"Keliling = sisi + sisi + sisi\nKeliling = {sisi} + {sisi} + {beda}")
                    print(f"Kelilingnya adalah = {keliling}")
                    UlangKeliling()

                else :
                    print("\nKedua sisinya tidak boleh sama dengan 0!\n")
                    HitungKelilingSegitiga()
            
            else :
                print("\nkedua sisinya harus menggunakan bilangan bulat!\n")
                HitungKelilingSegitiga()
        
        else :
            print("\nKedua sisinya tidak boleh kosong!\n")
            HitungKelilingSegitiga()

    elif segitiga == "sembarang" :
        inputSatu = input("Masukan sisi yang pertama :")
        inputDua = input("Masukan sisi yang kedua : ")
        inputTiga = input("Masukan sisi yang ketiga :")


        if inputSatu != '' and inputDua != '' and inputTiga != '' :
            
            if inputSatu.isdigit() & inputDua.isdigit() & inputTiga.isdigit():
                satu = int(inputSatu)
                dua = int(inputDua)
                tiga = int(inputTiga)
                
                if satu  != 0 & dua != 0 & tiga != 0:
                    keliling = satu + dua + tiga
                    print(f"Keliling = sisi + sisi + sisi\nKeliling = {satu} + {dua} + {tiga}")
                    print(f"Kelilingnya adalah = {keliling}")
                    UlangKeliling()

                else :
                    print("\nKetiga sisinya tidak boleh sama dengan 0!\n")
                    HitungKelilingSegitiga()
            
            else :
                print("\nKetiga sisinya harus menggunakan bilangan bulat!\n")
                HitungKelilingSegitiga()
        
        else :
            print("\nKetiga sisinya tidak boleh kosong!\n")
            HitungKelilingSegitiga()        

def PilihSegitiga() :
    pilih = input("""Pilih segitiga
    1. Segitiga sama sisi : sisi
    2. Segitiga sama kaki : kaki
    3. Segitiga sembarang : sembarang
    """)

    if pilih  != '' :
        
        if pilih == '1' or pilih == "sisi" :
            return "sisi"

        elif pilih == '2' or pilih == "kaki" :
            return "kaki"
            
        elif pilih == '3' or pilih == "sembarang" :
            return "sembarang"

        else :
            print("\nHarus memilih salah satu!\n")
            PilihSegitiga()
    
    else :
        print("\nHarus di isi!\n")
        PilihSegitiga()

def Segitiga() :
    pilih = input("""Menghitung luas dan keliling segitiga
    1. Luas | 2. Keliling
    """)

    if pilih.casefold() == "luas" or pilih == "1" :
        Luas()

    elif pilih.casefold() == "keliling" or pilih == "2" :
        Keliling()

    else :
        print("\nHarus memilih salah satu dari di atas!\n")
        Segitiga()

def Luas() :
    pilih = input("""
    1. Hitung Luas
    2. Hitung Alas
    3. Hitung Tinggi
    """)
    
    if pilih  != "" :
        
        if pilih == "luas" or pilih == "1" :
            HitungLuasSegitiga()

        elif pilih == "alas" or pilih == "2" :
            HitungAlasdariLuas()
        
        elif pilih == "tinggi" or pilih == "3":
            HitungTinggidariLuas()
        
        else :
            print("\nHarus memilih salah satu dari di atas!\n")
            Luas()

    else :
        print("\nHarus di isi!\n")
        Luas()

def Keliling() :
    pilih = input("""
    1. Hitung keliling : keliling
    2. Hitung sisi : sisi
    """)

    if pilih  != "" :
        
        if pilih == "keliling" or pilih == "1" :
            HitungKelilingSegitiga()

        elif pilih == "sisi" or pilih == "2" :
            HitungSisidariKeliling()

        else :
            print("\nHarus memilih salah satu dari di atas!\n")
            Keliling()
        
    else :
        print("\nHarus di isi! \n")  
        Keliling()  

def HitungAlasdariLuas() :
    inputLuas = input("\nMasukan Luas : ")
    inputTinggi = input("Masukan Tinggi : ")

    if inputLuas != "" and inputTinggi != "" :

        if inputLuas.isdigit() & inputTinggi.isdigit() :
            luas = int(inputLuas) 
            tinggi = int(inputTinggi)

            if luas != 0 & tinggi != 0 :
                
                if luas > tinggi :
                    alas = luas / tinggi * 2
                    print(f"Alas = luas / tinggi * 2\nAlas = {luas} / {tinggi} * 2")
                    print(f"Alasnya adalah = {alas}")
                    UlangAlasdariLuas()

                else :
                    print("\nLuas harus lebih besar dari tinggi!\n")
                    HitungAlasdariLuas()
            
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungAlasdariLuas()

        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            HitungAlasdariLuas()

    else :
        print("\nKeduanya harus di isi!\n")
        HitungAlasdariLuas()

def HitungTinggidariLuas() :
    inputLuas = input("\nMasukan Luas : ")
    inputAlas = input("Masukan Alas : ")
    
    if inputLuas  != "" and inputAlas  != "" :

        if inputLuas.isdigit() and inputAlas.isdigit() :
            luas = int(inputLuas)
            alas = int(inputAlas)
        
            if luas  != 0 and alas  != 0 :

                if luas  > alas :
                    tinggi = luas / alas * 2
                    print(f"Tinggi = luas / alas * 2\nTinggi = {luas} / {alas} * 2")
                    print(f"TIngginya adalah = {tinggi}")
                    UlangTinggidariLuas()

                else :
                    print("\nLuas harus lebih besar dari alas!\n")
                    HitungTinggidariLuas()
            
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungTinggidariLuas()
        
        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            HitungTinggidariLuas()
    
    else :
        print("\nKeduanya harus di isi!\n")
        HitungTinggidariLuas()

def HitungSisidariKeliling() :
    segitiga = PilihSegitiga()

    if segitiga == "sisi" :
        SisiSegitigasamaSisi()

    elif segitiga == "kaki" :
        SisiSegitigasamaKaki()

    elif segitiga == "sembarang" :
        SisiSegitigaSembarang()
    
    else :
        PilihSegitiga()

def UlangAlasdariLuas() :
    print("test")

def UlangTinggidariLuas() :
    print("test")

def UlangSisidariKeliling() :
    print("test")

def SisiSegitigasamaSisi() :
    inputKeliling = input("\nMasukan Keliling : ")

    if inputKeliling  != "" :
        
        if inputKeliling.isdigit() :
            keliling = int(inputKeliling)

            if keliling  != 0 :
                sisi = keliling / 3
                print(f"Sisi segitiga sama sisi = keliling / 3\nSisi = {keliling} / 3")
                print(f"Sisinya adalah = {sisi}")
                UlangSisidariKeliling()

            else :
                print("\nKeliling tidak boleh sama dengan 0!\n")
                SisiSegitigasamaSisi()
        
        else :
            print("\nKeliling harus menggunakan bilangan bulat!\n")
            SisiSegitigasamaSisi()
    
    else :
        print("\nKeliling harus di isi!\n")
        SisiSegitigasamaSisi()

def SisiSegitigasamaKaki() :
    pilih = input("""
    1. Menghitung sisi yang sama? : sama
    2. Menghitung sisi yang berbeda? : beda
    """)
    
    if pilih != "" :

        if pilih.casefold() == "sama"  or pilih == "1" :
            SisiSama()

        elif pilih.casefold() == "beda" or pilih == "2" :
            SisiBeda()
        
        else :
            print("\nHarus melilih salah satu yang ada di atas!\n")
            SisiSegitigasamaKaki()
    else :
        print("\nHarus di isi!\n")
        SisiSegitigasamaKaki()

def SisiSegitigaSembarang() :
    print("test")

def SisiSama() :
    inputKeliling = input("\nMasukan Keliling : ")
    inputSisi = input("Masukan 1 Sisi yang berbeda : ")

    if inputKeliling  != "" and inputSisi  != "" :
        
        if inputKeliling.isdigit() and inputSisi.isdigit() :
            keliling = int(inputKeliling)
            sisi = int(inputSisi)

            if keliling  != 0 and sisi  != 0 :
                
                if keliling  > sisi :
                    kaki = (keliling - sisi) / 2
                    print(f"Sisi segitiga sama kaki = (keliling - sisi yang berbeda) / 2\nSisi = ({keliling} - {sisi}) / 2\n")
                    print(f"Sisi = {kaki}")
                    UlangSisidariKeliling()

                else :
                    print("\nKeliling harus lebih besar dari sisi yang berbeda!\n")
                    SisiSama()
            
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                SisiSama()
        
        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            SisiSama()
    
    else :
        print("\nKeduanya harus di isi!\n")
        SisiSama()

def SisiBeda() :
    print("test")

def SisiPanjang() :
    print("test")

def SisiPendek() :
    print("test")

def SisiSedang() :
    print("test")

Segitiga()