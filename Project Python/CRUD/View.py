from . import operasi

#4. Tahapan Delete konsole
def delete_console():
    read_console()
    while(True):
        print("Silahkan Pilih No buku yang akan didelete: ")
        no_buku = int(input("Nomor Buku: "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]

            print("\n" + "=" *100)
            print("Silahkan Pilih Data apa yang Ingin anda hapus:")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            is_done = input("Apakah yakin dihapus (y/n)?:")
            if is_done == "y" or is_done == "Y":
                operasi.delete(no_buku)
                break
           
        else:
            print("Nomor Tidak Valid, silahkan masukkan lagi")
    print("Data Berhasil dihapus")






#3. Tahapan Update Data
def update_console():
    read_console()
    while(True):
        print("Silahkan Pilih No buku yang akan diupdate: ")
        no_buku = int(input("Nomor Buku: "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor Tidak Valid, silahkan masukkan lagi")

    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        #Data yang ingin diupdate
        print("\n" + "=" *100)
        print("Silahkan Pilih Data apa yang Ingin anda Ubah:")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")


        #Memilih mode untuk update
        user_option = input("Pilih data [1,2,3]:")
        print("\n" + "="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while(True): #mengulang untuk mengambil data tahun jika diisi dengan salah
                    try: #untuk mengatasi synntax eror agar membeirikan pesan bukan membatalkan program

                        tahun = int(input("Tahun\t: "))
                        #hanya mengisikan angka pada 4 digit nilai dan tidak bisa lebih
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Hanya Angka yang harus dimasukkan")

                    except:
                        print("Hanya Angka yang harus dimasukkan")
            case _: print("index tidak cocok")
        
        is_done = input("apakah selesai (y/n)?")
        if is_done == "y" or is_done == "Y":
            break
    
    operasi.update(no_buku,pk,date_add,tahun,judul,penulis)


#2. Tahpan Create Data
def create_console():
    print("\n\n" + "=" *100)
    print("Silahkan Tambahkan data Buku\n")
    judul = input ("Judul\t: ")
    penulis = input("Penulis\t: ")
        
    while(True): #mengulang untuk mengambil data tahun jika diisi dengan salah
        try: #untuk mengatasi synntax eror agar membeirikan pesan bukan membatalkan program

            tahun = int(input("Tahun\t: "))
            #hanya mengisikan angka pada 4 digit nilai dan tidak bisa lebih
            if len(str(tahun)) == 4:
                break
            else:
                print("Hanya Angka yang harus dimasukkan")

        except:
            print("Hanya Angka yang harus dimasukkan")

    operasi.create(tahun,judul,penulis)
    print("\nBerikut adalah data baru anda")
    read_console()

#1. Tahapan Read data
def read_console():
    data_file = operasi.read()
    index = "NO"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
#Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-" *100)
   
#Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break [4]
        print (f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")
#footer
    print("\n" + "="*100)



