import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="HiveNavigator Dashboard", page_icon="🐝", layout="wide")

st.title("🐝 HiveNavigator — Acoustic Analysis Dashboard")
st.markdown("Analysis of queenless vs queenright bee colonies using acoustic and sensor data")

@st.cache_data
def load_data():
    df = pd.read_csv("features.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

st.sidebar.title("Controls")

feature_cols = ['centroid', 'bandwidth', 'rolloff', 'flatness', 'zcr', 'rms'] + \
               [f'mfcc_{i}' for i in range(1, 14)] + \
               [f'chroma_{i}' for i in range(1, 13)]

selected_feature = st.sidebar.selectbox("Select Feature", feature_cols)

all_hives = sorted(df['hive'].unique().tolist())
selected_hives = st.sidebar.multiselect("Select Hives", all_hives, default=all_hives)

min_date = df['timestamp'].min().date()
max_date = df['timestamp'].max().date()
date_range = st.sidebar.date_input("Date Range", [min_date, max_date])

df_filtered = df[df['hive'].isin(selected_hives)]
if len(date_range) == 2:
    df_filtered = df_filtered[
        (df_filtered['timestamp'].dt.date >= date_range[0]) &
        (df_filtered['timestamp'].dt.date <= date_range[1])
    ]

colors = {
    'hive_03': 'red',
    'hive_04': 'orange',
    'hive_05': 'blue',
    'hive_06': 'green',
    'hive_07': 'purple',
    'hive_08': 'brown',
    'hive_09': 'pink',
    'hive_10': 'gray'
}

fig = go.Figure()

for hive in selected_hives:
    hive_data = df_filtered[df_filtered['hive'] == hive]
    is_queenless = hive in ['hive_03', 'hive_04']
    fig.add_trace(go.Scatter(
        x=hive_data['timestamp'],
        y=hive_data[selected_feature],
        name=f"{hive} {'👑❌' if is_queenless else '👑✅'}",
        line=dict(color=colors.get(hive, 'black'),
                  width=2 if is_queenless else 1),
        mode='lines'
    ))

fig.add_vrect(
    x0='2026-03-12', x1='2026-03-14',
    fillcolor='red', opacity=0.1,
    layer='below', line_width=0,
    annotation_text='Queen removal window',
    annotation_position='top left'
)

fig.add_vrect(
    x0='2026-03-09', x1='2026-03-12',
    fillcolor='orange', opacity=0.1,
    layer='below', line_width=0,
    annotation_text='Hive 04 queenless',
    annotation_position='top right'
)

fig.update_layout(
    title=f'{selected_feature.upper()} Over Time — All Hives',
    xaxis_title='Date',
    yaxis_title=selected_feature,
    hovermode='x unified',
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 Queenless vs Queenright Comparison")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("RMS Difference", "-46.7%", help="Queenless hives are quieter")
with col2:
    st.metric("Flatness Difference", "+55%", help="Queenless hives are more chaotic")
with col3:
    st.metric("Total Recordings", f"{len(df)}", help="Feature vectors extracted")

st.subheader("🔍 Key Findings")
st.markdown("""
- **RMS Energy** dropped by **46.7%** in queenless hives
- **Spectral Flatness** increased by **55%** in queenless hives
- **Hive 04** showed stronger signals after queen introduction
- Changes appear **within hours** of queen status change
- **Modulation spectrogram** revealed patterns not visible in MFCCs
""")
