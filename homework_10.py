s = 'Taras Shevchenko*1814-03-09*1861-03-10'
var = s.split('*')
name = var[0]
data_1 = var[1]
data_2 = var[2]
year_1 = data_1.split('-')[0]
year_2 = data_2.split('-')[0]
age = int(year_2) - int(year_1)
print('%s прожил %d лет' % (name, age))



