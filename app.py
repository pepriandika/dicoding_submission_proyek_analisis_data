import streamlit as st
import analysis as charts

# set page config
st.set_page_config(
    layout="wide",
    page_title="Pepri Andika - Analysis Report",
    page_icon=":bar_chart:"
)

# st.markdown("""
#     <h1 style="text-align: center; font-size: 36px; margin-top: -20px;">
#         Analisis Data Kualitas Udara - Dongsi Station (2013-2017)
#     </h1>
# """, unsafe_allow_html=True)

# Styling Sidebar
st.markdown(
    """
    <style>
        /* Styling sidebar */
        [data-testid="stSidebar"] {
            background-color: #2E4053;
        }
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] h4, 
        [data-testid="stSidebar"] h5, 
        [data-testid="stSidebar"] h6, 
        [data-testid="stSidebar"] p {
            color: white;
        }
        .css-1aumxhk {
            font-size: 18px !important;
            font-weight: bold;
        }t
    </style>
    """,
    unsafe_allow_html=True
)

# Buat sidebar navigasi yang lebih menarik
st.sidebar.title("Dashboard Analisis Kualitas Udara\nDongsi Station(2013-2017)")
st.sidebar.markdown("---")

# Navigasi dengan icon
page = st.sidebar.radio(
    "📊 Pilih Grafik",
    [
        "Tren Tahunan",
        "Dampak Angin",
        "Tingkat Polusi per Jam",
        "Curah Hujan vs Polusi"
    ]
)

df = charts.load_data("data/PRSA_Data_Dongsi_20130301-20170228.csv")
pivot_hourly, pivot_yearly, pivot_wind, df = charts.preprocess_data(df)

if page == "Tren Tahunan":
    st.header("Tren Polusi Tahunan")
    st.pyplot(charts.plot_yearly_trends(pivot_yearly))
    st.markdown(
        """
        **Insight**
        - PM2.5 mengalami penurunan pada 2016 tetapi melonjak signifikan pada 2017.
        - PM10 menunjukkan tren serupa dengan PM2.5, turun pada 2016 lalu meningkat tajam pada 2017.
        - SO2 mengalami penurunan drastis antara 2014 dan 2016, kemudian naik kembali pada 2017.
        - NO2 turun signifikan dari 2014 hingga 2015, lalu perlahan naik dan melonjak pada 2017.
        - CO meningkat secara bertahap dan mencapai puncaknya pada 2017.
        - O3 mengalami tren penurunan sejak 2013 dengan sedikit fluktuasi di tahun-tahun berikutnya.
        """
    )

elif page == "Dampak Angin":
    st.header("Dampak Arah Angin pada Polusi")
    st.pyplot(charts.plot_wind_impact(pivot_wind))
    st.markdown(
        """
        **Insight**
        - PM2.5 dan PM10 cenderung tinggi saat angin berasal dari timur dan utara, serta lebih rendah saat angin dari selatan dan barat daya.
        - SO2 menunjukkan variasi tinggi saat angin dari timur laut dan menurun signifikan saat angin dari barat daya.
        - NO2 memiliki pola fluktuatif dengan puncak saat angin dari timur dan timur laut, serta menurun saat angin dari selatan.
        - CO memiliki konsentrasi tertinggi saat angin dari timur dan menurun drastis saat angin dari arah barat daya.
        - O3 justru meningkat saat angin dari barat daya dan selatan, menunjukkan pola kebalikan dari polutan lainnya.
        - Arah angin memainkan peran penting dalam distribusi polutan, dengan polutan utama lebih terkonsentrasi saat angin berasal dari timur dan utara.
        """
    )

elif page == "Tingkat Polusi per Jam":
    st.header("Tingkat Polusi Rata-rata per Jam")
    st.pyplot(charts.plot_hourly_trends(pivot_hourly))
    st.markdown(
        """
        **Insight**
        - PM2.5 dan PM10 menunjukkan tren menurun dari tengah malam hingga siang, lalu meningkat kembali di malam hari.
        - SO2 mengalami fluktuasi dengan puncak sekitar pukul 10-12 siang dan titik terendah pada sore hari.
        - NO2 cenderung menurun hingga sore hari, lalu meningkat kembali setelah pukul 18.00.
        - CO memiliki pola serupa dengan PM2.5 dan PM10, dengan tingkat tertinggi di malam hari dan terendah di sore hari.
        - O3 meningkat dari pagi hingga sore hari, lalu menurun kembali pada malam hari.
        - Pola ini menunjukkan bahwa polutan cenderung tinggi pada malam hingga dini hari, sedangkan O3 lebih tinggi di siang hingga sore hari.
        """
    )

elif page == "Curah Hujan vs Polusi":
    st.header("Hubungan Curah Hujan dan Polusi")
    st.pyplot(charts.plot_rain_impact(df))
    st.markdown(
        """
        **Insight:**
        - Curah hujan berbanding terbalik dengan tingkat polusi udara, di mana semakin tinggi curah hujan, polutan cenderung menurun.
        - Partikel PM2.5 dan PM10 mengalami penurunan signifikan karena terbawa air hujan dan mengendap ke permukaan.
        - Curah hujan rendah (0-5 mm) kurang efektif dalam mengurangi polusi udara secara signifikan.
        - Gas polutan seperti CO dan NO2 juga menurun karena hujan membantu melarutkannya di udara.
        """
    )

