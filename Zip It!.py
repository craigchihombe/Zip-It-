s1 = {1, 2, 3, 4}
s2 = {'a', 'b', 'c', 'd'}
s3 = list(zip(s1,s2))
print(s3)

list1 = [20, 40, 60 ,80]
list2 = [140, 180, 220, 260]
for x,y in zip(list1, list2[::-1]):
    print(x, y)

stocks = ['Reliance','infosys','tcs']
prices = [2300,2314,4564]
new_dict = {stocks:prices for stocks,prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))