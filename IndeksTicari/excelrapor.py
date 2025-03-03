import pandas as pd
import os

# Örnek Stok Verisi
data = {
    "Ürün": ["Kalem", "Defter", "Silgi"],
    "Miktar": [10, 5, 20],
    "Fiyat": [1.5, 2.0, 0.5]
}

# Excel dosyasının kaydedileceği konumu belirleyelim
dosya_yolu = os.path.abspath("StokRaporu.xlsx")

# DataFrame ile Excel dosyası oluştur
df = pd.DataFrame(data)
df.to_excel(dosya_yolu, index=False)

print(f"Excel raporu oluşturuldu: {dosya_yolu}")
name: Excel Raporlama

on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Depoyu Klonla
      uses: actions/checkout@v2

    - name: Python'u Kur
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'

    - name: Gerekli Kütüphaneleri Yükle
      run: pip install pandas openpyxl

    - name: Python Kodunu Çalıştır
      run: python scripts/excel_rapor.py

    - name: Çıktı Dosyasını Yükle
      uses: actions/upload-artifact@v2
      with:
        name: StokRaporu
        path: StokRaporu.xlsx
