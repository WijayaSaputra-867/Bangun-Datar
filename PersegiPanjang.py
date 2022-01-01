def UlangLuas(panjang, lebar) :
    ulang = input("""\nApakah anda mau menghitung ulang lagi? 
    1. ya | 2. tidak
    3. Menghitung keliling dari panjang dan lebar yang sama? : sama
    4. Menghitung keliling dari panjang dan lebar yang baru? : baru 
    5. Menghitung panjang dengan luas dan lebar yang baru? : panjang
    6. Menghitung lebar dengan luas dan panjang yang baru? : lebar
    7. Mengihtung panjang dari keliling dan lebar yang berbeda? : beda
    8. Menghitung lebar dari keliling dan panjang yang berbeda? : keliling
    9. Menghitung luas dengan satu yang berbeda? : luas
    10. Menghitung keliling dengan satu yang berbeda? : satu
    """)

    if ulang  != "" :

        if ulang.casefold() == "ya" or ulang == "1" :
            HitungLuasPersegiPanjang()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "sama" or ulang == "3" :
            HitungKelilingdariLuas(panjang, lebar)

        elif ulang.casefold() == "baru" or ulang == "4" :
            HitungKelilingPersegiPanjang()

        elif ulang.casefold() == "panjang" or ulang == "5" :
            HitungPanjangDariLuas()

        elif ulang.casefold() == "lebar" or ulang == "6" :
            HitungLebardariLuas()

        elif ulang.casefold() == "beda" or ulang == "7" :
            HitungPanjangdariKeliling()

        elif ulang.casefold() == "keliling" or ulang == "8" :
            HitungLebardariKeliling()

        elif ulang.casefold() == "luas" or ulang == "9" :
            LuasSatu(panjang, lebar)

        elif ulang.casefold() == "satu" or ulang == "10" :
            KelilingSatu(panjang, lebar)

        else :
            print("\nHarus memilih salah satu yang ada diatas!\n")
            UlangLuas(panjang, lebar)

    else :
        print("\nTidak boleh kosong!\n")
        UlangLuas(panjang, lebar)
       
def UlangKeliling(panjang, lebar) : 
    ulang = input("""\nApakah anda mau menghitung ulang lagi? 
    1. ya | 2. tidak
    3. Menghitung luas dari panjang dan lebar yang sama? : sama
    4. Menghitung luas dari panjang dan lebar yang baru? : baru 
    5. Menghitung panjang dari keliling dan lebar yang baru? : panjang
    6. Menghitung lebar dari keliling dan panjang yang baru? : lebar
    7. Menghitung panjang dari luas dan lebar yang berbeda? : beda
    8. Menghitung lebar dari luas dan panjang yang berbeda? : luas
    9. Menghitung keliling dengan satu yang berbeda? : keliling
    10. Menghitung luas dengan satu yang berbeda? : satu
    """)

    if ulang  != "" :

        if ulang.casefold() == "ya" or ulang == "1":
            HitungKelilingPersegiPanjang()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "sama" or ulang == "3" :
            HitungLuasdariKeliling(panjang, lebar)

        elif ulang.casefold() == "baru" or ulang == "4" :
            HitungLuasPersegiPanjang()

        elif ulang.casefold() == "panjang" or ulang == "5" :
            HitungPanjangdariKeliling()

        elif ulang.casefold() == "lebar" or ulang == "6" :
            HitungLebardariKeliling()

        elif ulang.casefold() == "beda" or ulang == "7" :
            HitungPanjangDariLuas()

        elif ulang.casefold() == "luas" or ulang == "8" :
            HitungLebardariLuas()

        elif ulang.casefold() == "keliling" or ulang == "9" :
            KelilingSatu(panjang, lebar)

        elif ulang.casefold() == "satu" or ulang == "10" :
            LuasSatu(panjang, lebar)

        else :
            print("\nHarus memilih salah satu yang ada diatas!\n")
            UlangKeliling(panjang, lebar)

    else :
        print("\nTidak boleh kosong!\n")
        UlangKeliling(panjang, lebar)
            
