#19410051072-Sümeyye Karakaş YBS NORMAL ÖĞRETİM 3.SINIF
sayi_kodlari = [32 ,33, 34,35,36 ,37 ,38 , 39 ,40, 41 ,42 ,43 ,44 ,45, 46 ,47, 48 ,49, 50,
                51 ,52 ,53 ,54,55 ,56 ,57 ,58 ,59, 60, 61 ,62 ,63 ,64 ,65, 66, 67, 68 ,69, 70,
                71, 72, 73 ,74, 75 ,76 ,77,78 ,79 ,80, 81, 82 ,83, 84, 85 ,86 ,87, 88 ,89 ,90,
                91, 92 ,93, 94 , 95, 96, 97, 98 ,99, 100 ,101 ,102, 103, 104 ,105 ,106 ,107 ,
                108, 109,110,111, 112 ,113 ,114 ,115 ,116 ,117 ,118 ,119,120 ,121, 122 ,123 ,
                124, 125 ,126 ,127 , 128 ,129, 130, 131, 132 ,133, 134 ,135 ,136 ,137 ,138,
                139 ,140 ,141 ,142 ,143,144,145, 146 ,147, 148, 149, 150 ,151 ,152, 153 ,154,
                155, 156, 157, 158,159, 160, 161 ,162, 163, 164 ,165,166, 167 ,168, 169, 170, 171, 172]
#ascıı değerlerinin onluk sisteme göre sıra numaralarını sırasıyla yazdım.

def sifre(text,key):
    sifreli_metin=""
    anahtar_uzunlugu = len(key)
    for indis,x in enumerate(text):
        acik_karakter=x
        anahtar_karakter=key[indis%anahtar_uzunlugu]
        acik_ascii = ord(acik_karakter)  #ord kullanmamızın sebebi girilen değerin temsil ettiği integer değerini almaktır.
        ascii_anahtari = ord(anahtar_karakter)
        anahtar_kod = sayi_kodlari[ascii_anahtari]
        y = anahtar_kod + acik_ascii  ##anahtar girişinden alınan değerin ascii kodunun yerinde bulunan0 sayi_kodları dizisindeki sayı ile şifrelenmek istenen metnin ascii kodları toplanır.
        bolumunden_kalan = y%26 #elde edilen toplam değer ie ingilizce alfabede 26 değer bulunduğu için elde edilen değeri 26 sayısına böleriz.
        sifreli_karakter = chr(bolumunden_kalan+97) # ve bölümünden kalan değeri ASCİİ kodunda 97 den itibaren küçük harfler başladğı için kalan değere 97 ekleriz.
        sifreli_metin += sifreli_karakter # ve bu durumda yeni bir ascii kod elde ederiz örneğin 97+5=102=  f harfi.
    return sifreli_metin # bu adımlar şifrelenmek istenen metnin her karakterine uygulanır.

def coz(text,key): #deşifre işleminde şifreleme işleminde kullanılan anaht ve elde edilen şifrenin girilmesi yeterlidir.
    yeni_kelime = ""
    anahtar_uzunlugu = len(key)
    for indis, x in enumerate(text):
        sifreli_karakter = x
        anahtar_karakter = key[indis%anahtar_uzunlugu]
        sifreli_ascii = ord(sifreli_karakter) #şifrelenmiş metnin karakterlerinin integer olarak değerini elde ederiz
        ascii_anahtari = ord(anahtar_karakter) # aynı şekilde anahtak karakterlerinin integer olarak değerini alırız.
        anahtar_kod = sayi_kodlari[ascii_anahtari]
        z = sifreli_ascii-97  #şifrelenmiş olan karakterin ascii kodunu -97 den çıkarıız
        if z==0:
            cikar = (26 - anahtar_kod%26)  #z değerinin 0 olması halinde yapılacak işlem
        else:
            cikar = (z - anahtar_kod%26)
        katsayi = int((122-cikar)/26)  # çıkan değeri 122 den çıkarırz çünkü son ascii küçük hraf karakteri. integer vermemizin sebebi virgüllü sayı çıkma ihtimalini önleme
        yeni_ascii = 26*katsayi+cikar   #katsayidan çıkan sonucu 26 ile toplayıp cıkar'dan aldığımız değerden çıkaırız.
        yeni_karakter= chr(yeni_ascii) #yeni ascii değerimizi bulmuş oluruz.
        yeni_kelime += yeni_karakter #bulduğumuz değeri elde etmek istediğimiz değere ekleriz
    return yeni_kelime # bunu her karakter için tekrarlarız. ve şifrelenmemiş metni elde ederiz.


def char_tr(text):  #şifreleme ingilzce alfabeye göre yapılmıştır.
    text = text.lower() #eğer kullanıcı türkçe karakterler girerse replace komutuyla harfi değiştiririz.
    text=text.replace("ç","c")
    text=text.replace("ğ","g")
    text=text.replace("ı","i")
    text=text.replace("ö","o")
    text=text.replace("ş","s")
    text=text.replace("ü","u")
    return text
while True: #kullanıcın yapmak istediği işlemlere yol gösteren aşamalar.
    print("\n\t--ANAHTARLI ŞİFRELEME--")
    print("\tŞifrelemek istediğiniz metni giriniz --- (1)")
    print("\tŞifreli metni Çöz --- (2)")
    print("\tÇıkış --- (0)")
    try:
        secenek = int(input("Seçmek istediğiniz değer: "))
    except:
        print("Lütfen Bir Tamsayı Giriniz!")
        secenek=-1
    if secenek==1:
        text = input("Açık Metin:")
        text = char_tr(text)
        key = input("Anahtar:")
        key = char_tr(key)
        print("Açık metin:", text)
        kelimeler=text.split(" ")
        sifreli_metin=""
        for i in kelimeler:
            sifreli_kelime = sifre(i,key)
            sifreli_metin += sifreli_kelime + " "
        print("\n***Açık metin",key,"anahtarı ile şifrelendi.***")
        print("Şifreli metin:",sifreli_metin)
    elif secenek==2:
        text = input("Şifreli Metin:")
        text=char_tr(text)
        key = input("Anahtar:")
        key = char_tr(key)
        print("Şifreli metin:", text)
        kelimeler=text.split(" ")
        desifre_metin = ""
        for i in kelimeler:
            yeni_kelime = coz(i,key)
            desifre_metin += yeni_kelime + " "
        print("\n***Şifreli metin",key,"anahtarı ile deşifre edildi.***")
        print("Deşifre Edilmiş Metin:",desifre_metin)
    elif secenek==0:
        print("Çıkış yapıldı.")
        break
    else:
        print("Doğru bir seçim yapmadınız.")


