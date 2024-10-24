import pandas as pd

file_path = 'C:\\Users\\Armando\\Documents\\GitHub\\Actividad-Limpieza\\bike_buyers.csv'
data = pd.read_csv(file_path)

def generate_initial_data_report(df):
    report = ""
    
    
    num_duplicates = df.duplicated().sum()
    report += f"1. Duplicados: Se encontraron {num_duplicates} filas duplicadas.\n"
    
    
    missing_values = df.isnull().sum()
    missing_values_info = missing_values[missing_values > 0]
    report += "\n2. Valores Faltantes:\n"
    if missing_values_info.empty:
        report += "   - No se encontraron valores faltantes.\n"
    else:
        for column, missing in missing_values_info.items():
            report += f"   - {column}: {missing} valores faltantes.\n"
    
    
    report += "\n3. Tipos de Datos:\n"
    for column, dtype in df.dtypes.items():
        report += f"   - {column}: {dtype}\n"
    
    return report

print("== Reporte de Inspección Inicial ==")
print(generate_initial_data_report(data))

def clean_data(df):
    df_cleaned = df.copy()

    
    df_cleaned = df_cleaned.drop_duplicates()

    categorical_columns = ['Marital Status', 'Gender', 'Home Owner']
    numerical_columns = ['Income', 'Children', 'Cars', 'Age']

    
    for column in categorical_columns:
        if column in df_cleaned.columns:
            df_cleaned.loc[:, column] = df_cleaned.loc[:, column].fillna(df_cleaned[column].mode()[0])

    
    for column in numerical_columns:
        if column in df_cleaned.columns:
            if column == 'Income':
                df_cleaned['Income'] = df_cleaned['Income'].str.replace(',', '').astype(float)
            df_cleaned.loc[:, column] = df_cleaned.loc[:, column].fillna(df_cleaned[column].median())
    
    return df_cleaned

data_cleaned = clean_data(data)

def generate_cleaned_data_report(df):
    report = ""
    
    
    num_duplicates = df.duplicated().sum()
    report += f"1. Duplicados: Se encontraron {num_duplicates} filas duplicadas después de la limpieza.\n"
    
    
    missing_values = df.isnull().sum()
    missing_values_info = missing_values[missing_values > 0]
    report += "\n2. Valores Faltantes después de la limpieza:\n"
    if missing_values_info.empty:
        report += "   - No se encontraron valores faltantes.\n"
    else:
        for column, missing in missing_values_info.items():
            report += f"   - {column}: {missing} valores faltantes.\n"
    
    return report

print("\n== Reporte después de la Limpieza ==")
print(generate_cleaned_data_report(data_cleaned))

data_cleaned.to_csv('C:\\Users\\Armando\\Documents\\GitHub\\Actividad-Limpieza\\bike_buyers_cleaned.csv', index=False)
print("\nDatos limpios guardados en: bike_buyers_cleaned.csv")