def HitungLuasPersegiPanjang() :
    inputPanjang = input("\nMasukan Panjang : ")
    inputLebar = input("Masukan Lebar : ")

    if inputPanjang  != "" and inputLebar  != "" :
        
        if inputPanjang.isdigit() and inputLebar.isdigit() :
            panjang = int(inputPanjang)
            lebar = int(inputLebar)

            if panjang  != 0 and lebar  != 0 :
                
                if panjang > lebar :
                    luas = panjang * lebar
                    print(f"Luas = Panjang * Lebar\nLuas = {panjang} * {lebar}")
                    print(f"Luasnya adalah = {luas}")
                    UlangLuas(panjang, lebar)

                else :
                    print("\nPanjang harus Lebih besar dari lebar!\n")
                    salah = True

                    while salah :
                        pilih = input("""
                        1. Memasukan ulang? : ulang
                        2. Mengubah panjang? : panjang
                        3. Mengubah lebar : lebar
                        """)

                        if pilih  != "" :
                            
                            if pilih.casefold() == "ulang"  or pilih == "1" :
                                salah = False
                                HitungLuasPersegiPanjang()

                            elif pilih.casefold() == "panjang"  or pilih == "2" :
                                salah = False
                                LuastanpaPanjang(lebar)

                            elif pilih.casefold() == "lebar" or pilih == "3" :
                                salah = False
                                LuastanpaLebar(panjang)
                            
                            else :
                                print("\nHarus memilih salah satu yang ada di atas!\n")
                                salah = True
                        
                        else :
                            print("\nTidak boleh kosong!\n")
                            salah = True
            
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungLuasPersegiPanjang()

        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            HitungLuasPersegiPanjang()

    else :
        print("\nKeduanya tidak boleh kosong!\n")
        HitungLuasPersegiPanjang()

def HitungKelilingPersegiPanjang() :
    inputPanjang = input("\nMasukan Panjang : ")
    inputLebar = input("Masukan Lebar : ")

    if inputPanjang  != "" and inputLebar  != "" :
        
        if inputPanjang.isdigit() and inputLebar.isdigit() :
            panjang = int(inputPanjang)
            lebar = int(inputLebar)

            if panjang  != 0 and lebar  != 0 :
                
                if panjang > lebar :
                    keliling = (panjang + lebar) * 2
                    print(f"Keliling = (Panjang + Lebar) * 2\nKeliling = ( {panjang} +  {lebar}) * 2")
                    print(f"Kelilingnya adalah = {keliling}")
                    UlangKeliling(panjang, lebar)

                else :
                    print("\nPanjang harus Lebih besar dari lebar!\n")
                    salah = True

                    while salah :
                        pilih = input("""
                        1. Memasukan ulang? : ulang
                        2. Mengubah panjang? : panjang
                        3. Mengubah lebar? : lebar
                        """)

                        if pilih  != "" :
                            
                            if pilih.casefold() == "ulang"  or pilih == "1" :
                                salah = False
                                HitungKelilingPersegiPanjang()

                            elif pilih.casefold() == "panjang"  or pilih == "2" :
                                salah = False
                                KelilingtanpaPanjang(lebar)  

                            elif pilih.casefold() == "lebar"  or pilih == "3" :
                                salah = False
                                KelilingtanpaLebar(panjang)

                            else :
                                print("\nHarus memilih salah satu yang ada di atas!\n")
                                salah = True

                        else :
                            print("\nTidak boleh kosong!\n")
                            salah = True                              
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungKelilingPersegiPanjang()

        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            HitungKelilingPersegiPanjang()

    else :
        print("\nKeduanya tidak boleh kosong!\n")
        HitungKelilingPersegiPanjang()

def HitungKelilingdariLuas(panjang, lebar) :
    keliling = (panjang + lebar) * 2
    print(f"Keliling = (Panjang + Lebar) * 2\nKeliling = ({panjang} + {lebar}) * 2")
    print(f"Kelilingnya adalah = {keliling}")
    UlangKeliling(panjang, lebar)

def HitungLuasdariKeliling(panjang, lebar) :
    luas = panjang * lebar
    print(f"Luas = Panjang * Lebar\nLuas = {panjang} * {lebar}")
    print(f"Luasnya adalah = {luas}")
    UlangLuas(panjang, lebar)

