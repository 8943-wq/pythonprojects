#STRİNGLER

print("STRİNGLER")

#stringlerde en önemli olan ileri düzey kodlarda her mühendise kolaylık yaşatan veri atamadır içiçe yazılan kodlardan print komutunun içine yazarak hata veren kodu kolaylıla düzeltiriz 

kullanıcı = "muhammed"

print(kullanıcı); #böylelikle mesale siber güvenlik alanında çoğul kodlarla indexlerle uğraşırken kolaylık sağlar.

#şuda olurmu olur 
#print("muhammed")

#örnek 2

kullanıcı1 = ("Connelly")
kullanıcı2 = ("Samantha")
print(kullanıcı1 +" "+ kullanıcı2) #arasına boşluklu tırnak koyarak birleştirelecek olan  "connellysamantha" ismini "connelly samantha" şeklinde yazdık 

#örnek 3 

print(kullanıcı[0]) #bu döngü demektir istediğimiz karakteri geri döndürür 0. karakter m harfidir .(pc 0 ve 1 den oluşur 0 pc için 0 dır bizim için 1 dir )

print(kullanıcı[0:4]) #bu şekilde ise 0 ve 4 . karakter arasındaki karakterleri çağırır 0 dahildir ama 4. karakter dahil değildir  

#örnwk 4 
for x1 in range(1,11):
    print(x1)
#örnek 4 aslında örnek 3 ün farklı bir parametresi ama amç aynı 1 dahil 11 değil yani 1 den 10 kadar olan sayılar 

for x4 in range (0,11,2): #0 dam 10 a kadar çift sayıları yazmasaını istiyorsak yanına 2 yazarız ççünkü çift sayı = n ,n+2 olarak gider
    print(x4)
    
    
#örnek 5 
print(kullanıcı.upper()) #kodu çalıştırdığınızda zaten görürsünüz ama ben yinede tanıtayım upper fonksiyonu yazılan stringer değişkenini büyük harflerle yazar 

#örnek 6 

y1 = kullanıcı.lower() #burdaki lower fonksiyonu ise yazılan ve tanımlanan değişkenin bütün harflerini küçültür .

print(y1) #farkettiyseniz burda bir farklılık yaptık . kullanıcı isimli değişkeni y1 e aatadık böylelikle bu tarzdaki  büyük projelerde yazılan kodu çoğaltmak için kolaylık sağlıyacaktır 

#örnek 7 

y2 = kullanıcı.capitalize() # captilaze fonksiyonu ise  yazılan değişkenin ilk hanesini büyük yazar 

print(y2) 

#örnek8 

y3 = kullanıcı.startswith("mu")   #şimdi burdaki fonksiyona bakarsak STARTswith yani şu; atanan değerin başlangıcı parantez içindeki değerse çıktı turue olarak çıkar değilse false 
 
print(y3)

#örnek9 

y4 = kullanıcı.endswith("ed") #aslında bu örnek örnek 8 in benzer parametresi sadece burda kelimeninde kelime anlamından yola çıkarsak ENDswith yani son demek verilen değişkenin sonu ed ile bitiryorsa true .ıktısını alırız 

print(y4) #dipçe olarak şunu eklemek gerek sadece son iki harf yada ilk iki değil son harfide sorgulatabiliriz yazılıma 

#örnek 10 

print(len(kullanıcı)) #** çok önemli olan len fonksiyonu değişkenin kaç karakterden oluştuğunu söyler. bu karakterler=>01234567 dir ve daha önceki örneklerde dediğimiz gibi 0 bizim için 0 dır pc için 1 dir ve pcler 0ve1 den oluşur 

#örnek11 

isim = "ali" 
yas = "20"
print("{} , {} yasindadir".format(isim,yas)) #bu format fonksiyonu da oldukça önemlidir ve bu formasyon excel benzeri programların temelini oluşturur.yani bir şahsın ismini ve yaşını sürekli print kullanarak tanımlarsak vakiit kaybederiz 

#örnek 11.2

isim = "ahmet" 
mesaj = " seni sevmiyorum "
print("{},{}\tdedi...".format(isim,mesaj))




