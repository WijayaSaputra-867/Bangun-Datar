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
    if ulang.casefold() == "ya" or ulang == "1" :
        HitungLuasPersegiPanjang()
    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()
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
    if ulang.casefold() == "ya" or ulang == "1":
        HitungKelilingPersegiPanjang()
    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()
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
            
def HitungLuasPersegiPanjang() :
    inputPanjang = input("\nMasukan Panjang : ")
    inputLebar = input("Masukan Lebar : ")
    if inputPanjang.isdecimal() & inputLebar.isdecimal() :
        panjang = int(inputPanjang)
        lebar = int(inputLebar)

        if panjang > lebar :
            hasil = panjang * lebar
            print("Luas = Panjang * Lebar\nLuas = ", panjang, " * ", lebar)
            print("Luasnya adalah = ", hasil)
            UlangLuas(panjang, lebar)

        else :
            print("\nPanjang harus Lebih besar dari lebar!\n")
            HitungLuasPersegiPanjang()

    else :
        print("\nKeduanya harus menggunakan bilangan bulat!\n")
        HitungLuasPersegiPanjang()

def HitungKelilingPersegiPanjang() :
    inputPanjang = input("\nMasukan Panjang : ")
    inputLebar = input("Masukan Lebar : ")
    if inputPanjang.isdecimal() & inputLebar.isdecimal() :
        panjang = int(inputPanjang)
        lebar = int(inputLebar)

        if panjang > lebar :
            hasil = (panjang + lebar) * 2
            print("Keliling = (Panjang + Lebar) * 2\nKeliling = (", panjang, " + ", lebar, ") * 2")
            print("Kelilingnya adalah = ", hasil)
            UlangKeliling(panjang, lebar)

        else :
            print("\nPanjang harus Lebih besar dari lebar!\n")
            HitungKelilingPersegiPanjang()

    else :
        print("\nKeduanya harus menggunakan bilangan bulat!\n")
        HitungKelilingPersegiPanjang()

def HitungKelilingdariLuas(panjang, lebar) :
    hasil = (panjang + lebar) * 2
    print("Keliling = (Panjang + Lebar) * 2\nKeliling = (", panjang, " + ", lebar, " ) * 2")
    print("Kelilingnya adalah = ", hasil)
    UlangKeliling(panjang, lebar)

def HitungLuasdariKeliling(panjang, lebar) :
    hasil = panjang * lebar
    print("Luas = Panjang * Lebar\nLuas = ", panjang, " * ", lebar)
    print("Luasnya adalah = ", hasil)
    UlangLuas(panjang, lebar)

def HitungPanjangDariLuas() :
    inputLuas = input("\nMasukan Luas : ")
    inputLebar = input("Masukan Lebar : ")
    if inputLuas.isdecimal() & inputLebar.isdecimal() :
        luas = int(inputLuas)
        lebar = int(inputLebar)
        if luas > lebar :
            panjang = luas / lebar
            print("Panjang = luas / lebar\nPanjang = ", luas, " / ", lebar)
            print("Panjangnya adalah = ", panjang)
            UlangPanjangdariLuas(panjang, lebar)
        else :
            print("\nLuas harus lebih besar dari lebar!\n")
            HitungPanjangDariLuas()
    else :
        print("\nKeduanya harus menggunakan bilangan bulat!\n")
        HitungPanjangDariLuas()

def HitungLebardariLuas() :
    inputLuas = input("\nMasukan Luas : ")
    inputPanjang = input("Masukan Panjang : ")
    if inputLuas.isdecimal() & inputPanjang.isdecimal() :
        luas = int(inputLuas)
        panjang = int(inputPanjang)
        if luas > panjang :
            lebar = luas / panjang
            print("Lebar = luas / lebar\nLebar = ", luas, " / ", panjang)
            print("Lebarnya adalah = ", lebar)
            UlangLebardariLuas()
        else :
            print("\nLuas harus lebih besar dari panjang!\n")
            HitungLebardariLuas()
    else :
      print("\nKeduanya harus menggunakan bilangan bulat!\n")
      HitungLebardariLuas()

