def UlangLuas() :
    ulang = input("""Apakah anda mau menghitung ulang lagi?
    1. Ya | 2. Tidak
    3. Menghitung keliling dengan sisi : keliling
    4. Menghitung tinggi dengan luas dan alas : tinggi
    5. Menghitung alas dengan luas dan tinggi : alas
    6. Menghitung sisi segitiga dengan keliling : sisi
    """)

    if ulang  != "" :
        
        if ulang.casefold() == "ya" or ulang == "1" :
            HitungLuasSegitiga()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "keliling" or ulang == "3" :
            HitungKelilingSegitiga()

        elif ulang.casefold() == "tinggi" or ulang == "4" :
            HitungTinggidariLuas()

        elif ulang.casefold() == "alas" or ulang == "5" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "sisi" or ulang == "6" :
            HitungSisidariKeliling()

        else :
            print("\nHarus memilih salah satu yang ada di atas!\n")
            UlangLuas()

    else :
        print("\nTidak boleh kosong!\n")
        UlangLuas()

def UlangKeliling() :
    ulang = input("""Apakah anda mau menghitung ulang lagi?
    1. Ya | 2. Tidak
    3. Menghitung luas dengan alas dan tinggi : luas
    4. Menghitung tinggi dengan luas dan alas : tinggi
    5. Menghitung alas dengan luas dan tingii : alas
    6. Menghitung sisi segitiga dengan keliling : sisi
    """)

    if ulang  != "" :

        if ulang.casefold() == "ya" or ulang == "1" :
            HitungKelilingSegitiga()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "luas" or ulang == "3" :
            HitungLuasSegitiga()

        elif ulang.casefold() == "tinggi" or ulang == "4" :
            HitungTinggidariLuas()

        elif ulang.casefold() == "alas" or ulang == "5" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "sisi" or ulang == "6" :
            HitungSisidariKeliling()

        else :
            print("\nHarus memilih salah satu yang ada di atas!\n")
            UlangKeliling()

    else :
        print("\nTidak boleh kosong!\n")
        UlangKeliling()

def HitungLuasSegitiga() :
    inputAlas = input("\nMasukan alas : ")
    inputTinggi = input("Masukan tinggi : ")

    if inputAlas != '' and inputTinggi != '' :
        
        if inputAlas.isdigit() and inputTinggi.isdigit() :
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
        print("\nKeduanya tidak boleh kosong!\n")
        HitungLuasSegitiga()

def HitungKelilingSegitiga() :
    segitiga = PilihSegitiga()

    if segitiga == "sisi" :
        salah = True

        while salah:
            inputSisi = input("Masukan 3 sisi yang sama : ")

            if inputSisi != '' :
                
                if inputSisi.isdigit() :
                    sisi = int(inputSisi)
                    
                    if sisi  != 0 :
                        print(f"Keliling = sisi + sisi + sisi\nKeliling = {sisi} + {sisi} + {sisi}")
                        print(f"Kelilingnya adalah = {sisi * 3}")
                        salah = False
                        UlangKeliling()

                    else :
                        print("\nSisi tidak boleh sam dengan 0!\n")
                        salah = True
                
                else :
                    print("\nSisi harus menggunakan bilangan bulat!\n")
                    salah = True
            
            else :
                print("\nSisinya tidak boleh kosong!\n")
                salah = True

    elif segitiga == "kaki" :
        salah = True

        while salah:
            inputSisi = input("Masukan 2 sisi  yang sama : ")
            inputBeda = input("Masukan 1 sisi yang berbeda : ")

            if inputSisi != '' and inputBeda != '' :
                
                if inputSisi.isdigit() and inputBeda.isdigit() :
                    sisi = int(inputSisi)
                    beda = int(inputBeda)
                    
                    if sisi  != 0 and beda != 0 :
                        print(f"Keliling = sisi + sisi + sisi\nKeliling = {sisi} + {sisi} + {beda}")
                        print(f"Kelilingnya adalah = {(sisi * 2) + beda}")
                        salah = False
                        UlangKeliling()

                    else :
                        print("\nKedua sisinya tidak boleh sama dengan 0!\n")
                        salah = True
                
                else :
                    print("\nKedua sisinya harus menggunakan bilangan bulat!\n")
                    salah = True
            
            else :
                print("\nKedua sisinya tidak boleh kosong!\n")
                salah = True

    elif segitiga == "sembarang" :
        salah = True

        while salah :
            inputSatu = input("Masukan sisi yang pertama :")
            inputDua = input("Masukan sisi yang kedua : ")
            inputTiga = input("Masukan sisi yang ketiga :")


            if inputSatu != '' and inputDua != '' and inputTiga != '' :
                
                if inputSatu.isdigit() and inputDua.isdigit() and inputTiga.isdigit():
                    satu = int(inputSatu)
                    dua = int(inputDua)
                    tiga = int(inputTiga)
                    
                    if satu  != 0 and dua != 0 and tiga != 0 :
                        print(f"Keliling = sisi + sisi + sisi\nKeliling = {satu} + {dua} + {tiga}")
                        print(f"Kelilingnya adalah = {satu + dua + tiga}")
                        salah = False
                        UlangKeliling()

                    else :
                        print("\nKetiga sisinya tidak boleh sama dengan 0!\n")
                        salah = True
                
                else :
                    print("\nKetiga sisinya harus menggunakan bilangan bulat!\n")
                    salah = True
            
            else :
                print("\nKetiga sisinya tidak boleh kosong!\n")
                salah = True

    else :
        PilihSegitiga()

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
        print("\nTidak boleh kosong!\n")
        PilihSegitiga()

