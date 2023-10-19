"""Dosya yolu belirt"""
import time
import os

#create new book
def yeni_kitap_olustur():
    #take the book name and convert to txt file with ".txt"
    kitap_olustur=input("Kitap Adını Giriniz: ".upper())+".txt"#oluşturmak istenilen dosya adı alınır +".txt" ile metin belgesine çevrilir.
    print("Dosya Oluşturuluyor...")
    #new file created by module "x" and define turkish chars with encoding. 
    dosya= open(kitap_olustur,"x",encoding="utf-8") #"x" modülü ile yeni dosya oluşturulur, encoding ile türkçe karakter tanımlanır ve bunlar DOSYA denilen bir değişkene atanır.
    time.sleep(0.5)
    print("\t****Dosya Oluşturuldu****")
    #After creating file add to note with module "w"
    dosya=open(kitap_olustur,"w",encoding="utf-8")#Bu kısımda oluşturulan dosyaya (metin belgesine) "w" modülü ile notlar eklenir.
    #take to note about book
    icerik=input("Kitap Hakkındaki Notlarınızı Giriniz: ")
    print("İçerik Ekleniyor...")
    #content is insert to file
    dosya.write(icerik)#Dosyaya içerik eklenir.
    time.sleep(0.5)
    print("\t****İçerik Eklendi****")
    #file is closing
    dosya.close() #Dosya kapatılır.

#add context
def icerik_ekle(): #Daha önce açılan dosyaya yeni notlar ekleme fonksiyonu
    #call the book
    kitaba_eris=input("Erişmek İstediğiniz Kitap Adını Giriniz: ".upper())+".txt"#Halihazırda olan dosya adı alınır
    print("{} adlı Kitap Sorgulanıyor...".format(kitaba_eris))
    #book is found?
    if os.path.isfile(kitaba_eris):#Girilen dosya adı ile daha önce dosya açılmış mı kontrolünü yapar
        time.sleep(0.5)
        print("\t****{} adlı kitap bulundu.****".format(kitaba_eris))
        #if book is founded, go to file and add the note with method "a"
        dosya_eris=open(kitaba_eris,"a",encoding="utf-8")#Eğer daha önce aynı ad ile dosya oluşturulduysa bu bloğa girer ve "a" metoduyla metnin sonuna not ekler
        #take the notes
        not_ekle=input("Kitap Hakkındaki Eklemek İstediğiniz Notları Girin: ")
        print("{} adlı kitaba girilen içerik ekleniyor...".format(kitaba_eris))
        #add the note
        dosya_eris.write(not_ekle)
        time.sleep(0.5)
        print("\t****İçerik Eklendi****")
        #file is closing
        dosya_eris.close()#Dosya kapatılır
    else:
        print("{} adlı kitap bulunamadı".format(kitaba_eris))
        while True:
            #do u want to create new file
            islem=input("\t Yeni bir dosya Oluşturmak İster Misiniz (E/H): ")#Eğer girilen dosya adıyla bir dosya bulunmadıysa Yeni bir dosya açmak için izin ister.
            print("Sadece E ya da H karakterlerinden birini giriniz: ")
            #e or E meaning is yes
            if (islem=="E") or (islem=="e"):#E ye basılırsa 
                    print("\t\t{} Adlı Yeni Kitap Oluşturuluyor...".format(kitaba_eris))
                    time.sleep(0.5)
                    #call the function for creating book
                    yeni_kitap_olustur()#bu fonksiyon çalıştırılır
                    print("\t\t\t*** {} Adlı Yeni Kitap Oluşturuldu***".format(kitaba_eris))
                    break
            # h or H meaning is no
            elif(islem=="H") or (islem=="h"):
                    print("Dosya oluşturma işlemi İptal Ediliyor...")
                    time.sleep(0.5)
                    print("***Dosya oluşturma işlemi iptal edildi.***")
                    break
            else:
                print("Lütfen sadece E ya da H karakterlerinden birini giriniz, çıkmak için 'Q' ya basın: ")
                continue
     
           
         

#see the file and read them                
def kitap_oku():#Daha önce var olan dosyaya erişip içeriği okumamızı sağlar
    while True:
            #take the book name for calling
            kitaba_eris=input("Erişmek İstediğiniz Kitap Adını Giriniz: ".upper())+".txt"
            if os.path.isfile(kitaba_eris):
               print("\t{} adlı dosya çağrılıyor...".format(kitaba_eris))
               #read the file with module "r"
               dosya_eris=open(kitaba_eris,"r",encoding="utf-8")#Erişilen dosyayı "r" modülü ile okur
               icerik=dosya_eris.read()
               time.sleep(0.5)
               print(icerik)
               dosya_eris.close()
               break
            else:
               #if book is not found create or pass
               print("{} adlı kitap bulunamadı".format(kitaba_eris))
               while True:
                    islem=input("\t{} adlı yeni bir dosya Oluşturmak İster Misiniz (E/H): ".format(kitaba_eris))#Eğer girilen dosya adıyla bir dosya bulunmadıysa Yeni bir dosya açmak için izin ister.

                    if (islem=="E") or (islem=="e"):#E ye basılırsa 
                     print("\t\t{} Adlı Yeni Kitap Oluşturuluyor...".format(kitaba_eris))
                     time.sleep(0.5)
                     yeni_kitap_olustur()#bu fonksiyon çalıştırılır
                     print("***\t\t\t {} Adlı Yeni Kitap Oluşturuldu***".format(kitaba_eris))
                     break
                    elif(islem=="H") or (islem=="h"):
                      print("Dosya oluşturma işlemi İptal Ediliyor...")
                      time.sleep(0.5)
                      print("***Dosya oluşturma işlemi iptal edildi.***")
                      break
                    else:
                        print("Sadece E ya da H karakterlerinden birini giriniz: ")
                        continue
            break


#delete book
def kitap_sil():
    while True:
        kitap_adi=input("Silmek İstediğiniz Kitabın Adını Giriniz: ".upper())+".txt"
        if os.path.isfile(kitap_adi):
            print("{} adlı kitap siliniyor....".format(kitap_adi))
            os.remove(kitap_adi) #Girilen dosya adının sadece içeriğini temizler
            time.sleep(0.5)
            print("\t****{} adlı kitap silindi****".format(kitap_adi))
            continue
        else:
            print("{} adlı kitap bulunamadı...".format(kitap_adi))
            break
  






