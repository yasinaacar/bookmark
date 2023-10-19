import fonksiyonlar

while True:
    try:
        #choose the process
        islem_sec=int(input("1)Yeni Kitap Oluştur\t2)Kitaba Yeni Not Ekle\t3)Kitap Oku\t4)Kitap Sil\n\tYapmak İstediğiniz İşlemi Seçiniz: "))
    except ValueError:
        print("Lütfen sadece yapmak istediğiniz işlemin yanında gördüğünüz rakamı girin: ")
        continue
    #create book
    if islem_sec==1:
        fonksiyonlar.yeni_kitap_olustur()
    #add note
    elif islem_sec==2:
        fonksiyonlar.icerik_ekle()
    #read the book    
    elif islem_sec==3:
        fonksiyonlar.kitap_oku()
    #delete book    
    elif islem_sec==4:
        fonksiyonlar.kitap_sil()
        break
    else:
        #quit the program
        cikis_islemi=input("Tanımsız İşlem, İşleme devam etmek için E/H işlemi sonlandırmak için Q ya basınız:  ")
        if cikis_islemi=="e" or cikis_islemi=="E":
            continue
        elif cikis_islemi=="h" or cikis_islemi=="H":
            print("***İŞLEM SONLANDIRILDI***")
            break
        elif cikis_islemi=="Q" or cikis_islemi=="q":
            print("***PROGRAMDAN ÇIKILIYOR***")
            break
        else:
            continue