def Segitiga() :
    print(10*"-"+"Segitiga"+"-"*10)
    pilih = input("""Menghitung luas dan keliling segitiga
    1. Luas | 2. Keliling
    """)

    if pilih  != "" :

        if pilih.casefold() == "luas" or pilih == "1" :
            Luas()

        elif pilih.casefold() == "keliling" or pilih == "2" :
            Keliling()

        else :
            print("\nHarus memilih salah satu dari di atas!\n")
            Segitiga()

    else :
        print("\nTidak boleh kosong!\n")
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
        print("\nTidak boleh kosong!\n")
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
        print("\nTidak boleh kosong!\n")  
        Keliling()  

def HitungAlasdariLuas() :
    inputLuas = input("\nMasukan Luas : ")
    inputTinggi = input("Masukan Tinggi : ")

    if inputLuas != "" and inputTinggi != "" :

        if inputLuas.isdigit() and inputTinggi.isdigit() :
            luas = int(inputLuas) 
            tinggi = int(inputTinggi)

            if luas != 0 and tinggi != 0 :
                
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
        print("\nKeduanya tidak boleh kosong!\n")
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
        print("\nTidak boleh kosong!\n")
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
    ulang = input("""Apakah anda mau menghitung ulang lagi?
    1. Ya
    2. Tidak
    3. Menghitung luas segitiga dengan alas dan tinggi yang baru? : luas
    4. Menghitung keliling segitiga? : keliling
    5. Menghitung tinggi dengan luas dan alas yang baru? : tinggi
    6. Menghitung sisi dengan keliling? : sisi
    """)

    if ulang != "" :
        
        if ulang.casefold() == "ya" or ulang  == "1" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            from Menu import Main
            Main()
        
        elif ulang.casefold() == "luas" or ulang == "3" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "keliling" or ulang == "4" :
            HitungKelilingSegitiga()

        elif ulang.casefold() == "tinggi" or ulang == "5" :
            HitungTinggidariLuas()

        elif ulang.casefold() == "sisi" or ulang == "6" :
            HitungSisidariKeliling()

        else :
            print("\nHarus memilih salah satu yang ada di atas!\n")
            UlangAlasdariLuas()

    else :
        print("\nTidak boleh kosong!\n")
        UlangAlasdariLuas()                

def UlangTinggidariLuas() :
    ulang = input("""Apakah anda mau menghitung ulang lagi?
    1. Ya
    2. Tidak
    3. Menghitung luas segitiga dengan alas dan tinggi yang baru? : luas
    4. Menghitung keliling segitiga? : keliling
    5. Menghitung alas dengan luas dan tinggi yang baru? : alas
    6. Menghitung sisi dengan keliling? : sisi
    """)

    if ulang != "" :
        
        if ulang.casefold() == "ya" or ulang  == "1" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            from Menu import Main
            Main()
        
        elif ulang.casefold() == "luas" or ulang == "3" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "keliling" or ulang == "4" :
            HitungKelilingSegitiga()

        elif ulang.casefold() == "alas" or ulang == "5" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "sisi" or ulang == "6" :
            HitungSisidariKeliling()

        else :
            print("\nHarus memilih salah satu yang ada di atas!\n")
            UlangTinggidariLuas()

    else :
        print("\nTidak boleh kosong!\n")
        UlangTinggidariLuas() 

