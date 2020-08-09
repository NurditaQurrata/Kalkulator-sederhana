def penjumlahan():
    print("PENJUMLAHAN)")
    print("\n")
    a=float(input("masukkan angka pertama : "))
    b=float(input("masukkan angka kedua : "))
    print("\n")
    a=a+b
    print("HASIL = ",a)
    
def pengurangan():
    print("PENGURANGAN")
    print("\n")
    a=float(input("masukkan angka pertama : "))
    b=float(input("masukkan angka kedua : "))
    print("\n")
    a=a-b
    print("HASIL = ",a)

def perkalian():
    print("PERKALIAN")
    print("\n")
    a=float(input("masukkan angka pertama : "))
    b=float(input("masukkan angka kedua : "))
    print("\n")
    a=a*b
    print("HASIL = ",a)

def pembagian():
    print("PEMBAGIAN")
    print("\n")
    a=float(input("masukkan angka pertama : "))
    b=float(input("masukkan angka kedua : "))
    print("\n")
    a=a/b
    print("HASIL = ",a)

   
while True:
    print("opsi matematika")
    print(">>>>>>>>>>>>>>>>")
    print("[1] PENJUMLAHAN")
    print("[2] PENGURANGAN")
    print("[3] PERKALIAN")
    print("[4] PEMBAGIAN")
    print("<<<<<<<<<<<<<<<<")
    print("\n")
    opsi=int(input("Silahkan pilih nomor opsi yang akan dikerjakan : "))
    print("/////////////////////////////////////////////////")
    if opsi == 1:
        penjumlahan()
        print("----------------------------------------------------")
    elif opsi == 2:
        pengurangan()
        print("----------------------------------------------------")
    elif opsi == 3:
        perkalian()
        print("----------------------------------------------------")
    elif opsi == 4:
        pembagian()
        print("----------------------------------------------------")
    else:
        print("MAAF NOMOR YANG ANDA MASUKKAN TIDAK ADA DALAM OPSI,MOHON DENGAN NOMOR YANG HANYA ADA PADA OPSI!!!")

    p=input("APAKAH ANDA MAU MENGGUNAKAN KALKULATOR LAGI? (Y/T) : ")
    print("\n")
    if not(p == "y" or p == "Y"):
        break
print("-------------------------------------------------------")
print("TERIMA KASIH SUDAH MENGGUNAKAN APLIKASI KALKULATOR SAYA")
print("-------------------------------------------------------")

