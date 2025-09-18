from time import time
from . import Databese
from .Util import random_string
import time
import os

def delete(no_buku):
    print(Databese.DB_NAME)
    try:
        with(open(Databese.DB_NAME,'r')) as file:
            counter = 0
            
            while(True):
                content  = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                
                else:
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("databese error")
    os.remove("data.txt")
    os.rename("data_temp.txt","data.txt")


#3 Tahapan Update data
def update (no_buku,pk,date_add,tahun,judul,penulis):
    data = Databese.TEMPLATE.copy()

    data["pk"] = pk
    data ["date_add"] = date_add
    data["judul"] = judul + Databese.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Databese.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)
    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with(open(Databese.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data * (no_buku-1))
            file.write(data_str)

    except:
        print("error dalam data update")
    

#2. Tahapan Create Data
def create(tahun,judul,penulis):
    data = Databese.TEMPLATE.copy()


    data["pk"] = random_string(6)
    data ["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Databese.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Databese.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    try:
        with open (Databese.DB_NAME,"a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak bisa ditambahkan")



#1. tahapan Read console
def create_firs_data():
    judul =input("Judul: ")
    penulis =input("Penulis: ")
    while(True): #mengulang untuk mengambil data tahun jika diisi dengan salah
        try:
            tahun = int(input("Tahun\t: "))
            #hanya mengisikan angka pada 4 digit nilai dan tidak bisa lebih
            if len(str(tahun)) == 4:
                break
            else:
                print("Hanya Angka yang harus dimasukkan")

        except:
            print("Hanya Angka yang harus dimasukkan")
# tahapan paling awal - bagian membuat Databese
    data = Databese.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data ["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Databese.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Databese.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    try:
        with open (Databese.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udahlah gagal bossss")

#1. tahapan untuk read data
def read(**kwargs): 
    try:
        with open(Databese.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
               index_buku = kwargs["index"]-1
               if index_buku < 0 or index_buku > jumlah_buku:
                   return False
               else:
                   return content[index_buku]
            else:
                return content
    except:
        print("membaca Databese error")
        return False