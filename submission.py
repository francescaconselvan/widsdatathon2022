test = pd.read_csv("test.csv")
row_id = test.iloc[:,62:]

submission = xgb.predict(test_final)
submission

submission = cbr.predict(test_final)
submission

row = row_id.to_numpy().flatten()
submit = pd.DataFrame()
submit['id'] = row
submit['site_eui'] = submission
submit.head()
submit.to_csv('Submission.csv', index=False)