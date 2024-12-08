# scripts/data_processing.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts.outliers import clean_dataframe  # Ensure this function is defined in your outliers module

# Function to process each country's dataset
def process_country_data(country_name, path):
    """Load and process the dataset for a specific country."""
    print(f'Loading data for {country_name}...')
    df = pd.read_csv(path)

    # Display initial data
    print(f'\n{country_name} data: \n')
    display(df.head())

    # Statistics
    print(f'{country_name} statistics:')
    display(df.describe())

    # Drop unnecessary columns
    df.drop(columns=['Comments'], inplace=True, errors='ignore')

    # Null and duplicates check
    print('\nNull values:')
    display(df.isnull().sum())
    print(f'\nDuplicates: {df.duplicated().sum()}')

    # Remove negative values
    df = df[(df['GHI'] >= 0) & (df['DNI'] >= 0) & (df['DHI'] >= 0)]

    # Convert Timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Clean the DataFrame by removing outliers from specified columns
    columns_to_clean = ['ModA', 'ModB', 'WS']
    df_cleaned = clean_dataframe(df, columns_to_clean)

    return df_cleaned

# Function to visualize data
def plot_time_series(df, country_name):
    """Plot time series for GHI, DNI, and DHI."""
    fig, ax = plt.subplots(figsize=(14, 6))
    df.plot(x='Timestamp', y=['GHI', 'DNI', 'DHI'], ax=ax)
    ax.set_title(f'Time Series of GHI, DNI, and DHI for {country_name}')
    ax.set_ylabel('Radiance (W/m²)')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df, country_name):
    """Plot a correlation heatmap for GHI, DNI, DHI, ModA, and ModB."""
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title(f'Correlation Heatmap for {country_name}')
    plt.show()

def plot_histograms(df, country_name):
    """Plot histograms for GHI, DNI, DHI, and WS."""
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    df['GHI'].hist(ax=axs[0, 0], bins=20)
    axs[0, 0].set_title('Histogram of GHI')
    df['DNI'].hist(ax=axs[0, 1], bins=20)
    axs[0, 1].set_title('Histogram of DNI')
    df['DHI'].hist(ax=axs[1, 0], bins=20)
    axs[1, 0].set_title('Histogram of DHI')
    df['WS'].hist(ax=axs[1, 1], bins=20)
    axs[1, 1].set_title('Histogram of Wind Speed')
    plt.tight_layout()
    plt.suptitle(f'Histograms for {country_name}', fontsize=16)
    plt.show()

def plot_scatter(df, country_name):
    """Scatter plot of GHI vs. Tamb."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='GHI', y='Tamb', data=df)
    plt.title(f'GHI vs. Temperature for {country_name}')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Temperature (°C)')
    plt.show()