#format komutu
print("Benim adım==>{},yaşım==>{}".format('emin',16)) #format komutu değişkenlerde işimize oldukça yarar çünkü değişebilen oldukları için rahatça değiştirebiliriz 
#format komutunda index:aslında pc nin otamatik olarak yaptığını burada biz değiştiriyoruz birinci örnekte baştan başlayıp ikinci değişkene kadar sırasıyla yazdırdı fakat bunu değiştirmek istersek süslü parantezin içine index atarız 
print("Benim adım==>{0},yaşım==>{1}".format('emin',16)) 
print("Benim adım==>{1},yaşım==>{0}".format('emin',16)) 

baslik1 = 'HOŞGELDİN,KULLANICI'
#string(yaani sözel veriler için kullanılır ve string için veriyi tanımlarken iki tırnak kullanılması gerekir)
baslik2 = "HABERİN" "OLSUNNN!"
baslik3 = "BAYRAMA""ÖZEL>"
#>
vade = 12
faizorani = 1.47
 #ikiside sayısal veridir ve sayısal verilerde tırnak kullanılmaz.
 #"vade"tam sayıdır 
#faizorani ise ondalık sayıdır ondalık sayılarda virgül kullanılmaz 
   #"vade">integer
#"faizorani">float
      #"type" veri türünü belirlemek için kullanılır
print(baslik1)
print(baslik2) 
print(baslik3)
print(vade,"ay")
print("%",faizorani,"faiz","seçenekleri","sunuyoruz")
print(type(baslik1))
print(type(baslik2))
print(type(baslik3))
print(type(vade))
print(type(faizorani))
#"type"verinin türünü belirlememize yarar.
#(+) kullanımı string veri tipinde yazılan verileri birleştirir(örnek-1)
#fakat float ve integer verilerinde bildiğimiz toplama işlemi yapar (örnek-2)

print("örnek1;")

mesaj = "hoşgeldin"
müsteriadi = "Gunnar"
müsterisoyadi = "createdAt"
müsterino = "(271) 710-6259"

x = "customer;firstname,lastname " " and " " phone" "namber:"

print(x)
 
x1 = müsteriadi+","+" "+müsterisoyadi+","+" "+müsterino  #değişkene sadece bir element atarsan onu her yerde kolaylıkla print fonk. içine yazılır 

print(x1)

print("örnek2;")

print(20+10)

#şart blokları

dolarkurubugun = 8.75
dolarkurudun = 8.75

if dolarkurubugun<dolarkurudun:
    print("azalış " " oku")
    print("bitti")
    
elif dolarkurubugun>dolarkurudun:
    print("Artış " " oku")
    print("bitti")

else:
    print("eşittir " " oku")
    
#if ve elif şart komututudur istenilen değer karşılanıyorsa verilen verinin çıktısı alınır ama ikiside bu değeri karşılamıyorsa else devrye girer ve verilen veriyi çıktıda alırız

#dizeler 

krediler = ["hızlı kredi","maaşını halbanktan alanlara özel kredi","mutlu emekli ihtiyaç kredisi"]

print(krediler[0]) #diziler 0 dan başlar
print(krediler[1])
print(krediler[2])

print(len(krediler)) #dizelerin içinde kaç tane eleman olduğunu bilmek için len fonksiyonu kullanılır

#dizelerde atama 
krediler[0] = "çabuuk kredi"
print(krediler)

#başka bir zaman dizeleri böyle numara vererek sıralamak zor gelicek evet elle yazılır mı yazılır 
#ama büyük projelerde bu oldukça zor onun için for döngüsünü kullanıyoruz 

#"for - in "döngüsü

krediler = ["hızlı kredi","maaşını halbanktan alanlara özel kredi","mutlu emekli ihtiyaç kredisi"]

for kredi in krediler:
    print(kredi)
#for-in döngüsü verilen liste elemanlarını gezer burda "krediler" mesela verilen liste kredi ise takma attır yani for - in gezer gezdiği değeri o an görmek için verdiğimiz takma isimdir "kredi" buna da alias denir

#for döngüsü sadece dizelerle ilgili değildir birşeyi belirli bir sayıda yapmak içinde kullanırız

for x in range(1,10): #1 dahil 10 dahil değil demek yani , başta 1 sonda 10 olmasını istiyorsak (1,11) yazılması gerekiyor
    print(x)
    
print("-")
    
for x2 in range(10): 
    print(x2)
    
print("-")
    
for x3 in range(3,15):
    print(x3)
    
print("-")

for x4 in range (0,11,2): #0 dam 10 a kadar çift sayıları yazmasaını istiyorsak yanına 2 yazarız ççünkü çift sayı = n ,n+2 olarak gider
    print(x4)

def kredilerilistele():
    krediler = ["hızlı kredi","maaşını halbanktan alanlara özel kredi","mutlu emekli ihtiyaç kredisi"]
    for x in krediler:
        print(kredi)

kredilerilistele();

kredilerilistele();

kredilerilistele();

kredilerilistele();

kredilerilistele();

kredilerilistele();

kredilerilistele();
    