def UlangSisidariKeliling() :
    ulang = input("""Apakah anda mau menghitung ulang lagi?
    1. Ya
    2. Tidak
    3. Menghitung luas segitiga dengan alas dan tinggi yang baru? : luas
    4. Menghitung keliling segitiga? : keliling
    5. Menghitung tinggi dengan luas dan alas yang baru? : tinggi
    6. Menghitung alas dengan luas dan tinggi yang baru? : alas
    """)

    if ulang != "" :
        
        if ulang.casefold() == "ya" or ulang  == "1" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            from Menu import Main
            Main()
        
        elif ulang.casefold() == "luas" or ulang == "3" :
            HitungAlasdariLuas()

        elif ulang.casefold() == "keliling" or ulang == "4" :
            HitungKelilingSegitiga()

        elif ulang.casefold() == "tinggi" or ulang == "5" :
            HitungTinggidariLuas()

        elif ulang.casefold() == "alas" or ulang == "6" :
            HitungAlasdariLuas()

        else :
            print("\nHarus memilih salah satu yang ada di atas!\n")
            UlangSisidariKeliling()

    else :
        print("\nTidak boleh kosong!\n")
        UlangSisidariKeliling() 

def SisiSegitigasamaSisi() :
    inputKeliling = input("\nMasukan keliling : ")

    if inputKeliling  != "" :
        
        if inputKeliling.isdigit() :
            keliling = int(inputKeliling)

            if keliling  != 0 :
                print(f"Sisi segitiga sama sisi = keliling / 3\nSisi = {keliling} / 3")
                print(f"Sisinya adalah = {keliling / 3}")
                UlangSisidariKeliling()

            else :
                print("\nKeliling tidak boleh sama dengan 0!\n")
                SisiSegitigasamaSisi()
        
        else :
            print("\nKeliling harus menggunakan bilangan bulat!\n")
            SisiSegitigasamaSisi()
    
    else :
        print("\nKeliling tidak boleh kosong!\n")
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
        print("\nTidak boleh kosong!\n")
        SisiSegitigasamaKaki()

def SisiSegitigaSembarang() :
    pilih = input("""
    1. Menghitung sisi yang terpanjang? : panjang
    2. Menghitung sisi yang sedang? : sedang
    3. Menghitung sisi yang terpendek? : pendek
    """)

    if pilih != "" :
        
        if pilih.casefold() == "panjang"  or pilih == "1" :
            SisiPanjang()

        elif pilih.casefold() == "sedang" or pilih == "2" :
            SisiSedang()
            
        elif pilih.casefold() == "pendek" or pilih == "3" :
            SisiPendek()

        else :
            print("\nHarus memilih salah satu yang ada di atas!\n")
            SisiSegitigaSembarang()

    else :
        print("\nTidak boleh kosong!\n")
        SisiSegitigaSembarang()

def SisiSama() :
    inputKeliling = input("\nMasukan keliling : ")
    inputSisi = input("Masukan 1 Sisi yang berbeda : ")

    if inputKeliling  != "" and inputSisi  != "" :
        
        if inputKeliling.isdigit() and inputSisi.isdigit() :
            keliling = int(inputKeliling)
            sisi = int(inputSisi)

            if keliling  != 0 and sisi  != 0 :
                
                if keliling  > sisi :
                    print(f"Sisi segitiga sama kaki = (keliling - sisi yang berbeda) / 2\nSisi = ({keliling} - {sisi}) / 2\n")
                    print(f"Sisi = {(keliling - sisi) / 2}")
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
        print("\nKeduanya tidak boleh kosong!\n")
        SisiSama()

