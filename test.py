import playsound
def play(nama_file):
    playsound.playsound(nama_file)

from gtts import gTTS
def suara(text, lang="id"):
    text = bicara
    suara = gTTS(text=text, lang=lang)
    suara.save(nama_file)

nama_file = "suara.mp3"
bicara = "import datetime x = datetime dot datetime.now kurung buka kurung tutup. nama_menu = kurung siku buka, kurung siku tutup, jumlah_menu = kurung siku buka, kurung siku tutup, harga_menu = kurung siku buka, kurung siku tutup,total_menu = kurung siku buka, kurung siku tutup,harga_total = 0, total_item = 0, banyak_pembelian = 0."
suara(bicara)
play(nama_file)