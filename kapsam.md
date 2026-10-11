# İleri Python Programlama - Hafta 3: Değişken Kapsamı (Scope) ve Tuzaklar Raporu

**Öğrenci Adı Soyadı:** Emir Talha Karaman  
**Öğrenci Numarası:** 20253006003  
**Ders:** İleri Python Programlama  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**Tarih:** 11.10.2026  

---

## 1. Giriş ve Python'da LEGB Kuralı

Python'da bir değişkene erişilmek istendiğinde, Python ad alanlarını (namespaces) **LEGB** sırasıyla arar:
1. **L (Local):** Fonksiyonun kendi yerel kapsamı.
2. **E (Enclosing):** İç içe geçmiş fonksiyonlarda dıştaki (kapsayan) fonksiyonun kapsamı.
3. **G (Global):** Modül düzeyinde tanımlanmış değişkenler.
4. **B (Built-in):** Python'ın yerleşik fonksiyon ve sabitleri (`len`, `range`, `print` vb.).

Aşağıda derste ele alınan 3 temel kapsam örneğinin tahminleri, gerçek çalışma sonuçları ve detaylı nedenleri yer almaktadır.

---

## 2. Dersteki Kapsam Örnekleri

### Örnek 1: Yerel (Local) ve Global Değişken Gölgeleme (Shadowing)

#### Kod:
```python
x = 10

def f():
    x = 20
    print("Fonksiyon içi x:", x)

f()
print("Fonksiyon dışı x:", x)
```

- **Tahminim:** Fonksiyon çağrıldığında 20 basar, sonrasında global x değeri değişmeyeceği için fonksiyon dışında 10 basar.
- **Gerçek Sonuç:**
  ```text
  Fonksiyon içi x: 20
  Fonksiyon dışı x: 10
  ```
- **Nedeni:**  
  Python'da fonksiyon içerisinde bir değişkene atama yapıldığında (`x = 20`), Python bu değişkeni fonksiyonun **yerel (local)** kapsamında yeni bir değişken olarak tanımlar. Bu yerel `x`, global `x`'i gölgeler (shadowing). Fonksiyon tamamlandığında yerel ad alanı bellekten temizlenir. Modül düzeyindeki global `x` değişkeni hiçbir şekilde etkilenmez ve değeri `10` kalır.

---

### Örnek 2: UnboundLocalError Tuzağı

#### Kod:
```python
sayac = 0

def arttir():
    sayac += 1
    print(sayac)

arttir()
```

- **Tahminim:** Dışarıdaki `sayac` okunmaya çalışılır ancak fonksiyon içinde atama olduğu için Python bunu yerel kabul eder ve henüz değer atanmadığından `UnboundLocalError` hatası verir.
- **Gerçek Sonuç:**
  ```text
  UnboundLocalError: cannot access local variable 'sayac' where it is not associated with a value
  ```
- **Nedeni ve Detaylı Açıklama:**  
  Bu hata Python'ın çalışma mekanizmasıyla doğrudan ilgilidir:
  1. **Derleme Aşaması (Compilation / Bytecode Generation):** Python bir fonksiyonu derlerken fonksiyon gövdesini tarar. Eğer fonksiyon içinde bir değişkene herhangi bir yerde atama yapılıyorsa (burada `sayac += 1`, yani `sayac = sayac + 1`), Python bu değişkeni baştan sona **yerel değişken (local variable)** olarak işaretler.
  2. **Çalışma Aşaması (Runtime Execution):** Fonksiyon çalıştırıldığında `sayac + 1` ifadesi değerlendirilir. Python `sayac`'ı yerel olarak işaretlediği için global kapsama bakmaz, yerel kapsamda arar. Ancak henüz bu değişkene bir değer atanmamıştır (atama sağdaki işlem bitince yapılacaktı).
  3. Değeri olmayan bir yerel değişkene erişilmeye çalışıldığı için Python `UnboundLocalError` fırlatır.
  - **Çözüm (global kullanmadan):** Fonksiyona değişkeni parametre olarak geçip yeni değeri döndürmek (`def arttir(s): return s + 1`) veya iç içe fonksiyonlarda `nonlocal` kullanmaktır.

---

### Örnek 3: Kapsayan Alan (Enclosing Scope), Closure ve `nonlocal`

#### Kod:
```python
def dis():
    mesaj = "merhaba"
    def ic():
        nonlocal mesaj
        mesaj = "dünya"
    ic()
    print("Dış fonksiyon mesajı:", mesaj)

dis()
```

- **Tahminim:** `nonlocal` kullanıldığı için iç fonksiyon dış fonksiyonun yerel değişkenini değiştirebilir ve "dünya" yazdırır.
- **Gerçek Sonuç:**
  ```text
  Dış fonksiyon mesajı: dünya
  ```
- **Nedeni:**  
  İç içe fonksiyon yapılarında içteki fonksiyon, kapsayan dış fonksiyonun değişkenlerine erişebilir (Enclosing Scope). Normalde atama yapıldığında iç fonksiyon kendi içinde yeni bir yerel değişken oluştururdu. Ancak `nonlocal mesaj` ifadesi sayesinde Python'a bu değişkenin yerel olmadığı, bir üst kapsama ait olduğu açıkça belirtilir. Böylece `ic()` fonksiyonu `dis()` fonksiyonunun kapsamındaki `mesaj` değişkenini doğrudan günceller.

---

## 3. Görev 4 (a) - Varsayılan Argüman Tuzağı (Mutable Default Argument)

### Problem:
```python
def yakit_ekle(miktar, depo=[]):
    depo.append(miktar)
    return depo
```
Python'da varsayılan argümanlar (`depo=[]`) fonksiyon her çağrıldığında DEĞİL, fonksiyon ilk tanımlandığında (derleme anında) bir kez oluşturulur. Fonksiyon her çağrıldığında aynı liste nesnesi bellekte tutulup paylaşılır. Bu nedenle ardışık çağrılar birbirini kirletir:
- `yakit_ekle(10)` -> `[10]`
- `yakit_ekle(20)` -> `[10, 20]` (Beklenen: `[20]`)

### Çözüm (None Kalıbı):
```python
def yakit_ekle(miktar: int, depo: list | None = None) -> list:
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo
```
`None` değişmez (immutable) bir nesnedir. Her çağrıda `depo is None` kontrolü yapılarak o çağrıya özel yeni bir liste `[]` açılır. Böylece çağrılar birbirini etkilemez.
