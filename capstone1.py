# Aplikasi Sistem Informasi Rental Mobil
# Memiliki 5 Menu yaitu membaca data, merubah data, menambah data, menghapus data, dan data mobil tersedia

menuList = [
    '1. Report Data Mobil',
    '2. Mengubah Data Mobil',
    '3. Menambah Data Mobil',
    '4. Menghapus Data Mobil',
    '5. Daftar Mobil Tersedia',
    '6. Keluar'
]

# Dummy Data Mobil
dataMobil = [
    {'PlatNomor': 'M0001A', 'Merk': 'Toyota', 'Model': 'Avanza', 'Tahun': '2020', 'Harga Sewa per Hari': 350000, 'Status': 'Tersedia'},
    {'PlatNomor': 'M0002B', 'Merk': 'Honda', 'Model': 'Jazz', 'Tahun': '2019', 'Harga Sewa per Hari': 450000, 'Status': 'Disewa'},
    {'PlatNomor': 'M0003C', 'Merk': 'Suzuki', 'Model': 'Ertiga', 'Tahun': '2021', 'Harga Sewa per Hari': 400000, 'Status': 'Tersedia'},
    {'PlatNomor': 'M0004D', 'Merk': 'Daihatsu', 'Model': 'Xenia', 'Tahun': '2018', 'Harga Sewa per Hari': 300000, 'Status': 'Tersedia'},
    {'PlatNomor': 'M0005E', 'Merk': 'Mitsubishi', 'Model': 'Xpander', 'Tahun': '2022', 'Harga Sewa per Hari': 500000, 'Status': 'Disewa'},
    ]

def reportData(): 
    pilihanUserMenu1 = '1'
    while pilihanUserMenu1 != '3':
        print("\n======= REPORT DATA MOBIL ======\n")
        print("1. Tampilkan Semua Data Mobil")
        print("2. Tampilkan Data Mobil Sesuai Plat Nomor")
        print("3. Kembali ke Menu Utama")
        pilihanUserMenu1 = input("Silakan pilih menu (Masukkan angka 1-3): ")
        if pilihanUserMenu1 == '1':
            if len(dataMobil) == 0:
                print("Data mobil kosong.")
            else:
                for index, mobil in enumerate(dataMobil):
                    print(f"{index+1}. {mobil['PlatNomor']} | {mobil['Merk']} {mobil['Model']} | Tahun: {mobil['Tahun']} | Harga Sewa per Hari: Rp{mobil['Harga Sewa per Hari']:,} | Status: {mobil['Status']}")
            continue
        elif pilihanUserMenu1 == '2':
            if len(dataMobil) == 0:
                print("Data mobil kosong.")
            else: 
                platInput = input("Masukkan plat nomor mobil yang ingin Anda lihat: ")
                for index, mobil in enumerate(dataMobil):
                    if mobil['PlatNomor'] == platInput:
                        print(f"Plat Nomor: {mobil['PlatNomor']}\nMerk: {mobil['Merk']} {mobil['Model']}\nTahun: {mobil['Tahun']}\nHarga Sewa per Hari: Rp{mobil['Harga Sewa per Hari']:,}\nStatus: {mobil['Status']}")
                        break
                else:
                    print("Data yang Anda cari tidak ditemukan.")
                continue
        elif pilihanUserMenu1 == '3':
            quit 
        else:
            print("Menu yang Anda masukkan salah!")

def updateData():
    pilihanUserMenu2 = '1'
    while pilihanUserMenu2 != '2':
        print("\n======= UBAH DATA MOBIL ======\n")
        print("1. Ubah Data Mobil")
        print("2. Kembali ke Menu Utama")
        pilihanUserMenu2 = input("Silakan pilih Sub Menu Update Data[1-2]: ")
        
        if pilihanUserMenu2 == '1':
            if len(dataMobil) == 0:
                print("Data mobil kosong.")
            else:
                platInput = input("Masukkan Plat Nomor mobil: ")
                for index, mobil in enumerate(dataMobil):
                    if mobil['PlatNomor'] == platInput:
                        print(f"Plat Nomor: {mobil['PlatNomor']}\nMerk: {mobil['Merk']} {mobil['Model']}, Tahun: {mobil['Tahun']}, Harga Sewa: Rp{mobil['Harga Sewa per Hari']:,}, Status: {mobil['Status']}")
                        lanjut = input("Tekan Y jika ingin lanjut Update Data atau N jika ingin cancel Update (Y/N): ").strip().upper()
                        
                        if lanjut == 'Y':
                            kolom_mapping = {
                                'plat nomor': 'PlatNomor',
                                'merk': 'Merk',
                                'model': 'Model',
                                'tahun': 'Tahun',
                                'harga sewa per hari': 'Harga Sewa per Hari',
                                'status': 'Status'
                            }
                            kolom_user = input("Masukkan Kolom/Keterangan yang ingin di-update: ").strip().lower()
                            if kolom_user in kolom_mapping:
                                nilaiBaru = input(f"Masukkan {kolom_user} baru: ")
                                if kolom_user == 'harga sewa per hari':
                                    nilaiBaru = int(nilaiBaru)
                                simpan = input("Apakah data akan diupdate? (Y/N): ").strip().upper()
                                if simpan == 'Y':
                                    dataMobil[index][kolom_mapping[kolom_user]] = nilaiBaru
                                    print("Data telah di-Update.")
                                else:
                                    print("Update dibatalkan.")
                            else:
                                print("Kolom tidak ditemukan.")
                        break
                else:
                    print("Data yang Anda cari tidak ditemukan.")
            continue  # kembali ke submenu update

        elif pilihanUserMenu2 == '2':
            break  # keluar dari update menu
        else:
            print("Menu yang Anda masukkan salah!")

