from databaseHandler import *
from  stockInfo import *

while True:
    option = input(' 1. Search stock info \n 2. Buy stocks \n 3. Check average stock profits \n 4. Portfolio profit calc(every Stock) \n')
    match option:
        case'1':
            stock = input('Enter stock: ')
            stockInfo = stockPrice(stock)
            print( stockInfo[1] +' current price: ' + str(stockInfo[0]) + f'({stockInfo[2]})')
            print('\n')

        case'2':
            stock = input('Enter stock to be purchased: ')
            stockBuyer(stock)
            print('\n')

        case'3':
            stock = input('Enter stock: ')
            stockProfitCalc(stock)
            print('\n')
        case '4':
            portfolioProftCalc()
