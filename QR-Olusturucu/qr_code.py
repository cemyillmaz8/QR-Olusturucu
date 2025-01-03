import tkinter as tk
from tkinter import filedialog 
import pyqrcode
from pyqrcode import QRCode


def url_kodu_olustur():
    url = url_girdi.get()

    if url:
        #qrcode oluşturacak aldığımız urlye göre
        qr_url = pyqrcode.create(url)

        #dosyayı nereye kaydedilsin sorusunu sordurtacak
        #svg şeklinde kaydedicek ve svg dısında hiçbir şekile kaydetmeyecek
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG dosyaları","*.svg")])

        if dosya_yolu:
            #dosyayı svg ye dönüştürüp kaydetti qr code boyutu 8
            qr_url.svg(dosya_yolu, scale=8)

            durum_etiketi.config(text="qr code oluşturuldu ve kaydedildi!")

#tasarım alanı
uygulama_pencere = tk.Tk()  
uygulama_pencere.title("QR code oluşturucu")

etiket = tk.Label(uygulama_pencere, text= "URL adresini girin:")

#kullanıcının veriyi giriş yapacağı yer(entry ile) ve bunu uygulama penceresine ekliyor
url_girdi = tk.Entry(uygulama_pencere, width=40)
qr_kod_olustur_butonu = tk.Button(uygulama_pencere, text="QR kod oluştur",command=url_kodu_olustur)
durum_etiketi = tk.Label(uygulama_pencere,text="")


etiket.grid(row=0,column=0,padx=10,pady=10)    
url_girdi.grid(row=0,column=1,padx=10,pady=10)
qr_kod_olustur_butonu.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)









uygulama_pencere.mainloop()