def HitungPanjangDariLuas() :
    inputLuas = input("\nMasukan Luas : ")
    inputLebar = input("Masukan Lebar : ")

    if inputLuas  != "" and inputLebar  != "" :
        
        if inputLuas.isdigit() and inputLebar.isdigit() :
            luas = int(inputLuas)
            lebar = int(inputLebar)

            if luas  != 0 and lebar  != 0 :
                
                if luas > lebar :
                    panjang = luas / lebar
                    print(f"Panjang = luas / lebar\nPanjang = {luas} / {lebar}")
                    print(f"Panjangnya adalah = {panjang}")
                    UlangPanjangdariLuas(panjang, lebar)

                else :
                    print("\nLuas harus lebih besar dari lebar!\n")
                    HitungPanjangDariLuas()
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungPanjangDariLuas()

        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            HitungPanjangDariLuas()

    else :
        print("\nKeduanya tidak boleh kosong!\n")
        HitungPanjangDariLuas()

def HitungLebardariLuas() :
    inputLuas = input("\nMasukan Luas : ")
    inputPanjang = input("Masukan Panjang : ")

    if inputLuas  != "" and inputPanjang  != "" :
        
        if inputLuas.isdigit() and inputPanjang.isdigit() :
            luas = int(inputLuas)
            panjang = int(inputPanjang)

            if luas  != 0 and panjang  != 0 :
                
                if luas > panjang :
                    lebar = luas / panjang
                    print(f"Lebar = luas / lebar\nLebar = {luas} / {panjang}")
                    print(f"Lebarnya adalah = {lebar}")
                    UlangLebardariLuas()

                else :
                    print("\nLuas harus lebih besar dari panjang!\n")
                    HitungLebardariLuas()
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungLebardariLuas()

        else :
            print("\nKeduanya harus menggunakan bilangan bulat!\n")
            HitungLebardariLuas()

    else :
        print("\nKeduanya tidak boleh kosong!\n")
        HitungLebardariLuas()

def HitungPanjangdariKeliling() :
    inputKeliling = input("\nMasukan Keliling : ")
    inputLebar = input("Masukan Lebar : ")

    if inputKeliling  != "" and inputLebar  != "" :
        
        if inputKeliling.isdigit() and inputLebar.isdigit() :
            keliling = int(inputKeliling)
            lebar = int(inputLebar)
            
            if keliling  != 0 and lebar  != 0 :
                
                if keliling > lebar :
                    panjang = (keliling / 2) - lebar
                    print(f"Panjang = (keliling / 2) - lebar\nPanjang = ({keliling}  / 2) - {lebar}")
                    print(f"Panjangnya adalah = {panjang}")
                    UlangPanjangdariKeliling(panjang , lebar)

                else :
                    print("\nKeliling harus lebih besar dari lebar!\n")
                    HitungPanjangdariKeliling()

            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungPanjangdariKeliling()

        else :
            print("\nHarus menggunakan bilangan bulat!\n")
            HitungPanjangdariKeliling()

    else :
        print("\nKeduanya tidak boleh kosong!\n")
        HitungPanjangdariKeliling()

def HitungLebardariKeliling() :
    inputKeliling = input("\nMasukan Keliling : ")
    inputPanjang = input("Masukan Panjang : ")

    if inputKeliling  != "" and inputPanjang  != "" :
        
        if inputKeliling.isdigit() and inputPanjang.isdigit() :
            keliling = int(inputKeliling)
            panjang = int(inputPanjang)

            if keliling  != 0 and panjang  != 0 :
                
                if keliling > panjang :
                    lebar = (keliling / 2) - panjang
                    print(f"Lebar = (keliling / 2) - panjang\nLebar = ({keliling} / 2) - {panjang}")
                    print(f"Lebarnya adalah = {lebar}")
                    UlangLebardariKeliling(panjang, lebar)

                else :
                    print("\nKeliling harus lebih besar dari lebar!\n")
                    HitungLebardariKeliling()
            else :
                print("\nKeduanya tidak boleh sama dengan 0!\n")
                HitungLebardariKeliling()

        else : 
            print("\nHarus menggunakan bilangan bulat!\n")
            HitungLebardariKeliling()

    else :
        print("\nKeduanya tidak boleh kosong!\n")
        HitungLebardariKeliling()

