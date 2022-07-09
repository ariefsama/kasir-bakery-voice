# Project Kasir Bakery (Python)
# Preparation
import datetime
x = datetime.datetime.now()

import playsound
def play(nama_file):
    playsound.playsound(nama_file)

from gtts import gTTS
def suara(text, lang="id"):
    text = bicara
    suara = gTTS(text=text, lang=lang)
    suara.save(nama_file)

def strip1():
    print("===============================================================================")
def strip2():
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
def strip3():
    print("_______________________________________________________________________________")
def menu():
    strip1()
    print("Daftar Menu".center(75))
    strip1()
    print("\t*Kode*\t\t\t*Nama Item*\t\t\t*Harga*\t")
    strip1()
    print("<<<BAKERY>>>".center(75))
    print("")
    print("\t| 1 |\t\t\tCUP CAKE\t\t\tRp. 50000\t")
    print("\t| 2 |\t\t\tDONUTS\t\t\t\tRp. 55000\t")
    print("\t| 3 |\t\t\tBROWNIES\t\t\tRp. 45000\t")
    print("")
    strip2()
    print("<<<==PROMO==>>>".center(75))
    print("")
    print("Beli CUP CAKE Minimal 3 Bungkus akan Mendapatkan DISKON 20%".center(75))
    print("")
    strip2()

nama_menu = []
jumlah_menu = []
harga_menu = []
total_menu = []
harga_total = 0
total_item = 0
banyak_pembelian = 0
print("")
print("Selamat Datang di UBSI Bakery".center(75))

nama_file = "suara.mp3"
bicara = "Selamat Datang di UBSI Bakery, Silahkan masukkan nama anda!"
suara(bicara)
play(nama_file)

    
print("")
#input
customer = input("Nama Customer\t: ")

bicara = "Hallo" + customer
suara(bicara)
play(nama_file)

print("")
while True:
    menu() 
    bicara = "Silahkan pilih kode menu yang ingin anda pesan! , setelah itu masukkan banyaknya jumlah pembelian!"
    suara(bicara)
    play(nama_file)

    kode = input("Pilih Kode\t : ")
    if kode == "1":
        nama = ("CUP CAKE")
        nama_menu.append(nama) 
        harga = 50000
        jumlah = int(input("Jumlah Pembelian : "))
        banyak_pembelian += 1
        if jumlah >= 3:
            jumlah_menu.append(jumlah)
            diskon = 20 / 100
            harga_diskon = harga - (harga * diskon)
            harga_menu.append(harga_diskon)
            total = harga_diskon * jumlah
            total_menu.append(total)
            harga_total += total

            print("")
            print("Anda mendapatkan diskon sebesar 20%")
            print("Anda memilih ", nama, "seharga ", int(harga_diskon), "Berjumlah ", jumlah)
            print("Total ", int(total))

            bicara = "Anda mendapatkan diskon sebesar 20% . Anda memilih cup caek, seharga 40.000 rupiah, Berjumlah "+ str(jumlah)+ ". totalnya menjadi "+ str(total)+"rupiah."
            suara(bicara)
            play(nama_file)

        else:
            total_menu.append(total)
            harga_total += total
            jumlah_menu.append(jumlah)
            harga_menu.append(harga)
            total = harga * jumlah
            total_menu.append(total)
            harga_total += total
            print("")
            print("Anda Tidak Mendapat Diskon")
            print("")
            print("Anda memilih ", nama, "seharga ", int(harga), "Berjumlah " , jumlah)
            print("Total ", total)

            bicara = "Anda Tidak mendapat diskon. Anda memilih cup kaeg, seharga 50.000 rupiah, Berjumlah "+ str(jumlah)+ ". totalnya menjadi "+ str(total)+"rupiah."
            suara(bicara)
            play(nama_file)

    elif kode == "2":
        nama = ("DONUTS  ")
        nama_menu.append(nama)
        harga = 55000
        harga_menu.append(harga)
        banyak_pembelian += 1
        jumlah = int(input("Jumlah Pembelian : "))
        jumlah_menu.append(jumlah)
        total = harga * jumlah
        total_menu.append(total)
        harga_total += harga * jumlah

        print("")
        print("Anda memilih ", nama, "seharga ", harga, "Dengan Jumlah ", jumlah)
        print("total ", total)

        bicara = "Anda memilih Donat, seharga 55.000 rupiah, Berjumlah "+ str(jumlah)+ ". totalnya menjadi "+ str(total) +"rupiah."
        suara(bicara)
        play(nama_file)

    
    elif kode == "3":
        nama = ("BROWNIES")
        nama_menu.append(nama)
        harga = 45000
        harga_menu.append(harga)
        banyak_pembelian += 1
        jumlah = int(input("Jumlah Pembelian : "))
        jumlah_menu.append(jumlah)
        total = harga * jumlah
        total_menu.append(total)
        harga_total += harga * jumlah
        print("")
        print("Anda memilih ", nama ,"seharga ", harga,"Dengan Jumlah ", jumlah)
        print("total ", total)

        bicara = "Anda memilih Brownis, seharga 45.000 rupiah, Berjumlah "+ str(jumlah)+ ". totalnya menjadi "+ str(total)+"rupiah."
        suara(bicara)
        play(nama_file)
    
    else:
        print("Maaf Kode tersebut tidak ada dalam Daftar Menu")
        bicara = "Maaf, Kode tersebut tidak ada dalam Daftar Menu"
        suara(bicara)
        play(nama_file)
        

    bicara = "tekan y! jika masih ingin berbelanja,dan tekan n! jika sudah selesai belanja"
    suara(bicara)
    play(nama_file)
   
    lanjut = input("lanjut Belanja? (Y/n): ")
    if lanjut == "n" or lanjut == "N":
        print("")
        break
    else:
        print("")
        