#LİSTELER 


print("LİSTELER")

#öncelikle bir liste nasıl tanımlanır ona birlikte bakalım ;

#örnek 12 

# renkler = ["siyah","beyaz","sarı", "mavi "] #şekilde görüldüğü gibi liste kapalı parantezler arsında oluşturuluyor 

#şimdi bunların liste olup olmadığına bakmak için şöyle bir geçmişe gidelim bakalım doğrumu 
#!unutma yazılan kod türünü belirlerken type fonksiyonu kullanılır python da 

renkler = ["siyah","beyaz","sarı", "mavi ", "yeşil"] #yukarıdaki açıklama örneğini aldık 
print(type(renkler)) #çıktı <class 'list > olucaktır 
print(renkler) #şimdi liste olduğundan emin olduğumuz kodumuzu bi çalıştıralım ( #çıktı ; ['siyah', 'beyaz', 'sarı', 'mavi ', 'yeşil'])

#şimdi stringlerde zaten gördüğümüüz ama yinede çalışma dosyanızda olması için biraz daha oynuyacağız bu listelerle 

#örnek13

print(renkler[1:4]) #şimdi bunu daha öncede söyledik ama hatırlatmakda fayda var bu listedeki [x:y] varya burda x dahil y değil demek yani o liste elemanlarını ona dahil etmiyor 
 #yani örnekte 4 dahil değil 1 den (beyaz) başlayıp maviye kadar devam ediyor . yeşil dahil değil

#örnek 14 
 
print(renkler[1::2]) # bu kod ise kodu parçalama denir. başlangıcı biz seçeriz yani birinci elemandan başlar oda beyazdır yazılan listeyi parçalar ve ikişer ikişer yazar 

#eğer şu şekilde yazarsak print(renkler[::2]) siyahtan okumaya başlar çünkü başa birşey yazmazzask orayı sıfır kabul eder 

#örnek 15

#şimdi bir başka örnekte ise 14.cü örneğin benzeri olacaktır 

print(renkler[1:4:2]) #okunması ise şu 1.elemandna 4.elemana kadar ikişer ikişer elelman yazdıracak 



#ŞİMDİ BAŞKA BİR ALT KONUYA GELDİK ; METODLAR 

#APPEND METODU  : yazılan ve belirlenen listeye yeni bir eleman eklenmesini sağlar 

#marklar = ['monster','arçelik','vestel']

marklar = ['monster','arçelik','vestel']

marklar.append("bu bir append metodu ile yazılmış yazıdır ")

print(marklar) #yazılan metodun çalışması için tekrar printlemek gerekir hemen altına 

#çıktı ; ['monster', 'arçelik', 'vestel', 'bu bir append metodu ile yazılmış yazıdır ']

#İNSERT METODU : appendin daha gelişmiş metodur appende sadece en son elemana ekleriz yazılan elemanı ama insertte belirlenen aralığa ekleriz 

içecekler = ['gazlı','meyvesuyu','alkollü'] #aslında listeyi okuduğunda (print(içecekler)) = ['gazlı','meyvesuyu','alkollü'] inserten sonra = ['gazlı', 'rakı', 'meyvesuyu', 'alkollü']

içecekler.insert(1,"rakı")

print(içecekler) #['siyah', 'turkuaz', 'beyaz', 'sarı', 'mavi ', 'yeşil', 'bu bir append metodu ile yazılmış yazıdır ']



#REMOVE METODU : BİR LİSTEDEN BİR ELEMANI SİLMEYE YARAR 
carname = ['bmw','woksvagen','mercedes']

carname.remove("bmw")

print(carname)

#EXTEND METODU : birden fazla değiişken atammamızı sağlar 

# şimdi öncelikle örneklere geçmeden önce şunu söylemekte fayda var extend metodunu yapacağını apend yapıyordu nasıl yapıyor gösterelim 
şehirler = ["niğde","adana"]

plakalar = ["51","01"]

şehirler.append(plakalar)
print(şehirler) #dediğimiz zaman oluşturduğumuz yeni listeyi append metodu ile ilk oluşturulan şehirler listesine ekleriz 

