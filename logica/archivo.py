import pandas as pd
import numpy as np
dataframe = pd.read_csv('CovidData.csv',delimiter=';')
dataframe['DATE_DIED'] = dataframe['DATE_DIED'].replace('9999-99-99', np.nan)
replacement_dict = {1: True, 2: False}
dataframe['INTUBED'] = dataframe['INTUBED'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['INTUBED'].isin([True, False]), 'INTUBED'] = np.nan
is_numeric = pd.to_numeric(dataframe['AGE'], errors='coerce').notnull().all()
if is_numeric:
    print("All values in the column are numbers.")
else:
    print("There are non-numeric values in the column.")
dataframe.loc[dataframe['AGE'] > 100, 'AGE'] = np.nan
has_numbers_greater_than_100 = (dataframe['AGE'] > 100).any()

if has_numbers_greater_than_100:
    print("There are numbers greater than 100 in the column.")
else:
    print("There are no numbers greater than 100 in the column.")

dataframe['PREGNANT'] = dataframe['PREGNANT'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['PREGNANT'].isin([True, False]), 'PREGNANT'] = np.nan

dataframe['DIABETES'] = dataframe['DIABETES'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['DIABETES'].isin([True, False]), 'DIABETES'] = np.nan

dataframe['COPD'] = dataframe['COPD'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['COPD'].isin([True, False]), 'COPD'] = np.nan

dataframe['ASTHMA'] = dataframe['ASTHMA'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['ASTHMA'].isin([True, False]), 'ASTHMA'] = np.nan

dataframe['INMSUPR'] = dataframe['INMSUPR'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['INMSUPR'].isin([True, False]), 'INMSUPR'] = np.nan

dataframe['HIPERTENSION'] = dataframe['HIPERTENSION'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['HIPERTENSION'].isin([True, False]), 'HIPERTENSION'] = np.nan

dataframe['OTHER_DISEASE'] = dataframe['OTHER_DISEASE'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['OTHER_DISEASE'].isin([True, False]), 'OTHER_DISEASE'] = np.nan

dataframe['CARDIOVASCULAR'] = dataframe['CARDIOVASCULAR'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['CARDIOVASCULAR'].isin([True, False]), 'CARDIOVASCULAR'] = np.nan

dataframe['OBESITY'] = dataframe['OBESITY'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['OBESITY'].isin([True, False]), 'OBESITY'] = np.nan

dataframe['RENAL_CHRONIC'] = dataframe['RENAL_CHRONIC'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['RENAL_CHRONIC'].isin([True, False]), 'RENAL_CHRONIC'] = np.nan

dataframe['TOBACCO'] = dataframe['TOBACCO'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['TOBACCO'].isin([True, False]), 'TOBACCO'] = np.nan

dataframe['ICU'] = dataframe['ICU'].replace(replacement_dict, regex=False)
dataframe.loc[~dataframe['ICU'].isin([True, False]), 'ICU'] = np.nan

columna = dataframe.loc[:10, 'ICU']
print(columna)
