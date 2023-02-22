#ÖRNEK-1 DERS NOTU 

#print("MERHABA İTÜLÜ ")
#vize = input("vize notunuzu giriniz : ")
#final = input("final notunu giriniz : ") 
#ortalama = int(vize)*0.4 + int(final)*0.6 
#if ortalama >=50  :
 #   harf = "   GEÇTİNİZ"
#elif ortalama<50 : 
#    harf ="   DAHA ÇOK ÇALIŞMANIZ GEREK..."     
#print("DÖNEM SONU ORTALAMANIZ : {0}".format(ortalama)+harf) 

#ÖRNEK-2 MAAŞIN ZAM ORANINA GÖRE BELİRLENMESİ 

print("YENİ YIL ENFLASYON ORANINA GÖRE DÜZENLENEN MAAŞ ÖĞRENME SAYFASINA HOŞGELDİNİZ")

print ("1 = maaş öğrenme")
print("2 = geçersiz ve diğer")
x1 = int(input("yapmak istediğiniz işlemi kısaca yazınız : "))



if (x1)<=1 :
    isim =input("isminiz :")
elif (x1)>=2 :
    print("lütfen geçerli işlem giriniz!")        



soyisim = input("soyisminiz : ")

vatandaslıkno = input("Türkiye cumhuriyeti vatandaşlık numaranız : ")

ö1 = input("öğrenim gördüğünüz bölüm :")

ö2 = int(input("kaç yıl öğrenim gördünüz : "))

print("hoşgeldiniz" + " " +  isim +" "+ soyisim )

print("yeni yılınız kutlu olsun yeni yıl maaşınızı hesaplamak için enter tuşuna tıklayınız ")

maas = input("mevcut maaşınızı giriniz :")

if int(ö2) < 6 :
    zam = 40
    
elif int(ö2) > 6 : 
    zam = 50
           
yenımaas = int(maas)+(int(maas)*int(zam)/100)      


print("yeni yıl maaşınız : {0} ".format(int(yenımaas)))