#ÇIKTI ; ['niğde', 'adana', ['51', '01']]



#POP METODU : yazılan listedeki en son değişkeni silmeye yarar bununlada kalmaz 2. örnekte olan işide yarar ve 2. örneğe uyarlayabilirsiiniz 

kitaptür = ['bilim kurgu','yazılım','aşk']

kitaptür.pop()

print(kitaptür) 

#örnek 2 => siilinen ögeyi bize gösterecek kod dizilimi

meslekler = ['yazılımcı','prof','tıp','pilot']

silinen = meslekler.pop()

print (silinen ) #çıktı = pilot


#REVERSE METODU . yazılan listenin değişkenlerini terssten yazmaya yarar 

dersler = ['fizik','kimya','biyo']

dersler.reverse()

print(dersler)



#SORT VE SORTED METODLAR
#SORT METODU : LİSTEYİ ALFABETTİK SIRAYA GÖRE SIRALAR ; metinsel değişkenler varsa alfabetik , sayısal veriler varsa küççükten büyüğe 

liste3 = ["Adana","Denizli","Bursa","Ceyhan","Edirne","Fatsa","Giresun"]

liste3.sort()

print(liste3)

#şimdi sorted metoduna geçmeden önce şunu sormamız gerek ;
# olıuşturulan bu listeyi tam tersi bir şekilde (a-z ,değil z-a yada küçükten büyüğe değil büyükten küçüğe) nasıl yazaarız ?
# iki yolu var 
#1

print(liste3)
liste3.sort()
liste3.reverse()
print(liste3) #çıktı  :   ['Giresun', 'Fatsa', 'Edirne', 'Denizli', 'Ceyhan', 'Bursa', 'Adana']
#bu 1.parametrenin bir diğer örneği şu : liste3.sort(reverse=true) yine aynı şekilde dçner 

#ANCAK ŞUNU BİLMELİYİZKİ BU YAPTIKLARIMIZLA LİSTE HER ZAMAN AYNI KALMIYOR DEĞİŞİYOR EĞER LİSTEMİZİN DEĞİŞMEİSNİ İSTEMEYİP 
# AMA SIRALANMIŞ HALİNE İHTİYACIMIZ DA VAR İSE İŞTE O ZAMAN SORTED DEVREYE GİRİYOR . LİSTE DEĞİŞMİYOR SIRALANIYOR 



#KÜMELER(SETS)
#AÇIKLAMA:aslında listelere çok benzeyen özellikleri var listelerden ayıran en önde gelen özelliği ise sıralı biçimde olmaması yaani;
#liste {'arba','ev','bahçe'} çıktı :{'ev','araba','bahçe'} veya {'bahçe','araba','ev'} gibi çıkabilir ve her okuttuğumuzda sırası değişen değerler çıkar
#listelerden ayıran diğer özelliik ise süslü parantezli olması ve çeşitli komutların farklı olması 
print("KÜMELER")

#kümelere eleman ekleme (farkındaysanız diğer metodlar liste ile  aynıyken bu kısımda apand yok çünkü sıralanmayan her seferinde değişen kümenin sonuna eleman eklemek saçma olur )

kume = {"muz","kivi","ananas","salatalık"}

kume.add("karpuz")

print(kume) #çıktı={'muz', 'karpuz', 'salatalık', 'ananas', 'kivi'}

#listelerde olan remove metodu yine aynı görevini burda yapar hatta %90 ı farklılık göstermez mantığını anlarsanız %10 luk kısımıda çözersiniz 

#şimdi remove komutunun çalışması için silinmesi gereken elemanın listede veya kümede veya demette olması gerekir yoksa hata alırız .
#hata almak istemiyorssak ama doğru eleman yazılınca silinmesini istiyorssak discard fonksiyonu devreye girer 

#DİSCARD FONKSİYONU : silme işlemide yapmaz olmayan eleman varsa hata da vermez (remove gibi davranmaz)

küme2 =  {"uçak","jet","helikopter"}

küme2.discard("araba") #kümede olmadığı için çıktı yazılan kümeninn aynısıdır .

print(küme2)#eğer araba yerine uçak yazarsak çıktı = {'helikopter', 'jet'} olur 



