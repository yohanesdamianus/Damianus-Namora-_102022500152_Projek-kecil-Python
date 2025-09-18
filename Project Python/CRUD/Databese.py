from . import operasi
DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "xxxxxx",#pk adalah 'prime key' yang biasa digunakan dalam databese
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
    
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Databese tersedia, init done")
    except:
        print("databese tidak ditemukan, silahkan membuat databese baru")
        operasi.create_firs_data()