#ÖRNEK-1 DERS NOTU 

print("MERHABA İTÜLÜ ")
vize = input("vize notunuzu giriniz : ")
final = input("final notunu giriniz : ") 
ortalama = int(vize)*0.4 + int(final)*0.6 
if ortalama >=50  :
    harf = "   GEÇTİNİZ"
elif ortalama<50 : 
    harf ="   DAHA ÇOK ÇALIŞMANIZ GEREK..."     
print("DÖNEM SONU ORTALAMANIZ : {0}".format(ortalama)+harf) 