def PersegiPanjang() :
    print(10*"-"+"Persegi Panjang"+"-"*10)
    Pilih = input("Menghitung luas atau keliling persegi panjang :\n1. Luas | 2. Keliling | 3. Menu\n")

    if Pilih  != "" :
        
        if Pilih.casefold() == "luas" or Pilih == "1" :
            Luas()  

        elif Pilih.casefold() == "keliling" or Pilih == "2" :
            Keliling()

        elif Pilih.casefold() == "main"  or Pilih == "3" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        else :
            print("\nHarus memilih salah satu yanga da di atas!\n")
            PersegiPanjang()
    
    else :
        print("\nTidak boleh kosong!\n")
        PersegiPanjang()

def Luas() : 
    Input_user = input("""
    1. Hitung luas : luas
    2. Hitung lebar : lebar
    3. Hitung panjang : panjang
    0. Kembali
    """)

    if Input_user  != "" :
        
        if Input_user == "1" or Input_user.casefold() == "luas" :
            HitungLuasPersegiPanjang()

        elif Input_user == "2" or Input_user.casefold() == "lebar" :
            HitungLuasPersegiPanjang()

        elif Input_user == "3" or Input_user.casefold() == "panjang" :
            HitungPanjangDariLuas()

        elif Input_user == "0"  or Input_user.casefold() == "kembali" :
            PersegiPanjang()

        else :
            print("\nHarap memilih salah satu yang ada diatas!\n")
            Luas()
    
    else :
        print("\nTidak boleh kosong!\n")
        Luas()
        
def Keliling() :
    Input_user = input("""
    1. Hitung Keliling : keliling
    2. Hitung lebar : lebar
    3. Hitung panjang : panjang
    0. Kembali
    """)

    if Input_user  != "" :
        
        if Input_user == "1" or Input_user.casefold() == "keliling" :
            HitungKelilingPersegiPanjang()

        elif Input_user == "2" or Input_user.casefold() == "lebar" :
            HitungLebardariKeliling()

        elif Input_user == "3" or Input_user.casefold() == "panjang" :
            HitungPanjangdariKeliling()

        elif Input_user == "0"  or Input_user.casefold() == "kembali" :
            PersegiPanjang()

        else :
            print("\nHarap memilih salah satu yang ada diatas!\n")
            Keliling()

    else :
        print("\nTidak boleh kosong!\n")
        Keliling()

def UlangLebardariLuas(panjang, lebar) :
    ulang = input("""\nApakah anda mau menghitung ulang lagi?
    1. Ya | 2. tidak
    3. Menghitung keliling dari panjang dan lebar yang sama? : sama
    4. Menghitung keliling dari panjang dan lebar yang baru? : baru
    5. Menghitung luas dari panjang dan lebar yang berbeda? : beda
    6. Menghitung panjang dari keliling dan lebar yang baru? : panjang
    7. Menghitung lebar dari keliling dan panjang yang baru? : lebar
    8. Menghitung lebar dari luas dan panjang yang baru? : luas
    9. Menghitung luas dengan satu yang berbeda? : satu
    10. Menghitung keliling dengan satu yang berbeda? : keliling
    """)

    if ulang  != "" :
        
        if ulang.casefold() == "ya" or ulang == "1" :
            HitungLebardariLuas()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "sama" or ulang == "3" :
            HitungKelilingdariLuas(panjang, lebar)

        elif ulang.casefold() == "baru" or ulang == "4" :
            HitungKelilingPersegiPanjang()

        elif ulang.casefold() == "beda" or ulang == "5" :
            HitungLuasPersegiPanjang()

        elif ulang.casefold() == "panjang" or ulang == "6" :
            HitungPanjangdariKeliling()

        elif ulang.casefold() == "lebar" or ulang == "7" :
            HitungLebardariKeliling()

        elif ulang.casefold() == "luas" or ulang == "8" :
            HitungLebardariLuas()

        elif ulang.casefold() == "satu" or ulang == "9" :
            LuasSatu(panjang, lebar)

        elif ulang.casefold() == "keliling" or ulang == "10" :
            KelilingSatu(panjang, lebar)

        else :
            print("\nHarap memilih dari salah satu yang ada di atas!\n")
            UlangLebardariLuas(panjang, lebar)
    
    else :
        print("\nTidak boleh kosong!\n")
        UlangLebardariLuas(panjang, lebar)
    
