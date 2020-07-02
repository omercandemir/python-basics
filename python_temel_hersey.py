# ============= User Sistemi =========================
class User:
    def __init__(self, isim, email, yas):
     self.isim = isim
     self.email = email
     self.yas = yas

    def selamla(self):
        print("selamlar, aramiza hosgeldin! {isim}".format(isim=self.isim))


class Musteri(User):
    def __init__(self, isim, email, yas):
        self.isim = isim
        self.email = email
        self.yas = yas
        self.bakiye = 0

    def bakiyemiSorgula(self):
        return self.bakiye

    def bakiyemiArttir(self):
        self.bakiye += 10
        print("Bakiyeniz 10 TL arttirildi!")

# Buraya girdiğimiz kodlar çıktıyı etkiler.
musteri1 = Musteri("Hasan", "hasan@gmail.com", 50)
musteri1.bakiyemiArttir()
print("Mevcut bakiyeniz:", musteri1.bakiyemiSorgula())

# ===========================================================
"""
kullanici1 = User("Omer", "omercn28@gmail.com", 18)
kullanici1.selamla()
kullanici2 = User("Alperen", "storluperde@gmail.com", 17)
kullanici2.selamla()
"""

# print(kullanici1.email)

# ===========================================================
"""
baslangic = 3
while baslangic != 0: # başlangıç 0'a eşit değilse baslangıctan -1 düş ve printle.
    baslangic = baslangic - 1
    print(baslangic)
"""
# ===========================================================
"""
meyveler = ["elma", "armut", "karpuz"]

for meyve in meyveler:
    if meyve == "armut":
        continue # armutu gördüğümüz an sonrakinden devam et.
    print(meyve)
"""
# ===========================================================
"""
meyveler = ["elma", "armut", "karpuz"]

for meyve in meyveler:
    if meyve == "karpuz":
        break # karpuza geldiğinde kesmemize yarar.
    print(meyve)
"""
# ===========================================================
"""
meyveler = ["elma", "armut", "karpuz"]

for meyve in meyveler:
    print(meyve)
    if meyve in ["elma", "karpuz"]: # in yerine == de kullanabiliriz ama yalnızca bir değişken kullanacaksak.
        print("ooo ne geldi!")
"""
# ===========================================================
"""
sayilar = [1, 2, 3]
aradigimSayi = 4

if aradigimSayi in sayilar:
    print("Aradiginiz sayi, sayi dizisinin icindedir.")

else:
    print("Aradiginiz sayi sayi dizisinin icinde degildir.")
"""
# ===========================================================
"""
x = 20

if x == 20 or x > 20: # or yada anlamına gelmekte.
    print("x 20'ye esit ya da buyuktur.")
"""
# ===========================================================
"""
x = 21
if x > 20: # eğer x 20'den büyükse
    print("X 20'den buyuktur.")

elif x == 20: # yok eğer x 20'ye eşitse
    print("X 20'ye esittir.")

else: # hiçbiri tutmazsa
    print("X 20'den kucuktur.")
"""
# ===========================================================
"""
# def = define yani tanımla
def toplam(sayi1, sayi2):
    return sayi1 + sayi2

print(toplam(13, 22))
"""

# ===========================================================
"""
insan = {
    "ilk_isim": "Omer",
    "soy_isim": "Demir",
    "yas": 18
}
del(insan["yas"]) # Yaş değerini silmemize yarar.
print(insan)
print(insan["ilk_isim"]) # Bir değer öğrenirken kullanılır.
print(insan["soy_isim"]) # Bir değer öğrenirken kullanılır.

"""

# ===========================================================
"""
kume = {"Elma", "Armut", "Karpuz"}
kume.add("Kavun")
kume.remove("Armut")
print(kume)
"""

# ===========================================================
"""
meyveler = ["Karpuz", "Mandalina", "Armut"]
meyveler[0] = "Elma" #ir Meyvelerin birinci elemanını elma olarak değiştirmemize yaradı.
print(meyveler)
"""


# ===========================================================
"""
meyveler = ["Karpuz", "Mandalina", "Armut"]
meyveler.sort() # Çıktının alfabetik sıraya göre dizilmesine yarıyor.
meyveler.reverse() # Çıktının sırasının tersine dönmesine yarar.
print(meyveler)
"""


# ===========================================================
"""
meyveler = ["Elma", "Armut", "Portakal"]
meyveler.append("Muz") # Değişkene sonradan bir değer ekleme.
meyveler.remove("Elma") # Değişkenler arasında elmayı kaldırır.
meyveler.insert(0, "Karpuz") # İnstert sayesinde değişkenin istediğimiz noktasına yeni değişken ekliyebiliriz.

print(meyveler)
"""
# ======================== F String ========================
"""
isim = "OmerCan"
yas = 18

print(f"{isim} {yas} yasindadir.")
"""

# ===========================================================

"""
sayi1, sayi2, sayi3 = 5, 10, 15

karakterler = "15" # string
rakamlar = 25 # int
virgullusayi = 2.5 # float
dogruyanlis = True # boolean


print(sayi1, sayi2, sayi3)
print(int(karakterler) + rakamlar) #karakter içerisinde bulunan sayılar ile işlem yapmak istiyorsak
# çıktıya int fonksiyonunu tanımlamalıyız.
"""

# ========================================================================

"""
name = 'OmerCN Software'

print(len(name)) # len kodu değişkenimizin içindeki karakter sayısını sayar.
print(name[1]) # [1] = 2. karakterinin ne olduğunun çıktısını almamıza yarar.
print(name[0:9]) # [0:9] = 0 dan 9. karaktere kadar çıktısını verir.

"""