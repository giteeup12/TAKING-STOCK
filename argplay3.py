import sys
print ('hello')
print('arg: ', str(sys.argv[0]))
print('arg: ', str(sys.argv[1]))
stock_list_file = r'C:\jim new\jimdoc\python\args\STOCKDATA.txt'
price_file = open(stock_list_file,"r")
stock_list = {}
line = price_file.readline()
while line != '':
    line_array = line.split(',')
    stock_list[line_array[0]] = line_array[5]
    print('stock symbol {0} - closing price {1}'.format(line_array[0],line_array[5]))
    line = price_file.readline()
#print('stock price of {0} is: {1} '.format(sys.argv[1]),stock_list[sys.argv[1]])
#print(stock_list["IBM"])
stock_name = str(sys.argv[1])
print('arg: ', str(stock_name))
stock_price = stock_list[str(sys.argv[1])]
print('stock price of {0} is {1}'.format(stock_name,stock_price))
