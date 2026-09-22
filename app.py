"""Food Stock Dashboard — placeholder entry.

Replace this file with the full app.py from the project zip,
or upload app.py via GitHub web UI.
"""

import streamlit as st

st.set_page_config(page_title="Food Stock Report", page_icon="📦", layout="wide")
st.title("📦 Food Stock Daily Report")
st.warning(
    "File app.py belum lengkap di repo. Upload `app.py` + `dashboard_html.py` "
    "dari zip project ke GitHub, lalu redeploy."
)
st.markdown(
    """
### Langkah cepat
1. Buka repo: https://github.com/steventjarvis44-ctrl/food-stock-dashboard
2. **Add file → Upload files**
3. Upload `app.py` dan `dashboard_html.py` dari zip
4. Commit → di Streamlit Cloud klik **Reboot app**

### Atau lokal
```bash
pip install -r requirements.txt
streamlit run app.py
```
"""
)
