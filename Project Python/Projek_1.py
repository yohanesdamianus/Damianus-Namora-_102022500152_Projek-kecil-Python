#membuat databese pertama
import os
import CRUD as CRUD
if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear") #Case digunakan untuk membandingkan atau mencocokkan nilai dalam kode yang dideklarasikan
        case "nt": os.system("cls")
    print("Selamat Datang di Program ")
    print("DATABESE PERPUSTAKAAN")
    print("=====================")    

    #Chechk databese itu ada di CRUD
    CRUD.init_console()

    
    

    while (True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        print("Selamat Datang di Program ")
        print("DATABESE PERPUSTAKAAN")
        print("===========================")


        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        
        user_optional  = input("masukkan opsi: ")
        

        match user_optional: # match adalah syntax mencocokan suatu data yang ada atau suatu perintah yang ada dan yang akan dibuat

            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_done = input("apakah selesai (y/n)?")
        if is_done == "y" or is_done == "Y":
            break
    

    print("program berakhir, terimakasih kaka")
