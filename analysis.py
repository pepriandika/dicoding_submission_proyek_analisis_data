import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

def load_data(file_path):
    """Membaca dan membersihkan data."""
    df = pd.read_csv(file_path)
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df.insert(0, 'datetime', df.pop('datetime'))
    df.drop(columns=['year', 'month', 'day', 'hour', 'No', 'station'], inplace=True)
    df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']] = df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].interpolate(method='linear')
    df = df.assign(wd=df['wd'].fillna(df['wd'].mode()[0]))
    return df

def preprocess_data(df):
    """Membuat pivot tabel yang diperlukan."""
    pivot_hourly = df.groupby(df["datetime"].dt.hour)[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()
    pivot_hourly.index.name = "Jam"

    pivot_yearly = df.resample('YE', on='datetime')[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()
    pivot_yearly.index.name = "Year"
    pivot_yearly.index = pivot_yearly.index.strftime('%Y')

    pivot_wind = df.groupby("wd")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()

    return pivot_hourly, pivot_yearly, pivot_wind, df

def plot_yearly_trends(pivot_yearly):
    """Menampilkan tren polusi tahunan."""
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    cols = 2
    rows = math.ceil(len(pollutants) / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))
    axes = axes.flatten()

    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        ax.plot(pivot_yearly.index, pivot_yearly[pollutant], label=pollutant, marker='o')
        ax.set_xlabel('Year')
        ax.set_ylabel(f'Avg {pollutant} Level')
        ax.set_title(f'Trend of {pollutant} Over the Years')
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    # plt.show()
    return fig

def plot_wind_impact(pivot_wind):
    """Menampilkan dampak arah angin pada polusi."""
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    cols = 2
    rows = math.ceil(len(pollutants) / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))
    axes = axes.flatten()

    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        ax.plot(pivot_wind.index, pivot_wind[pollutant], label=pollutant, marker='o')
        ax.set_xlabel('Wind Direction')
        ax.set_ylabel('Avg Pollution Level')
        ax.set_title(f'Impact of Wind Direction on {pollutant}')
        ax.legend()
        ax.grid(True)
        ax.set_xticks(pivot_wind.index)
        ax.set_xticklabels(pivot_wind.index, rotation=45)

    plt.tight_layout()
    # plt.show()
    return fig

def plot_hourly_trends(pivot_hourly):
    """Menampilkan tingkat polusi rata-rata per jam."""
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    rows = (len(pollutants) + 1) // 2
    cols = 2

    fig, axes = plt.subplots(rows, cols, figsize=(12, 8))
    fig.suptitle('Tingkat Polusi Rata-rata per Jam', fontsize=14)
    axes = axes.flatten()

    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        ax.plot(pivot_hourly.index, pivot_hourly[pollutant], marker='o', linestyle='-')
        ax.set_xlabel('Jam')
        ax.set_ylabel(f'{pollutant} Level')
        ax.set_title(f'Trend {pollutant}')
        ax.set_xticks(range(24))
        ax.set_xticklabels(range(24))
        ax.grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    # plt.show()
    return fig

def plot_rain_impact(df):
    """Menampilkan hubungan curah hujan dan tingkat polusi."""
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    rows = (len(pollutants) + 1) // 2
    cols = 2

    fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))
    axes = axes.flatten()

    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        sns.scatterplot(data=df, x='RAIN', y=pollutant, ax=ax)
        ax.set_xlabel('Curah Hujan (mm)')
        ax.set_ylabel(f'Tingkat {pollutant}')
        ax.set_title(f'Hubungan Curah Hujan dan {pollutant}')
        ax.grid(True)

    plt.tight_layout()
    # plt.show()
    return fig
