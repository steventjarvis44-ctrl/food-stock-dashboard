# Food Stock Daily Report Dashboard

Dashboard stok food harian untuk tim Purchasing Tomoro Coffee.

## Fitur
- Upload `analisa food.xlsx`
- KPI: OOS, SOH 0 + transit, stok rendah, P1, expired
- Teks report siap copy ke chat/bot
- Grafik: risiko per hub, tren ACT, priority, transit
- Alternatif HTML tanpa server (`dashboard_html.py`)

## Jalankan lokal (Streamlit)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Buka http://localhost:8501

## Alternatif HTML (tanpa Streamlit)

```bash
pip install pandas openpyxl
python dashboard_html.py "analisa food.xlsx"
```

Membuka `dashboard_food.html` di browser.

## Deploy online (Streamlit Cloud) — gratis

1. Buka https://share.streamlit.io
2. Login dengan GitHub
3. New app → pilih repo **food-stock-dashboard**
4. Main file path: `app.py`
5. Deploy → dapat link public (bisa dibuka HP/laptop tim)

## Catatan
- Excel tidak disimpan di server (hanya di memori sesi)
- Kolom dibaca otomatis dari header Excel
