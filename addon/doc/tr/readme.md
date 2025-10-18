# SMB

Sao Mai Braille yazılımı için NVDA eklentisi.  
Sürüm: 25.10  
Telif Hakkı 2022 - 2025 Sao Mai Technology Group'a aittir.

Sao Mai Braille (SMB), tarafından geliştirilen ücretsiz bir Braille metin editörü ve çeviri yazılımıdır.  
[Körler için Sao Mai](https://www.saomaicenter.org/en) 
Şu anda, doğrudan programda düzeltilemeyen bazı erişilebilirlik sorunları bulunmaktadır.  
Bu nedenle, bu küçük eklenti, NVDA ekran okuyucusunu SMB arayüzü için daha erişilebilir hale getirecektir.  
SMB programı hakkında daha fazla bilgi şu adreste bulunabilir: [https://www.saomaicenter.org/en/smsoft/smb](https://www.saomaicenter.org/en/smsoft/smb)

# Kaldırılan kısayollar:

SMB sürüm 25.5 itibariyle, aşağıdaki klavye kısayolları kaldırılmıştır:

- Alt+F9: Denklem Ekle iletişim kutusunu açar.
- Alt+F10: Resim Ekle iletişim kutusunu açar.
- Alt+F11: Müzik Partisyonu ekle iletişim kutusunu açar.

Yukarıda belirtilen kısayol tuşları yerine, aşağıdaki tuşlar kullanılacaktır:

- Ctrl+Shift+Q: Denklem ekle iletişim kutusunu açar.
- Ctrl+Shift+G: Resim ekle iletişim kutusunu açar.
- Ctrl+Shift+M: Müzik partisyonu ekle iletişim kutusunu açar.

Bu yeni kısayol tuşları, kullanıcıların hatırlamasını kolaylaştırabilir.  
Ancak, birçok kullanıcı eski klavye kısayollarına alışkın olabilir.  
Bu nedenle, bu eklenti eski komut tuşlarını entegre etti, böylece her iki kısayol stilini de paralel olarak kullanabilirsiniz.  
Bununla birlikte, yine de sağladıkları avantajlar nedeniyle yeni klavye kısayollarını kullanmanızı öneririz.  

Bu eklentinin 25.7 sürümünden itibaren, “smb” adlı bir dalı altına SMB kısayol tuşları ekledik. Böylece kullanıcılar, Sao Mai Braille penceresinde odaklandıklarında NVDA'nın Girdi Hareketleri iletişim kutusu aracılığıyla bu tuşları özelleştirebilirler.

# Eklenti Çevirisi:

Şu anda bu eklenti, eski SMB klavye kısayol giriş  yöntemleri için yardım dizelerinin yanı sıra bu Yardım dosyasını da içerir.  
[Bunları GitHub'da SMB kodu üzerinden çevirebilirsiniz.](https://github.com/manhcuong0312/SMB)  
veya platformu kullanmaya aşina değilseniz, yardım ve geri bildirim bölümündeki bilgiler aracılığıyla bizimle iletişime geçebilirsiniz.

# Yardım ve geri bildirim:

Körler için Sao Mai, Vietnam'ın Ho Chi Minh Şehrinde bulunan merkezli küçük ölçekli kar amacı gütmeyen bir kuruluştur.  
Görme engelliler için ücretsiz destek faaliyetleri yürütmek için büyük ölçüde proje hibelerine güveniyoruz.  
Bu destek faaliyetlerini sürdürmek ve yaygınlaştırmak için yardımınıza ihtiyacımız var.  
Lütfen aşağıdaki bilgilerden dilediğinizi kullanarak bizimle iletişime geçin:

Körler için Sao Mai:

- Adres: 52/22 Huynh Thien Loc, Hoa Thanh, Tan Phu, Ho Chi Minh City, Vietnam.
- E-Posta: [support@saomaicenter.org](mailto:support@saomaicenter.org)
- Bu eklentiyi çevirmek için iletişim: [tech@saomaicenter.org](mailto:tech@saomaicenter.org)
- Website: [https://saomaicenter.org/en](https://saomaicenter.org/en)

Kanallarımıza abone olun/takip edin:

- Bizden duyurular almak için şu adrese [boş bir e-posta göndererek kaydolun:](mailto:news+subscribe@saomaicenter.org)
- E-Posta listesi: [https://groups.io/g/smcb](https://groups.io/g/smcb)
- Twitter: [x.com/SaoMaiCenter](https://x.com/saomaicenter)
- Facebook: [fb.com/SaoMaiForTheBlind](https://www.facebook.com/saomaifortheblind)
- Youtube: [https://www.youtube.com/@smcenter](https://www.youtube.com/@smcenter)

# Değişiklik Günlüğü:

## 2025.10
- NVDA 2025.3 ile uyumlu.
- Türkçe readme dosyası eklendi (Umut KORKMAZ'a teşekkürler).
- Çeviriler güncellendi.

## 2025.7.2
- SMB'nin kısayol tuşları için giriş yardımı güncellendi.
- Vietnamca çeviri güncellendi. Denklem Ekle, Resim Ekle ve Müzik Partisyonu Ekle'nin adı artık SMB'nin Vietnamca arayüzüyle eşleşiyor.

## 2025.7
- SMB'nin kısayol tuşları “smb” adlı bir dal altına eklendi, böylece kullanıcılar Sao Mai Braille penceresi odaklanmışken Girdi Hareketleri iletişim kutusundan bunları özelleştirebilirler.
- NVDA 2025.2 ile uyumlu.

## 2025.5.22

* Henüz .smd veya .smb dosyası oluşturulmadan eski kısayol tuşları kullanıldığında kullanıcıya uyarı gösterilir

## 2025.5

* Mart 2025 sürümüne göre eklenti şablonu güncellendi
* Kaldırılan üç kısayol tuşunun giriş yardımının çevrilebilir olması sağlandı
* readme dosyası güncellendi

## 2025.4.2

* SMB’nin hem yeni hem de eski kısayol tuşlarının aynı anda kullanılabilmesi özelliği eklendi
* readme dosyası güncellendi

## 2025.4

* NVDA 2025.1 ile uyumlu hale getirildi
* Eklentinin kaynak kod deposu adresi değiştirildi
* readme dosyası güncellendi

## 2023.12

* NVDA 2024.1 ile uyumlu hale getirildi
* readme dosyası güncellendi

## 2023.10

* NVDA 2023.3 ile uyumlu hale getirildi
* GitHub kaynak kod deposu manhcuong0312 hesabına taşındı

## 2023.9

* NVDA 2023.2 ile uyumlu hale getirildi

## 2023.4

* Türkçe diliyle ilgili hata düzeltildi ve artık eklenti NVDA 2022.1.0 veya üzeri sürümleri gerektiriyor

## 2023.3

* Ad ve özet düzeltildi
* Çeviri güncellendi

## 2023.2

* NVDA 2023.1 ile uyumlu hale getirildi

## 2023.1

* NVDA 2022.4 ile uyumlu hale getirildi
* Umut KORKMAZ tarafından Türkçe çeviri eklendi

## 2022.8

* NVDA 2022.3 ile uyumlu hale getirildi
