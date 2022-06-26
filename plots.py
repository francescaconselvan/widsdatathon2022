plt.figure()
plt.subplot(2,2,1)
plt.plot(x='facility_type', y='site_eui',  kind='point', data = train)
plt.show()

x= train["facility_type"]
y1 = train["site_eui"]
plt.plot(x=train['facility_type'], y = y1,  'ro')
plt.show()
