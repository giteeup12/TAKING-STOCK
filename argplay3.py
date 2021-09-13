import sys
print ('hello')
print('arg: ', str(sys.argv[0]))
print('arg: ', str(sys.argv[1]))
#file of stock prices
stock_list_file = r'C:\jim new\jimdoc\python\args\STOCKDATA.txt'
price_file_object = open(stock_list_file,"r")
#file of my stocks
mystock  = r'C:\jim new\jimdoc\python\args\mystock.txt'
mystock_file = open(mystock,"r")
# read list of my stocks into list of my stocks
mystock_list = []
mystock_record = mystock_file.readline()
# new comment
while mystock_record != '':
  mystock_list.append(mystock_record[0:8])
  mystock_record = mystock_file.readline()
  print('stock from my list: {0} '.format(mystock_record[0:8]))
stock_list = {}
line = price_file.readline()
while line != '':
    line_array = line.split(',')
    stock_list[line_array[0]] = line_array[5]
    #print('stock symbol {0} - closing price {1}'.format(line_array[0],line_array[5]))
    line = price_file.readline()
#print('stock price of {0} is: {1} '.format(sys.argv[1]),stock_list[sys.argv[1]])
#print(stock_list["IBM"])
stock_name = str(sys.argv[1])
print('arg: ', str(stock_name))
stock_price = stock_list[str(sys.argv[1])]
print('stock price of {0} is {1}'.format(stock_name,stock_price))
