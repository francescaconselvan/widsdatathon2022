
import pandas as pd
import dataframe_image as dfi
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.inspection import permutation_importance
import catboost as cb
from catboost import CatBoostRegressor
from xgboost import XGBRegressor



train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
categorical_features = ["State_Factor", "building_class", 'facility_type', 'Year_Factor']
numerical_features = train.select_dtypes('number').columns
ordinal_cols = ['year_built', 'energy_star_rating']

list(train.columns)

# ['Year_Factor',
#  'State_Factor',
#  'building_class',
#  'facility_type',
#  'floor_area',
#  'year_built',
#  'energy_star_rating',
#  'ELEVATION',
#  'january_min_temp',
#  'january_avg_temp',
#  'january_max_temp',
#  'february_min_temp',
#  'february_avg_temp',
#  'february_max_temp',
#  'march_min_temp',
#  'march_avg_temp',
#  'march_max_temp',
#  'april_min_temp',
#  'april_avg_temp',
#  'april_max_temp',
#  'may_min_temp',
#  'may_avg_temp',
#  'may_max_temp',
#  'june_min_temp',
#  'june_avg_temp',
#  'june_max_temp',
#  'july_min_temp',
#  'july_avg_temp',
#  'july_max_temp',
#  'august_min_temp',
#  'august_avg_temp',
#  'august_max_temp',
#  'september_min_temp',
#  'september_avg_temp',
#  'september_max_temp',
#  'october_min_temp',
#  'october_avg_temp',
#  'october_max_temp',
#  'november_min_temp',
#  'november_avg_temp',
#  'november_max_temp',
#  'december_min_temp',
#  'december_avg_temp',
#  'december_max_temp',
#  'cooling_degree_days',
#  'heating_degree_days',
#  'precipitation_inches',
#  'snowfall_inches',
#  'snowdepth_inches',
#  'avg_temp',
#  'days_below_30F',
#  'days_below_20F',
#  'days_below_10F',
#  'days_below_0F',
#  'days_above_80F',
#  'days_above_90F',
#  'days_above_100F',
#  'days_above_110F',
#  'direction_max_wind_speed',
#  'direction_peak_wind_speed',
#  'max_wind_speed',
#  'days_with_fog',
#  'site_eui',
#  'id']

