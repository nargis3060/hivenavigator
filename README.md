# 🐝 HiveNavigator — Acoustic Analysis of Beehive Data

## About
Analysis of queenless vs queenright bee colonies using acoustic and sensor data.
Built as part of the HiveNavigator DigiLink 26/27 programme.

## 🔗 Live Dashboard
[View Interactive Dashboard](https://hivenavigator-cwsdbmxapke4dstubnw8wk.streamlit.app/)

## 📊 Key Findings
- **5,373** audio feature vectors extracted from 8 hives over 10 days
- **RMS Energy** dropped 46.7% in queenless hives
- **Spectral Flatness** increased 55% in queenless hives
- Acoustic changes appear within hours of queen status change

## 🛠️ Tools Used
- Python, Librosa, Pandas, NumPy, Scipy
- Plotly, Streamlit
- AWS S3, GitHub

## 📁 Files
- `app.py` — Streamlit dashboard
- `features.csv` — Extracted audio features
- `report.md` — Analysis report