def SisiBeda() :
    pilih = input("""
    1. Menghitung dengan memasukan keliling dan salah satu dari sisi yang sama? : satu
    2. Menghitung dengan memasukan keliling dan dua sisi yang sama? : dua
    """)

    if pilih  != "" :
        
        if pilih.casefold() == "satu" or pilih == "1" :
            salah = True

            while salah :
                inputKeliling = input("\nMasukan keliling : ")
                inputSisi = input("Masukan salah satu dari sisi yang sama : ")

                if inputKeliling  != "" and inputSisi  != "" :
                    
                    if inputKeliling.isdigit() and inputSisi.isdigit() :
                        keliling = int(inputKeliling)
                        sisi = int(inputSisi)

                        if keliling  != 0 and sisi  != 0 :
                            
                            if keliling  > sisi :
                                print(f"Sisi yang berbeda = keliling - sisi sama kaki * 2\nSisi = {keliling} - {sisi} * 2")
                                print(f"Sisinya adalah = {keliling - sisi * 2}")
                                salah = False
                                UlangSisidariKeliling()

                            else :
                                print("\nKeliling harus lebih besar dari sisi!\n")
                                salah = True

                        else :
                            print("\nKeduanya tidak boleh sama dengan 0!\n")
                            salah = True
                    
                    else :
                        print("\nKeduanya harus menggunakan bilangan bulat!\n")
                        salah = True

                else :
                    print("\nKeduanya tidak boleh kosong!\n")
                    salah = True    
        
        elif pilih.casefold() == "dua" or pilih == "2" :
            salah = True

            while salah :
                inputKeliling = input("\nMasukan keliling : ")
                inputSisi = input("Masukan total dari kedua sisi yang sama : ")

                if inputKeliling  != "" and inputSisi  != "" :
                    
                    if inputKeliling.isdigit() and inputSisi.isdigit() :
                        keliling = int(inputKeliling)
                        sisi = int(inputSisi)

                        if keliling  != 0 and sisi  != 0 :
                            
                            if keliling  > sisi :
                                print(f"Sisi yang berbeda = keliling - sisi\nSisi = {keliling} - {sisi}")
                                print(f"Sisinya adalah = {keliling - sisi}")
                                salah = False
                                UlangSisidariKeliling()
                            
                            else :
                                print("\nKeliling harus lebih besar dari sisi!\n")
                                salah = True
                        
                        else :
                            print("\nKeduanya tidak boleh sama dengan 0!\n")
                            salah = True
                    
                    else :
                        print("\nKeduanya harus menggunakan bilangan bulat!\n")
                        salah = True

                else :
                    print("\nKeduanya tidak boleh kosong!\n")
                    salah = True

        else :
            print("\nHarus memilih salah satu yang ada di Atas\n")
            SisiBeda()
    else :
        print("\nTidak boleh kosong!\n")
        SisiBeda()

def SisiPanjang() :
    inputKeliling = input("\nMasukan keliling : ")
    inputPendek = input("Masukan sisi yang terpendek : ")
    inputSedang = input("Masukan sisi yang sedang : ")

    if inputKeliling != "" and inputPendek != "" and inputSedang != "" :
       
        if inputKeliling.isdigit() and inputPendek.isdigit() and inputSedang.isdigit() :
            keliling = int(inputKeliling)
            pendek = int(inputPendek)
            sedang = input(inputSedang)

            if keliling != 0 and pendek != 0 and sedang != 0 :
                salah = True
                
                while salah:
                    
                    if keliling > pendek and keliling > sedang :

                        if sedang > pendek :
                            print(f"Sisi yang terpanjang = keliling - (pendek + sedang)\nSisi = {keliling} - ({pendek} + {sedang})")
                            print(f"Sisinya adalah = {keliling - (pendek + sedang)}")
                            salah = False
                            UlangSisidariKeliling()

                        else :
                            print(f"Sisi yang sedang harus lebih besar daripada sisi yang pendek = {pendek} dan harus kurang dari keliling = {keliling}")
                            inputSedang = input("\nMasukan sisi yang sedang : ")
                            salah = True
                            salah1 = True

                            while salah1 :

                                if inputSedang != "" :
                                    
                                    if inputSedang.isdigit() :
                                        sedang = int(inputSedang)

                                        if sedang != 0 :
                                            salah1 = False
                                        
                                        else :
                                            print("\nTidak boleh sama dengan 0!\n")
                                            salah1 = True
                                    
                                    else :
                                        print("\nHarus menggunakan bilangan bulat!\n")
                                        salah1 = True
                                
                                else :
                                    print("\nTidak boleh kosong!\n")
                                    salah1 = True

                    else :
                        print("\nKeliling harus lebiih besar dari sisi yang pendek dan sisi yang sedang!\n")
                        salah = False
                        SisiPanjang()

            else :
                print("\nKetiganya tidak boleh sama dengan 0!\n")
                SisiPanjang()

        else :
            print("\nKetiganya harus menggunakan bilangan bulat!\n")
            SisiPanjang()

    else :
        print("\nKetiganya tidak boleh sama dengan 0!\n")
        SisiPanjang()

