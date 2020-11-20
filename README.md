# İBB Olası Deprem Kayıp Tahmini Verileri
https://depremzemin.ibb.istanbul/guncelcalismalarimiz/

İBB tarafından ilçe ilçe hazırlanan olası depem kayıp tahmini kitapçıklarının bina hasarı ve can kaybı tablolarından elde ettiğim verileri JSON formatında bir araya getirdim.

Verilere __data.json__ dosyasından ulaşabilirsiniz.

## Not
~~__TUZLA__, __ŞİLE__ ve __ÇEKMEKÖY__ ilçelerinin verilerinde hatalar vardır ve elle girilmesi gerekmektedir.~~

## Dosyalar
| Dosyalar             | İşlevleri
| -------------------- | ---------
| data.json            | Verilerin son hali
| download_booklets.py | https://depremzemin.ibb.istanbul/guncelcalismalarimiz/ web sitesinden tüm ilçelerin pdf formatındaki kitapçıklarını indirir
| extract_tables.py    | Kitapçıklardan gerekli verileri toplayıp JSON formatına getirir
| requirements.txt     | Gerekli python kütüphaneleri
| correct_data.py      | Verileri düzeltir
