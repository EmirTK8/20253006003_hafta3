# İleri Python Programlama - Hafta 3 Lab Ödevi

**Öğrenci:** Emir Talha Karaman  
**Öğrenci Numarası:** 20253006003  
**Ders:** İleri Python Programlama  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**Dönem:** 2026–2027 Güz  
**GitHub Deposu:** https://github.com/EmirTK8/20253006003_hafta3  

---

### Proje Özeti ve Yapılan Çalışmalar

Bu lab çalışmasında, uzay macerası oyununun monolitik seyahat mekanizması (`travel`) küçük ve bağımsız test edilebilir fonksiyonlara bölünmüş, harita yapısı ise harici bir veri dosyasına taşınmıştır.

Ödev boyunca uygulanan temel başlıklar:
* **Saf Fonksiyonlar (Pure Functions):** `envanter_metni` ve `hedef_menusu` fonksiyonları ekrana çıktı basmadan metin üretecek şekilde kurgulanmış ve test odaklı (TDD) geliştirilmiştir.
* **Esnek ve Anahtar Kelime Parametreleri:** `gorev_kaydi` fonksiyonu ile `*args`, `**kwargs` açma işlemleri ve pozisyonel verilemeyen (keyword-only) `oncelik` parametresi kullanılmıştır.
* **Veri Odaklı Mimari:** Oyun evreni `galaksi.json` dosyasına aktarılmış; `galaksi_kur` fonksiyonu ile rota bağlantıları ve varsayılan yakıt değerleri yönetilmiştir.
* **Kapsam (Scope) Analizi ve Tuzaklar:** Varsayılan parametrelerdeki değiştirilebilir liste tuzağı `None` kalıbıyla giderilmiş; LEGB hiyerarşisi ve `UnboundLocalError` davranışları `kapsam.md` belgesinde incelenmiştir.
* **İleri Fonksiyon Teknikleri:** `nonlocal` ile durum tutan `hamle_sayaci` closure'ı, çok kriterli lambda sıralaması (`en_bagli_gezegenler`) ve yürütme süresini hesaplayan `@sure_olc` dekoratörü kodlanmıştır.

Tüm görevlerde `global` kullanımı yerine parametre aktarımı ve closure yapıları tercih edilmiş, tüm birim testlerin (`pytest`) eksiksiz geçmesi sağlanmıştır.
