#SÜMEYYE KARAKAŞ 19410051072 NORMAL ÖĞRETİM YBS 3.SINIF SORU1

#şifreleme sisteminin çalışma mantığı: Örneğin şifrelemek isteğimiz metin Z harfi olsun bu da bizim alfabemizde 61. sırada.
#daha sonra anahtar değerimizi de 1 verelim
# yapılacak işlem 61+1= 62, 62/61 = 1 yani alfabemizde ki 1 değerine denk geliyor a= 0 b= 1 bu durumda şifrelenmiş metnimiz b harfi oluyor.
#ŞİFRELEME
giris = input('lütfen şifrelemek istediğiniz metni rakam,büyük harf ya da küçük harf olarak giriniz:')
alfabe= "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #alfabede bulunan harflerin tamamını büyük harf ve küçük har olarak bir string olarak tanımladık
anahtar= input("lütfen anahtarı 8 rakam olacak şekilde giriniz:") #içine ek olarak rakamları da yerleştrdik. kullanıcı isterse rakam girip onu da şifreleyebilir.
sifre=''

for i in giris:
  girisdurum= alfabe.find(i)  #şifrelenecek metindeki karakterlerin indis numarasını bulur.
  anahtardurum=(girisdurum + int(anahtar) ) % 61 #alfabe karakterleri toplam 61 olduğu için 61 değerini yazdık. # daha sonrasında
#karakterden bulduğumuz indis değerini anahtardaki sayı ile toplarız. çıkan sonucu 61 e böleriz. bunun sonucunda elde ettiğimiz değer bizim şifrelenmiş il karakterimiz olur
  sifre+=alfabe [anahtardurum] # şifreleencek metin bitene kadar işlemi tekrarlar ve şifrelenmiş metine ekleriz.
sonuc = (sifre)
print('Şifrelenmiş metin: ' + (sonuc) )
print('Şifreleme Anahtarı: '+ (anahtar) )
#metin şifreleme aracı yani anahtar rakam ile gerçekleştirilmektedir.

#ŞİFRE ÇÖZME
import random
for i in range(1):
    anahtardeger = (random.randint(11111111111, 999999999999999)) #aralık belirtir
print("")
giris = input("Şifre kırmak istediğiniz metni giriniz")
alfabe = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
anahtar = input("Lütfen anahtarı 8 rakam olacak şekilde giriniz")
sifre=''
for i in giris:
    giris_durum = alfabe.find(i)
    anahtar_durum = (giris_durum + -int(anahtar) ) % 61 #alfabe karakterleri toplam 61 olduğu için 61 değerini yazıp böldük
    sifre+=alfabe [anahtar_durum]
sonuc = (sifre)
anahtarsonuc= (anahtardeger)

print('Çözülen metin : '+ (sonuc) )

