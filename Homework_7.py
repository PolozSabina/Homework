data = '01:27:1990'

data_split = data.split(':')
data_american = data_split[1]+':'+data_split[0]+':'+data_split[2]

print('Европейский формат %s' % data_american)




