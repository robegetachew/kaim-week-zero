
import pandas as pd

def calculate_iqr(df, column):
    """Calculate the IQR for a specified column."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return Q1, Q3, IQR

def remove_outliers(df, column):
    """Remove outliers from a specified column using the IQR method."""
    Q1, Q3, IQR = calculate_iqr(df, column)
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Detected outliers in column '{column}':\n{outliers}")

    # Return DataFrame without outliers
    df_no_outliers = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    print(f"Data without outliers in '{column}':\n{df_no_outliers}")
    return df_no_outliers

def clean_dataframe(df, columns):
    """Clean the DataFrame by removing outliers from specified columns."""
    for column in columns:
        df = remove_outliers(df, column)
    return df