def UlangPanjangdariLuas(panjang, lebar) :
    ulang = input("""\nApakah anda mau menghitung ulang lagi?
    1. Ya | 2. tidak
    3. Menghitung keliling dengan panjang dan lebar yang sama? : sama
    4. Menghitung keliling dengan panjang dan lebar yang baru? : baru
    5. Menghitung luas dengan panjang dan lebar yang berbeda? : beda
    6. Menghitung panjang dari keliling dan lebar yang baru? : panjang
    7. Menghitung lebar dari keliling dan panjang yang baru? : lebar
    8. Menghitung lebar dari luas dan panjang yang baru? : luas
    9. Menghitung luas dengan satu yang berbeda? : satu
    10. Menghitung Keliling dengan satu yang berbeda? : keliling
    """)

    if ulang  != "" :
        
        if ulang.casefold() == "ya" or ulang == "1" :
            HitungPanjangDariLuas()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "sama" or ulang == "3" :
            HitungKelilingdariLuas(panjang, lebar)

        elif ulang.casefold() == "beda" or ulang == "4" :
            HitungKelilingPersegiPanjang()

        elif ulang.casefold() == "beda" or ulang == "5" :
            HitungLuasPersegiPanjang()

        elif ulang.casefold() == "panjang" or ulang == "6" :
            HitungPanjangdariKeliling()

        elif ulang.casefold() == "lebar" or ulang == "7" :
            HitungLebardariKeliling()

        elif ulang.casefold() == "luas" or ulang == "8" :
            HitungLebardariLuas()

        elif ulang.casefold() == "satu" or ulang == "9" :
            LuasSatu(panjang, lebar)

        elif ulang.casefold() == "keliling" or ulang == "10" :
            KelilingSatu(panjang, lebar)

        else :
            print("\nHarus memilih dari salah satu yang di atas!\n")
            UlangPanjangdariLuas(panjang, lebar)

    else :
        print("\nTidak boleh kosong!\n")
        UlangPanjangdariLuas(panjang, lebar)

def UlangPanjangdariKeliling(panjang, lebar) :
    ulang = input("""\nApakah anda mau menghitung ulang lagi?
    1. Ya | 2. Tidak
    3. Menghitung luas dengan panjang dan lebar yang sama? : sama
    4. Menghitung luas dengan panjang dan lebar yang baru? : baru
    5. Menghitung keliling dengan panjang dan lebar yang berbeda? : beda
    6. Menghitung lebar dari keliling dan panjang yang baru? : lebar
    7. Menghitung panjang dari luas dan lebar yang baru? : panjang
    8. Menghitung lebar dari luas dan panjang yang baru? : luas
    9. Menghitung luas dengan satu yang berbeda? : satu
    10. Menghitung keliling dengan satu yang berbeda? : keliling
    """)

    if ulang  != "" :
        
        if ulang.casefold() == "ya" or ulang == "1" :
            HitungPanjangdariKeliling()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "sama" or ulang == "3" :
            HitungLuasdariKeliling(panjang, lebar)

        elif ulang.casefold() == "baru" or ulang == "4" :
            HitungLuasPersegiPanjang()

        elif ulang.casefold() == "beda" or ulang == "5" :
            HitungKelilingPersegiPanjang()

        elif ulang.casefold() == "lebar" or ulang == "6" :
            HitungLebardariKeliling()

        elif ulang.casefold() == "panjang" or ulang == "7" :
            HitungPanjangDariLuas()
            
        elif ulang.casefold() == "luas" or ulang == "8" :
            HitungLebardariLuas()
            
        elif ulang.casefold() == "satu" or ulang == "9" :
            LuasSatu(panjang, lebar)

        elif ulang.casefold() == "keliling" or ulang == "10" :
            KelilingSatu(panjang, lebar)

        else :
            print("\nHarus memilih salah satu dari di atas!\n")
            UlangPanjangdariKeliling(panjang, lebar)
    else :
        print("\nTidak boleh kosong!\n")
        UlangPanjangdariKeliling(panjang , lebar)
    