#Indentation metodu : burda devreye biraz matematik girmesi gerekiyor küme sorularındaki kesişim kümesini (∩) elde etmemizi sağlar 

küme3 = {"türkiye","rusya","amerika","rusya","fıransa","ukrayna","iran"}
küme4 = {"türkiye","rusya","amerika","rusya"}

print(küme3.intersection(küme4)) 

#UNİON METODU : bu da Indentation ' un bir farklı versiyonu yine kümeler konusuna gidecek olursa birleşim kümesi (u) olarak öğrenmemiz gerekir
küme5 = {"kalem","cetvel","saat"}
küme6 = {"masa","telefon","laptop"}
print(küme5.union(küme6))

#DİFFERENCE METODU : bu metod ise yine kğmelerdeki alt başlık olan kümeler arası fark dediğimiz şeydir yani 
#iki farklı kümede aynı olan ve aynı olmayan farklı elemanlar atayalım biri A diğeri B olsun A/B olarak gösterdiğimiz zaman A da olan B de olmayan elemanları verir 

küme7 = {"hidrojen","sodyum","lityum","potasyum","rubinyum","sezyum"}
küme8 = {"hidrojen","lityum","sodyum","potasyum"}

print(küme7.difference(küme8)) #küme 7 de olan ama küme 8 de olmayan yanii çıktı = {'rubinyum', 'sezyum'}

#DOĞRU YANLIŞ (TRUE-FALSE)
küme8 = {"hidrojen","lityum","sodyum","potasyum"}
print("hidrojen"in küme8) #çıktı=true 

#doğruysa yazılan değer true olarak çalıştırır yanlış ise yazılan kümeyi yazdırır kolay bir örnek;

#DİCTİONARİES(SÖZLÜKLER)
print("dictionaries(sözlükler)")
#aslında günlük hayattaki sözlüğe benzetmemiz çok doğru olur çünkü biz sözlükte bir kelime arayınca da aynı mantık oluşuyor 
#python da aynı o mantıkla aklında tutuyor fakat birinciye anahtar sözcük(keys) ikinciye değer (value)sözcüğü diyor 
#anahtarlar string veya integer olmak zorunda ama değer söz öbekleri value denilen kısım herşey olabilir 
#şimdi bi sözlük yazalım 
kisi = {"isim":"ali","yas":25,"cinsiyet":"E","hobiler":["sinema","konser","yazılım"]}
print(kisi)
#printle yazdığımız zaman sadece o sözlük grubunun tamamını yazar 
#istediğimiz sözcükleri yazmak istiyorsak şunu kullanmalıyız 

print(kisi["isim"]) #sadece ali ismini yazdırır 

#şimdi biz sözlük öbeklerinden isim yerine ali değilde ahmet yazdırmak istiyoruz diyelim 
#oda şu şekilde olucak 
kisi["isim"]="ahmet"
print(kisi) # isim artık ahmet oolarak değiştirildi buna sözcük update i denir

# yada en kullanışlı olanı şu 
kisi.update({"isim":"muhammed","yas":30})#en kullanışlı ve kapsamlı olanıdır yeni sözlğk oluşturarak yaparız 


#yeni birşey ekleyip çıkaralım 
#>ekleme
kisi["id"] = 473551122
print(kisi)
#>çıkarma
del kisi["id"]
print(kisi) 

#>for döngüsü ile yazdırma 
for x in kisi :
    print(x)   #yazılırsa keys olan kelimeleri yazdırır 
#value değerlerini yazdırmak için ;
for x in kisi:
    print(kisi[x])    

#sadece keysleri ya da values leri terminale yazdırmasını istiyorsak 
print(kisi.keys()) 

print(kisi.values()) 

#olarak yazdırabiliriz 


#AAAAAAAAAAAAAAA

list = ["kahve","çay","ada çayı","limonata","su"]

q1 = " kahve"
if q1 in list:
    print("menüde var ")
else:
    print("menüde yok ")


a = "Hadley"
b = "Hadley"

if a is b :
    print("a=b")
else:
    print("a != b")
    print(id(a))
    print(id(b))