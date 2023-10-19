import mysql.connector
from stockInfo import stockPrice
from connection import db 
cursor = db.cursor()
#cursor.execute(query)
def stockBuyer(stock):
    if not stockPrice(stock):
        print('Invalid Stock , Purchase failed')
    else:
        price,companyName,stock = stockPrice(stock)
        sql = 'INSERT INTO soldStocks(company , price , stock ) VALUES (%s , %s , %s )'
        cursor.execute(sql,(companyName,price,stock))
        print(f'Purchase of {companyName} successful')
        db.commit()
def stockProfitCalc(stock):
    query = 'SELECT DISTINCT stock FROM soldStocks'
    cursor.execute(query)
    result = cursor.fetchall()
    stockArray = [row[0] for row in result ]
    if stock not in stockArray:
        print('Stock not found or purchased')
    else:
        query = f"SELECT price FROM soldStocks WHERE stock = '{stock}' "
        cursor.execute(query)
        result = cursor.fetchall()
        priceArray = [float(row[0]) for row in result ]
        getPrice  = stockPrice(stock)
        currentPrice = getPrice[0]
        averageProfit = 0
        for price in priceArray:
            averageProfit += (currentPrice - price)/price
        averageProfit /= len(priceArray)
        print(str(averageProfit * 100) + '%' )
        return averageProfit
def portfolioProftCalc():
    query = 'SELECT DISTINCT stock FROM soldStocks'
    cursor.execute(query)
    result = cursor.fetchall()
    stockArray = [row[0] for row in result]
    for stock in stockArray:
        profit = stockProfitCalc(stock) * 100
        print(f'{stock} Profit = {profit}%')