#output
print("")
print("PT.UBSI Bakery".center(75))
print("JL.Merdeka Bogor".center(75))
print("Telp.(021) 134 225 65".center(75))
print("")
strip1()
print("Customer\t: ", customer)
print("Tanggal\t\t: ", x.strftime("%a %d %b %G %X"))
strip2()
print("\tHarga\t\t\tQty\t\t\tSubtotal")
print("")

for i in range(banyak_pembelian):
     print("\t" ,(nama_menu[i]))
     print("\tRp. %i\t\t%i\t\t\tRp. %i"%(harga_menu[i],jumlah_menu[i],total_menu[i]))
     print("")

strip2()
print("Total Keseluruhan\t\t\t\t\tRp.", int(harga_total))

bicara = "Total Keseluruhan belanja Anda senilai " + str(harga_total) +"Rupiah.silahkan masukkan uang pembayaran anda"
suara(bicara)
play(nama_file)

bayar = int(input("Pembayaran Tunai\t\t\t\t\tRp. "))
kembalian = bayar - harga_total

if bayar >= harga_total:
    print("Kembalian\t\t\t\t\t\tRp.", int(kembalian))
    strip1()
    print("Terimakasih Atas Kunjungan Anda".center(75))
    print("Silahkan Datang Kembali!".center(75))

    bicara = "uang pembayaran anda senilai" + str(bayar) + "Rupiah. jadi, kembalian anda sebesar" + str(kembalian)+"Rupiah. terima kasih atas kunjungan anda. silahkan datang kembali"
    suara(bicara)
    play(nama_file)

else:
    print("")
    print("Maaf Uang Anda kurang\t : Rp." , int(kembalian))
    print("")
    print("Silahkan coba dilain waktu!")
    print("")
    print("Terimakasih Atas Kunjungan Anda".center(75))
    print("Silahkan Datang Kembali!".center(75))

    bicara = "uang pembayaran anda senilai" + str(bayar) + "Rupiah.maaf ,uang pembayaran anda kurang senilai" + str(kembalian)+"rupiah"
    suara(bicara)
    play(nama_file)
    bicara = "silahkan coba dilain waktu!"
    suara(bicara)
    play(nama_file)
    bicara = "terima kasih atas kunjungan anda. silahkan datang kembali"
    suara(bicara)
    play(nama_file)