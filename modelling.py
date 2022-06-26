import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.linear_model import LinearRegression
import catboost as cb
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error as mse
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.inspection import permutation_importance


train_final = pd.read_excel('train_final.xlsx')
test_final = pd.read_excel('test_final.xlsx')

# split train test in training and testing (proportion 4:1)
X= train_final.drop('site_eui',axis=1)
y= train_final['site_eui']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


## GRADIENT BOOST MODELS
#explanation: # https://iaml.it/blog/gradient-boosting

# 1. CATBOOTS
# explanation:
# https://towardsdatascience.com/catboost-regression-in-6-minutes-3487f3e5b329

#greed = (iterations=800, learning_rate=0.01, max_depth=10, task_type='CPU', eval_metric='RMSE', loss_function='RMSE')

def model_performance(model):
    pred = model.predict(X_test)
    rmse = np.sqrt(mse(y_test, pred))
    r2 = r2_score(y_test, pred)
    print("RMSE: ", np.mean(rmse))  # or print('RMSE: {:.2f}'.format(model_rmse))
    print('R2: ', np.mean(r2))  # or print('R2: {:.2f}'.format(model_r2))

cbr = CatBoostRegressor(iterations=800,
                          learning_rate=0.01,
                          max_depth=10,
                          task_type='CPU',
                          eval_metric='RMSE',
                          loss_function='RMSE')
cbr.fit(X_train, y_train)

cbr_performance = model_performance(cbr)


# VARIABLE IMPORTANCE
#sorted_feature_importance = model.feature_importances_.argsort()
#plt.barh(train[sorted_feature_importance],
#        model.feature_importances_[sorted_feature_importance],
#        color='turquoise')
#plt.xlabel("CatBoost Feature Importance")

# 2. XGBOOST
xgb = XGBRegressor( n_estimators = 1000 , max_depth=10, learning_rate=0.01, random_state = 0, colsample_bytree = 0.4)
xgb.fit(X_train,y_train)
xgb_performance = model_performance(xgb)







