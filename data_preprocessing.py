
# MISSING VALUES
train.isnull().sum()
train['year_built'] =train['year_built'].replace(np.nan, train['year_built'].median()) # anno median
train['energy_star_rating']=train['energy_star_rating'].replace(np.nan,train['energy_star_rating'].median()) #medio per: anno di costruzione, domanda energetica per metro quadro, categoria di edificio sullo star rating
train['direction_max_wind_speed']= train['direction_max_wind_speed'].replace(np.nan,train['direction_max_wind_speed'].median())
train['direction_peak_wind_speed']= train['direction_peak_wind_speed'].replace(np.nan,train['direction_peak_wind_speed'].median())
train['max_wind_speed']=train['max_wind_speed'].replace(np.nan,train['max_wind_speed'].median())
train['days_with_fog']=train['days_with_fog'].replace(np.nan,train['days_with_fog'].median())

test['year_built'] =test['year_built'].replace(np.nan, test['year_built'].median())
test['energy_star_rating']=test['energy_star_rating'].replace(np.nan,test['energy_star_rating'].median())
test['direction_max_wind_speed']= test['direction_max_wind_speed'].replace(np.nan,test['direction_max_wind_speed'].median())
test['direction_peak_wind_speed']= test['direction_peak_wind_speed'].replace(np.nan,test['direction_peak_wind_speed'].median())
test['max_wind_speed']=test['max_wind_speed'].replace(np.nan,test['max_wind_speed'].median())
test['days_with_fog']=test['days_with_fog'].replace(np.nan,test['days_with_fog'].median())

# LABEL ENCODING
ord_enc = LabelEncoder()
for category in categorical_features:
    train[category] = ord_enc.fit_transform(train[[category]])
    test[category] = ord_enc.fit_transform(test[[category]])

# DROP UNECESSARY COLUMNS
col_drop = ['floor_area', 'ELEVATION',
       'january_min_temp', 'january_avg_temp', 'january_max_temp',
       'february_min_temp', 'february_avg_temp', 'february_max_temp',
       'march_min_temp', 'march_avg_temp', 'march_max_temp', 'april_min_temp',
       'april_avg_temp', 'april_max_temp', 'may_min_temp', 'may_avg_temp',
       'may_max_temp', 'june_min_temp', 'june_avg_temp', 'june_max_temp',
       'july_min_temp', 'july_avg_temp', 'july_max_temp', 'august_min_temp',
       'august_avg_temp', 'august_max_temp', 'september_min_temp',
       'september_avg_temp', 'september_max_temp', 'october_min_temp',
       'october_avg_temp', 'october_max_temp', 'november_min_temp',
       'november_avg_temp', 'november_max_temp', 'december_min_temp',
       'december_avg_temp', 'december_max_temp', 'precipitation_inches', 'snowfall_inches',
       'snowdepth_inches', 'avg_temp', 'days_below_30F', 'days_below_20F',
       'days_below_10F', 'days_below_0F', 'days_above_80F', 'days_above_90F',
       'days_above_100F', 'days_above_110F', 'direction_max_wind_speed',
       'direction_peak_wind_speed', 'max_wind_speed', 'days_with_fog']
train_reduced = train.drop(col_drop, axis=1)
test_reduced = test.drop(col_drop, axis=1)

train_reduced.to_excel('train_reduced.xlsx')
test_reduced.to_excel('test_reduced.xlsx')

# SCALE NUMERICAL FEATURES
def scale (df, output):
    s_scaler = StandardScaler()
    target_cols = df[['site_eui', 'id']]
    numeric_cols = df.iloc[:, ~df.columns.isin(['site_eui', 'id'])]
    numeric_cols_s = s_scaler.fit_transform(numeric_cols)
    numeric_cols = pd.DataFrame(numeric_cols_s, columns=['Year_Factor',
                                                         'State_Factor',
                                                         'building_class',
                                                         'facility_type',
                                                         'year_built',
                                                         'energy_star_rating',
                                                         'cooling_degree_days',
                                                         'heating_degree_days'])
    final = pd.concat([numeric_cols, target_cols], axis=1)
    final.to_excel(output)
scale(train_reduced, output='train_final.xlsx')
scale(test_reduced, output='test_final.xlsx') # "['site_eui'] not in index"


s_scaler = StandardScaler()

#train
target_cols = train_reduced[['site_eui', 'id']]
numeric_cols = train_reduced.iloc[:, ~train_reduced.columns.isin(['site_eui', 'id'])]
numeric_cols_s = s_scaler.fit_transform(numeric_cols)
numeric_cols = pd.DataFrame(numeric_cols_s, columns = ['Year_Factor',
 'State_Factor',
 'building_class',
 'facility_type',
 'year_built',
 'energy_star_rating',
 'cooling_degree_days',
 'heating_degree_days'])
train_final = pd.concat([numeric_cols, target_cols], axis=1)
train_final.to_excel('train_final.xlsx')

#test
target_cols = test_reduced[['id']]
numeric_cols = test_reduced.iloc[:, ~test_reduced.columns.isin(['site_eui', 'id'])]
numeric_cols_s = s_scaler.fit_transform(numeric_cols)
numeric_cols = pd.DataFrame(numeric_cols_s, columns = ['Year_Factor',
 'State_Factor',
 'building_class',
 'facility_type',
 'year_built',
 'energy_star_rating',
 'cooling_degree_days',
 'heating_degree_days'])
test_final = pd.concat([numeric_cols, target_cols], axis=1)
test_final.to_excel('test_final.xlsx')