def HitungPanjangdariKeliling() :
    inputKeliling = input("\nMasukan Keliling : ")
    inputLebar = input("Masukan Lebar : ")
    if inputKeliling.isdecimal() & inputLebar.isdecimal() :
        keliling = int(inputKeliling)
        lebar = int(inputLebar)
        if keliling > lebar :
            panjang = keliling / 2 - lebar
            print("Panjang = (keliling / 2) - lebar\nPanjang = ("+keliling+ " / 2) - ", lebar)
            print("Panjangnya adalah = ", panjang)
            UlangPanjangdariKeliling(panjang , lebar)
        else :
            print("\nKeliling harus lebih besar dari lebar!\n")
            HitungPanjangdariKeliling()
    else :
        print("\nHarus menggunakan bilangan bulat!\n")
        HitungPanjangdariKeliling()

def HitungLebardariKeliling() :
    inputKeliling = input("\nMasukan Keliling : ")
    inputPanjang = input("Masukan Panjang : ")
    if inputKeliling.isdecimal() & inputPanjang.isdecimal() :
        keliling = int(inputKeliling)
        panjang = int(inputPanjang)
        if keliling > panjang :
            lebar = (keliling / 2) - panjang
            print("Lebar = (keliling / 2) - panjang\nLebar = ("+keliling+" / 2) - ", panjang)
            print("Lebarnya adalah = ", lebar)
            UlangLebardariKeliling(panjang, lebar)
        else :
            print("\nKeliling harus lebih besar dari lebar!\n")
            HitungLebardariKeliling()
    else : 
        print("\nHarus menggunakan bilangan bulat!\n")
        HitungLebardariKeliling()

def PersegiPanjang() :
    Pilih = input("Menghitung luas atau keliling persegi panjang :\n1. Luas | 2. Keliling\n")
    if Pilih.casefold() == "luas" or Pilih == "1" :
        Luas()  
    elif Pilih.casefold() == "keliling" or Pilih == "2" :
        Keliling()
    else :
        print("\nJika menggunakan bilangan harus memilih 1 atau 2!\nJika menggunakan kalimat harus memilih luas atau keliling!\n")
        PersegiPanjang()

def Luas() : 
    Input_user = input("""
    1. Hitung luas : luas
    2. Hitung lebar : lebar
    3. Hitung panjang : panjang
    """)
    if Input_user == "1" or Input_user.casefold() == "luas" :
        HitungLuasPersegiPanjang()
    elif Input_user == "2" or Input_user.casefold() == "lebar" :
        HitungLuasPersegiPanjang()
    elif Input_user == "3" or Input_user.casefold() == "panjang" :
        HitungPanjangDariLuas()
    else :
        print("\nHarap memilih salah satu yang ada diatas!\n")
        Luas()
        
def Keliling() :
    Input_user = input("""
    1. Hitung Keliling : keliling
    2. Hitung lebar : lebar
    3. Hitung panjang : panjang
    """)
    if Input_user == "1" or Input_user.casefold() == "keliling" :
        HitungKelilingPersegiPanjang()
    elif Input_user == "2" or Input_user.casefold() == "lebar" :
        HitungLebardariKeliling()
    elif Input_user == "3" or Input_user.casefold() == "panjang" :
        HitungPanjangdariKeliling()
    else :
        print("\nHarap memilih salah satu yang ada diatas!\n")
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
    if ulang.casefold() == "ya" or ulang == "1" :
        HitungLebardariLuas()
    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()
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
    if ulang.casefold() == "ya" or ulang == "1" :
        HitungPanjangDariLuas()
    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()
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
    if ulang.casefold() == "ya" or ulang == "1" :
        HitungPanjangdariKeliling()
    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()
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
    if ulang.casefold() == "ya" or ulang == "1" :
        HitungLebardariKeliling()
    elif ulang.casefold() == "tidak" or ulang == "2" :
        print("\nTerima kasih :-)\n")
        exit()
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
        UlangPanjangdariKeliling(panjang , lebar)
        