def UlangLebardariKeliling(panjang , lebar) :
    ulang = input("""\nApakah anda mau menghitung ulang lagi?
    1. Ya | 2. Tidak
    3. Menghitung luas dengan panjang dan lebar yang sama? : sama
    4. Menghitung luas dengan panjang dan lebar yang baru? : baru
    5. Menghitung keliling dengan panjang dan lebar yang berbeda? : beda
    6. Menghitung panjang dari keliling dan lebar yang baru? : panjang
    7. Menghitung panjang dari luas dan lebar yang baru? : luas
    8. Menghitung lebar dari luas dan panjang yang baru? : lebar
    9. Menghitung luas dengan satu yang berbeda? : satu
    10. Menghitung keliling dengan satu yang berbeda? : keliling
    """)

    if ulang  != "" :
        
        if ulang.casefold() == "ya" or ulang == "1" :
            HitungLebardariKeliling()

        elif ulang.casefold() == "tidak" or ulang == "2" :
            print("\nKembali ke menu utama\n")
            from Menu import Main
            Main()

        elif ulang.casefold() == "sama" or ulang == "3" :
            HitungLuasdariKeliling(panjang, lebar)

        elif ulang.casefold() == "baru" or ulang == "4" :
            HitungLuasPersegiPanjang()

        elif ulang.casefold() == "beda" or ulang == "5" :
            HitungKelilingPersegiPanjang()

        elif ulang.casefold() == "lebar" or ulang == "6" :
            HitungPanjangdariKeliling()

        elif ulang.casefold() == "luas" or ulang == "7" :
            HitungPanjangDariLuas()

        elif ulang.casefold() == "lebar" or ulang == "8" :
            HitungLebardariLuas()

        elif ulang.casefold() == "satu" or ulang == "9" :
            LuasSatu(panjang, lebar)

        elif ulang.casefold() == "keliling" or ulang == "10" :
            KelilingSatu(panjang, lebar)

        else :
            print("\nHarus memilih salah satu dari di atas!\n")
            UlangLebardariKeliling(panjang , lebar)
    else :
        print("\nTidak boleh kosong!\n")
        UlangLebardariKeliling(panjang , lebar)
        
def LuasSatu(panjang, lebar) :
    pilih = input("""
    1. Hitung luas dengan hanya panjang yang baru? : panjang
    2. Hitung luas dengan hanya lebar yang baru? : lebar
    0. Kembali
    """)

    if pilih  != "" :
        
        if pilih.casefold() == "panjang" or pilih == "1" :
            LuastanpaPanjang(lebar)

        elif pilih.casefold() == "lebar" or pilih == "2" :
            LuastanpaLebar(panjang)

        elif pilih.casefold() == "kembali" or pilih == "0" :
            UlangLuas(panjang, lebar)

        else :
            print("\nHarus memilih dari salah sath diatas!\n")
            LuasSatu(panjang, lebar)

    else :
        print("\nTidak boleh kosong!\n")
        LuasSatu(panjang, lebar)

def KelilingSatu(panjang, lebar) :
    pilih = input("""
    1. Hitung Keliling dengan hanya panjang yang baru? : panjang
    2. Hitung Keliling dengan hanya lebar yang baru? : lebar
    0. Kembali
    """)

    if pilih  != "" :
        
        if pilih.casefold() == "panjang" or pilih == "1" :  
            KelilingtanpaPanjang(lebar)

        elif pilih.casefold() == "lebar" or pilih == "2" :
            KelilingtanpaLebar(panjang)

        elif pilih.casefold() == "kembali" or pilih == "0" :
            UlangKeliling(panjang, lebar)

        else :
            print("\nHarus memilih dari salah sath diatas!\n")
            KelilingSatu(panjang , lebar)

    else :
        print("\nTidak boleh kosong!\n")
        KelilingSatu(panjang ,lebar)