def SisiPendek() :
    inputKeliling = input("\nMasukan keliling : ")
    inputPanjang = input("Masukan sisi yang terpanjang : ")
    inputSedang = input("Masukan sisi yang sedang : ")

    if inputKeliling != "" and inputPanjang != "" and inputSedang != "" :
        
        if inputKeliling.isdigit() and inputPanjang.isdigit() and inputSedang.isdigit() :
            keliling = int(inputKeliling)
            panjang = int(inputPanjang)
            sedang = int(inputSedang)

            if keliling != 0 and panjang != 0 and sedang != 0 :
                salah = True

                while salah:
                    
                    if keliling > panjang and keliling > sedang :
                        
                        if panjang > sedang :
                            print(f"Sisi yang terpendek = keliling - (panjang + sedang)\nSisi = {keliling} - ({panjang} + {sedang})")
                            print(f"Sisi = {keliling - (panjang + sedang)}")
                            salah = False
                            UlangSisidariKeliling()
                        
                        else :
                            print(f"\nSisi yang sedang harus lebih kecil daripada sisi yang panjang = {panjang} dan keliling = {keliling}\n")
                            inputSedang = input("\nMasukan sisi yang sedang : ")
                            salah = True
                            salah1 = True

                            while salah1 :

                                if inputSedang != "" :
                                    
                                    if inputSedang.isdigit() :
                                        sedang = int(inputSedang)

                                        if sedang != 0 :
                                            salah1 = False
                                        
                                        else :
                                            print("\nTidak boleh sama dengan 0!\n")
                                            salah1 = True
                                    
                                    else :
                                        print("\nHarus menggunakan bilangan bulat!\n")
                                        salah1 = True
                                
                                else :
                                    print("\nTidak boleh kosong!\n")
                                    salah1 = True

                    else :
                        print("\nKeliling harus lebih besar dari sisi yang panjang dan sisi yang sedang!\n")
                        SisiPendek()

            else :
                print("\nKetiganya Tidak boleh sama dengan 0!\n")
                SisiPendek()

        else :
            print("\nKetiganya harus menggunakan bilangan bulat!\n")
            SisiPendek()

    else :
        print("\nKetiganya tidak boleh kosong!\n")
        SisiPendek()

def SisiSedang() :
    inputKeliling = input("\nMasukan keliling : ")
    inputPanjang = input("Masukan sisi yang terpanjang : ")
    inputPendek = input("Masukan sisi yang sedang : ")

    if inputKeliling != "" and inputPanjang != "" and inputPendek != "" :
        
        if inputKeliling.isdigit() and inputPanjang.isdigit() and inputPendek.isdigit() :
            keliling = int(inputKeliling)
            panjang = int(inputPanjang)
            pendek = int(inputPendek)

            if keliling != 0 and panjang != 0 and pendek != 0 :
                salah = True

                while salah:
                    
                    if keliling > panjang and keliling > pendek :
                        
                        if panjang > pendek :
                            print(f"Sisi yang terpendek = keliling - (panjang + pendek)\nSisi = {keliling} - ({panjang} + {pendek})")
                            print(f"Sisi = {keliling - (panjang + pendek)}")
                            salah = False
                            UlangSisidariKeliling()
                        
                        else :
                            print(f"\nSisi yang pendek harus lebih kecil daripada sisi yang panjang = {panjang} dan keliling = {keliling}\n")
                            inputPendek = input("\nMasukan sisi yang pendek : ")
                            salah = True
                            salah1 = True

                            while salah1 :

                                if inputPendek != "" :
                                    
                                    if inputPendek.isdigit() :
                                        pendek = int(inputPendek)

                                        if pendek != 0 :
                                            salah1 = False
                                        
                                        else :
                                            print("\nTidak boleh sama dengan 0!\n")
                                            salah1 = True
                                    
                                    else :
                                        print("\nHarus menggunakan bilangan bulat!\n")
                                        salah1 = True
                                
                                else :
                                    print("\nTidak boleh kosong!\n")
                                    salah1 = True

                    else :
                        print("\nKeliling harus lebih besar dari sisi yang panjang dan sisi yang pendek!\n")
                        SisiSedang()

            else :
                print("\nKetiganya Tidak boleh sama dengan 0!\n")
                SisiSedang()

        else :
            print("\nKetiganya harus menggunakan bilangan bulat!\n")
            SisiSedang()

    else :
        print("\nKetiganya tidak boleh kosong!\n")
        SisiSedang()