def LuasSatu(panjang, lebar) :
    pilih = input("""
    1. Hitung luas dengan hanya panjang yang baru? : panjang
    2. Hitung luas dengan hanya lebar yang baru? : lebar
    3. Kembali
    """)
    if pilih.casefold() == "panjang" or pilih == "1" :
        LuastanpaPanjang(lebar)
    elif pilih.casefold() == "lebar" or pilih == "2" :
        LuastanpaLebar(panjang)
    elif pilih.casefold() == "kembali" or pilih == "3" :
        UlangLuas(panjang, lebar)
    else :
        print("\nHarus memilih dari salah sath diatas!\n")
        LuasSatu(panjang, lebar)

def KelilingSatu(panjang, lebar) :
    pilih = input("""
    1. Hitung Keliling dengan hanya panjang yang baru? : panjang
    2. Hitung Keliling dengan hanya lebar yang baru? : lebar
    3. Kembali
    """)
    if pilih.casefold() == "panjang" or pilih == "1" :  
        KelilingtanpaPanjang(lebar)
    elif pilih.casefold() == "lebar" or pilih == "2" :
        KelilingtanpaLebar(panjang)
    elif pilih.casefold() == "kembali" or pilih == "3" :
        UlangKeliling(panjang, lebar)
    else :
        print("\nHarus memilih dari salah sath diatas!\n")
        KelilingSatu(panjang , lebar)

def LuastanpaPanjang(lebar) :
    inputPanjang = input("\nMasukan panjang : ")
    if inputPanjang.isdecimal() :
        panjang = int(inputPanjang)
        if panjang > lebar :
            hasil = panjang * lebar
            print("Luas = Panjang * Lebar\nLuas = ", panjang, " * ", lebar)
            print("Luasnya adalah = ", hasil)
            UlangLuas(panjang, lebar)
        else :
            print("\nPanjang harus lebih besar dari lebar!\nLebar = ", lebar, "\n")
            LuastanpaPanjang(lebar)
    else :
        print("\nHarus menggunakan bilangan bulat!\n")
        LuastanpaPanjang(lebar)

def LuastanpaLebar(panjang) :
    inputLebar = input("\nMasukan lebar : ")
    if inputLebar.isdecimal() :
        lebar = int(inputLebar)
        if panjang > lebar : 
            hasil = panjang * lebar
            print("Luas = Panjang * Lebar\nLuas = ", panjang, " * ", lebar)
            print("Luasnya adalah = ", hasil)
            UlangLuas(panjang, lebar)
        else : 
            print("\nLebar harus lebih kecil dari panjang!\nPanjang = ", panjang, "\n")
            LuastanpaLebar(panjang)
    else :
        print("\nHarus menggunakan bilangan bulat!\n")
        LuastanpaLebar(panjang)

def KelilingtanpaPanjang(lebar) :
    inputpanjang = input("\nMasukan panjang : ")
    if inputpanjang.isdecimal() :
        panjang = int(inputpanjang)
        if panjang > lebar :
            hasil = (panjang + lebar) * 2
            print("Keliling = (panjang * lebar) * 2\nKeliling = (", panjang, " + ", lebar, ") * 2")
            print("kelilingnya adalah = ", hasil)
            UlangKeliling(panjang, lebar)
        else :
            print("\nPanjang harus lebih besar dari lebar!\nLebar = ", lebar, "\n")
            LuastanpaLebar(lebar)
    else :
        print("\nHarus menggunakan bilangan bulat!\n")
        LuastanpaLebar(lebar)

def KelilingtanpaLebar(panjang) :
    inputLebar = input("\nMasukan lebar : ")
    if inputLebar.isdecimal() :
        lebar = int(inputLebar)
        if panjang > lebar : 
            hasil = (panjang + lebar) * 2
            print("Keliling = (panjang * lebar) * 2\nKeliling = (", panjang, " + ", lebar, ") * 2")
            print("kelilingnya adalah = ", hasil)
            UlangKeliling(panjang, lebar)
        else : 
            print("\nLebar harus lebih kecil dari panjang!\nPanjang = ", panjang, "\n")
            LuastanpaLebar(panjang)
    else :
        print("\nHarus menggunakan bilangan bulat!\n")
        LuastanpaLebar(panjang)


PersegiPanjang()