# 🔬 Snell Kanunu Simulatörü

> **Interaktif fizik simülasyonu ile Snell Kanunu'nu görselleştirin ve anlayın!**

Bu proje, fizik öğretimi için geliştirilmiş profesyonel bir Snell Kanunu simülatörüdür. Öğrenciler ve eğitmenler için ışığın kırılması, tam iç yansıma ve kritik açı kavramlarını görsel olarak öğrenmeyi sağlar.

---

## ✨ Özellikler

| 🎯 Özellik | 📝 Açıklama |
|------------|-------------|
| **🔍 Gerçek Zamanlı Simülasyon** | Parametre değişikliklerini anında görselleştirme |
| **⚡ Canlı Hesaplamalar** | Snell kanunu formüllerinin adım adım çözümü |
| **🎯 Tam İç Yansıma** | Kritik açı hesaplaması ve görselleştirme |
| **🎛️ İnteraktif Kontroller** | Slider'lar ve preset malzeme butonları |
| **📚 Eğitsel İçerik** | Fizik kuralları ve formül açıklamaları |
| **🎨 Modern Arayüz** | Kullanıcı dostu ve görsel olarak zengin tasarım |
| **⚙️ Kurulum Gerektirmez** | Exe dosyasını indirip çalıştırın |

---

## 🚀 Hızlı Başlangıç

### 📥 Windows Kullanıcıları (Önerilen)

**🎯 En Kolay Yol - Hazır EXE İndir:**
1. **[Releases](https://github.com/alibedirhan/CAL-snell-law/releases/latest)** sayfasına gidin
2. En son sürümden **"SnellKanuluSimulatoru.exe"** dosyasını indirin  
3. İndirilen exe dosyasını çift tıklayın - hemen çalışır! 🎉

**🔧 Alternatif - GitHub Actions:**
```bash
# 1. Actions sekmesine gidin  
# 2. "build-exe" workflow'unu çalıştırın (yeşil "Run workflow" butonu)
# 3. Tamamlandığında Artifacts bölümünden exe dosyasını indirin
```

### 🔧 Geliştiriciler ve Diğer Platformlar

#### Sistem Gereksinimleri
- Python 3.7 veya üstü
- NumPy
- Matplotlib

#### Kurulum
```bash
# Repository'yi klonlayın
git clone https://github.com/alibedirhan/CAL-snell-law.git
cd CAL-snell-law

# Sanal ortam oluşturun (önerilen)
python -m venv snell_env
source snell_env/bin/activate  # Linux/Mac
# veya
snell_env\Scripts\activate     # Windows

# Bağımlılıkları yükleyin
pip install numpy matplotlib

# Programı çalıştırın
python SnellLaw.py
```

---

## 🎮 Nasıl Kullanılır?

### 1. 🎛️ Temel Kontroller
- **Geliş Açısı Slider'ı**: Işının geliş açısını 5°-85° arasında ayarlayın
- **n₁ Slider'ı**: Üst ortamın kırılma indisini değiştirin (1.0-3.0)
- **n₂ Slider'ı**: Alt ortamın kırılma indisini değiştirin (1.0-3.0)

### 2. ⚡ Hızlı Seçim Butonları
| Buton | Malzeme Çifti | Kullanım Alanı |
|-------|---------------|----------------|
| **Hava→Su** | n₁=1.00, n₂=1.33 | Balık tutma, dalış |
| **Su→Hava** | n₁=1.33, n₂=1.00 | Tam iç yansıma örneği |
| **Cam→Hava** | n₁=1.52, n₂=1.00 | Optik lensler |
| **Sıfırla** | Varsayılan değerler | Başlangıç durumu |

### 3. 📊 Sonuçları Anlama
- **Kırmızı Ok**: Gelen ışın
- **Mavi Ok**: Kırılan ışın (normal kırılmada)
- **Yeşil Ok**: Yansıyan ışın (tam iç yansımada)
- **Hesaplama Paneli**: Adım adım matematiksel çözüm
- **Sonuç Paneli**: Kritik açı ve fizik kuralları

---

## 🔬 Fizik Prensipleri

### 📐 Snell Kanunu
```
n₁ × sin(θ₁) = n₂ × sin(θ₂)
```
**Nerede:**
- `n₁`, `n₂`: Ortamların kırılma indisleri
- `θ₁`: Geliş açısı (normale göre)
- `θ₂`: Kırılma açısı (normale göre)

### ⚡ Kritik Açı
```
θc = arcsin(n₂/n₁)    (sadece n₁ > n₂ ise)
```

### 🔄 Tam İç Yansıma Koşulları
1. **n₁ > n₂** (yoğun ortamdan seyrek ortama)
2. **θ₁ > θc** (geliş açısı kritik açıdan büyük)

---

## 📋 Malzeme Kırılma İndisleri

| 🧪 Malzeme | 📊 Kırılma İndisi (n) | 🌍 Kullanım Alanları |
|------------|----------------------|---------------------|
| **Vakum** | 1.000 | Uzay, referans değer |
| **Hava** | 1.000 | Günlük hayat |
| **Su** | 1.333 | Akvaryum, havuz |
| **Akrilik** | 1.490 | Plastik lensler |
| **Cam** | 1.520 | Pencere, lens |
| **Elmas** | 2.420 | Mücevher, kesici |
| **Silikon** | 3.420 | Yarı iletken |

---

## 🏗️ Geliştiriciler İçin

### 📦 Kendi Exe'nizi Oluşturun (Manuel)
Eğer GitHub Actions kullanmak istemiyorsanız:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "SnellKanuluSimulatoru" SnellLaw.py
```

### 🤖 Otomatik Build (GitHub Actions)
Repository'de `.github/workflows/build-exe.yml` dosyası mevcut.
- Tag push'unda otomatik çalışır
- Manuel olarak da çalıştırılabilir

### 📁 Proje Yapısı
```
snell-law-simulator/
├── 📄 SnellLaw.py          # Ana program
├── 📄 requirements.txt     # Python bağımlılıkları  
├── 📄 README.md           # Bu dosya
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 build-exe.yml # Otomatik exe oluşturma
└── 📄 .gitignore          # Git ignore kuralları
```

---

## ☕ Destek

Bu projeyi beğendiyseniz ve geliştiriciye destek olmak istiyorsanız:

**☕ [Buy Me a Coffee](https://buymeacoffee.com/alibedirhan)**

**Yapımcı:** Ali Bedirhan | **Yıl:** 2025