## DATA EXPLORATION
# Missing values
missing_col = [col for col in train.columns
               if train[col].isnull().any()]
miss_count = train.isna().sum()
miss_df = (
    pd.concat([miss_count.rename('Missing count'), miss_count.div(len(train)).rename('Missing value')], axis=1).loc[
        miss_count.ne(0)])
miss_df.style.background_gradient(cmap="coolwarm")
miss_df.to_excel("missing_data.xlsx")

# year_built
# energy_star_rating
# direction_max_wind_speed
# direction_peak_wind_speed
# max_wind_speed
# days_with_fog


# Categorical variables distribution
fig = plt.figure()
fig, ax = plt.subplots(2, 2, figsize=(16, 12), sharey=False)
state = sns.countplot(x=train['State_Factor'], label='State_factor', ax=ax[0, 0])
building_class = sns.countplot(x=train['building_class'], label='building_class', ax=ax[0, 1])
facility_type = sns.countplot(y=train['facility_type'], label='facility_type', ax=ax[1, 0])
year_factor = sns.countplot(x=train['Year_Factor'], label='year_factor', ax=ax[1, 1])
plt.suptitle('Categorical_features')
plt.show()
fig.savefig("categorical_distribution.png")

# Numeric variables distribution
for feature in numerical_features:
    sns.kdeplot(train[feature])
    plt.show()
    fig.savefig("numerical_distribution.png")

# Target variable distribution (EUI)
fig = plt.figure()
fig, ax = plt.subplots(1, 2, figsize=(20, 6), sharey=False)
sns.kdeplot(x=train['site_eui'], ax=ax[0])
sns.boxplot(x=train['site_eui'], ax=ax[1])
plt.show()
fig.savefig("target_distribution.png")

# Relation between categorical variable and target variable
fig = plt.figure()
fig, axs = plt.subplots(1, 2)
sns.catplot(x='facility_type', y='site_eui',  kind='point', data = train, aspect=3, ax=ax[0])
sns.catplot(x='State_Factor', y='site_eui', kind='point', data = train, aspect=3, ax=ax[1])
sns.catplot(x='building_class', y='site_eui', kind='point', data = train, aspect=3, ax=ax[2])
plt.show()
plt.close(1)
plt.close(2)
plt.show()


def catplot(df, color):
    for i, col in enumerate(['facility_type', 'State_Factor', 'building_class']):
        sns.catplot(x=col, y='site_eui', data=df, kind='point', aspect=3, color=color)
        plt.xticks(rotation=90)
        plt.show()
catplot(train, "green")



# Relation between numerical variable and target variable
sns.catplot(x='heating_degree_days', y='site_eui', data=train, kind='point', color="green")
plt.xticks(rotation=90)
plt.show()

def catplot(df, color):
    for i, col in enumerate(['energy_star_rating', 'year_built', 'cooling_degree_days',
                             'heating_degree_days']):
        sns.catplot(x=col, y='site_eui', data=df, kind='point', color=color)
        plt.xticks(rotation=90)
        plt.show()
catplot(train, "green")

# CHECK HIGHLY CORRELATED NUMERICAL FEATURES (temp, wind, snow, etc)
num_cols = ['floor_area', 'ELEVATION',
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
       'december_avg_temp', 'december_max_temp', 'cooling_degree_days',
       'heating_degree_days', 'precipitation_inches', 'snowfall_inches',
       'snowdepth_inches', 'avg_temp', 'days_below_30F', 'days_below_20F',
       'days_below_10F', 'days_below_0F', 'days_above_80F', 'days_above_90F',
       'days_above_100F', 'days_above_110F', 'direction_max_wind_speed',
       'direction_peak_wind_speed', 'max_wind_speed', 'days_with_fog']
feat = num_cols + ['site_eui']
corr = train[feat].corr()
corr.style.background_gradient(cmap='coolwarm')
corr.to_excel("corr_eui.xlsx")

# outliers
fig = plt.figure()
train.boxplot(column =['days_with_fog'], grid = False)
plt.show()
fig.savefig("outliers.png")
train['days_with_fog'].describe()