def addData():
    pilihanUserMenu3 = '1'
    while pilihanUserMenu3 != '2':
        print("\n======= TAMBAH DATA MOBIL ======\n")
        print("1. Tambah Data Mobil")
        print("2. Kembali ke Menu Utama")
        pilihanUserMenu3 = input("Silakan Pilih Sub Menu Create Data [1-2]: ")
        
        if pilihanUserMenu3 == '1':
            platBaru = input("Masukkan Plat Nomor : ")
            merkBaru = input("Masukkan Merk : ")
            modelBaru = input("Masukkan Model : ")
            tahunBaru = input("Masukkan Tahun : ")
            hargaBaru = input("Masukkan Harga Sewa per Hari : ")
            statusBaru = input("Masukkan Status : ")
            
            simpan = input("Apakah Data akan disimpan? (Y/N) : ").strip().upper()
            if simpan == 'Y':
                dataMobil.append({
                    'PlatNomor': platBaru,
                    'Merk': merkBaru,
                    'Model': modelBaru,
                    'Tahun': tahunBaru,
                    'Harga Sewa per Hari': int(hargaBaru),
                    'Status': statusBaru
                })
                print("Data Tersimpan.")
            else:
                print("Data tidak tersimpan.")
            continue
        
        elif pilihanUserMenu3 == '2':
            break
        else:
            print("Menu yang Anda masukkan salah!")

def deleteData():
    pilihanUserMenu4 = '1'
    while pilihanUserMenu4 != '2':
        print("\n======= HAPUS DATA MOBIL ======\n")
        print("1. Hapus Data Mobil")
        print("2. Kembali ke Menu Utama")
        pilihanUserMenu4 = input("Silakan pilih Sub Menu Delete Data [1-2]: ")

        if pilihanUserMenu4 == '1':
            if len(dataMobil) == 0:
                print("Data mobil kosong.")
            else:
                platInput = input("Masukkan Plat Nomor mobil yang ingin dihapus: ")
                for index, mobil in enumerate(dataMobil):
                    if mobil['PlatNomor'] == platInput:
                        print(f"Plat Nomor: {mobil['PlatNomor']}\nMerk: {mobil['Merk']} {mobil['Model']}, Tahun: {mobil['Tahun']}, Harga Sewa: Rp{mobil['Harga Sewa per Hari']:,}, Status: {mobil['Status']}")
                        hapus = input("Apakah Anda yakin ingin menghapus data ini? (Y/N): ").strip().upper()
                        if hapus == 'Y':
                            del dataMobil[index]
                            print("Data berhasil dihapus.")
                        else:
                            print("Penghapusan dibatalkan.")
                        break
                else:
                    print("Data yang Anda cari tidak ditemukan.")
            continue

        elif pilihanUserMenu4 == '2':
            break
        else:
            print("Menu yang Anda masukkan salah!")

def filterMobilTersedia():
    print("\n======= DAFTAR MOBIL TERSEDIA ======\n")
    if len(dataMobil) == 0:
        print("Data mobil kosong.")
    else:
        hasilFilter = [mobil for mobil in dataMobil if mobil['Status'].lower() == 'tersedia']
        
        if len(hasilFilter) == 0:
            print("Tidak ada mobil yang tersedia saat ini.")
        else:
            for index, mobil in enumerate(hasilFilter):
                print(f"{index+1}. {mobil['PlatNomor']} | {mobil['Merk']} {mobil['Model']} | Tahun: {mobil['Tahun']} | Harga Sewa: Rp{mobil['Harga Sewa per Hari']:,} | Status: {mobil['Status']}")
    
def mainMenu():
# Selama user tidak memilih nomor 5 ('Keluar') aplikasi akan terus berjalan
    userInput = '1'
    while userInput != '6' :
        print("\n======= SISTEM INFORMASI RENTAL MOBIL ======\n")
        for menu in menuList:
            print(menu)
        userInput = input('Silakan pilih menu (Pilih angka 1-5): ')
        if userInput == '1':
            reportData()
        elif userInput == '2':
            updateData()
        elif userInput == '3':
            addData()
        elif userInput == '4':
            deleteData()
        elif userInput == '5':
            filterMobilTersedia()
        elif userInput =='6':
            print("Anda telah keluar dari aplikasi.")
        else: 
            print("Menu yang Anda pilih tidak sesuai!")

mainMenu()