def LuastanpaPanjang(lebar) :
    inputPanjang = input("\nMasukan panjang : ")

    if inputPanjang  != "" :
        
        if inputPanjang.isdigit() :
            panjang = int(inputPanjang)

            if panjang  != 0 :
                    
                if panjang > lebar :
                    hasil = panjang * lebar
                    print(f"Luas = Panjang * Lebar\nLuas =  {panjang} *  {lebar}")
                    print(f"Luasnya adalah = {hasil}")
                    UlangLuas(panjang, lebar)

                else :
                    print(f"\nPanjang harus lebih besar dari lebar!\nLebar = {lebar}\n")
                    LuastanpaPanjang(lebar)
            else :
                print("\nTidak boleh sama dengan 0!\n")
                LuastanpaPanjang(lebar)

        else :
            print("\nHarus menggunakan bilangan bulat!\n")
            LuastanpaPanjang(lebar)
    
    else :
        print("\nTidak boleh kosong!\n")
        LuastanpaPanjang(lebar)

def LuastanpaLebar(panjang) :
    inputLebar = input("\nMasukan lebar : ")

    if inputLebar  != "" :
        
        if inputLebar.isdigit() :
            lebar = int(inputLebar)

            if lebar  != 0 :
                
                if panjang > lebar : 
                    hasil = panjang * lebar
                    print(f"Luas = Panjang * Lebar\nLuas = {panjang} * {lebar}")
                    print(f"Luasnya adalah = {hasil}")
                    UlangLuas(panjang, lebar)
                    
                else : 
                    print("\nLebar harus lebih kecil dari panjang!\nPanjang = ", panjang, "\n")
                    LuastanpaLebar(panjang)

            else :
                print("\nTidak boleh sama dengan 0!\n")
                LuastanpaLebar(panjang)

        else :
            print("\nHarus menggunakan bilangan bulat!\n")
            LuastanpaLebar(panjang)
    
    else :
        print("\nTidak boleh kosong!\n")
        LuastanpaLebar(panjang)

def KelilingtanpaPanjang(lebar) :
    inputpanjang = input("\nMasukan panjang : ")

    if inputpanjang  != "" :
        
        if inputpanjang.isdigit() :
            panjang = int(inputpanjang)

            if panjang != 0 :
                
                if panjang > lebar :
                    hasil = (panjang + lebar) * 2
                    print(f"Keliling = (panjang * lebar) * 2\nKeliling = ({panjang} + {lebar}) * 2")
                    print(f"kelilingnya adalah = {hasil}")
                    UlangKeliling(panjang, lebar)

                else :
                    print(f"\nPanjang harus lebih besar dari lebar!\nLebar = {lebar}\n")
                    KelilingtanpaPanjang(lebar)
            
            else :
                print("\nTidak boleh sama dengan 0!\n")
                KelilingtanpaPanjang(lebar)

        else :
            print("\nHarus menggunakan bilangan bulat!\n")
            KelilingtanpaPanjang(lebar)
    
    else :
        print("\nTidak boleh kosong!\n")
        KelilingtanpaPanjang(lebar)

def KelilingtanpaLebar(panjang) :
    inputLebar = input("\nMasukan lebar : ")

    if inputLebar  != "" :
        
        if inputLebar.isdigit() :
            lebar = int(inputLebar)

            if lebar  != 0 :
                
                if panjang > lebar : 
                    hasil = (panjang + lebar) * 2
                    print(f"Keliling = (panjang * lebar) * 2\nKeliling = ({panjang} +  {lebar}) * 2")
                    print(f"kelilingnya adalah = {hasil}")
                    UlangKeliling(panjang, lebar)

                else : 
                    print(f"\nLebar harus lebih kecil dari panjang!\nPanjang = {panjang}\n")
                    KelilingtanpaLebar(panjang)

            else :
                print("\nTidak boleh sama dengan 0!\n")
                KelilingtanpaLebar(panjang)        
                    
        else :
            print("\nHarus menggunakan bilangan bulat!\n")
            KelilingtanpaLebar(panjang)

    else :
        print("\nTidak boleh kosogn!\n")
        KelilingtanpaLebar(panjang)
