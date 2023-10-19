from requests_html import HTMLSession

s = HTMLSession()


def stockABB(stock):
    index = stock.find(':')
    return stock[index + 2 :]
def stockPrice(stock):
    url = f'https://www.google.com/search?q={stock}+stock&lr=lang_en&nf=1'
    headers = {
        "Accept-Language": "en-US;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    r = s.get(url, headers=headers)
    priceHTML = r.html.find('span.IsqQVc.NprOob.wT3VGc[jsname="vWLAgc"]', first=True)
    price = priceHTML.text 
    price = price.replace(',' , '.')
    
    currency = r.html.find('span.knFDje[jsname="T3Us2d"]', first=True)
    company = r.html.find('div.PZPZlf.ssJ7i.B5dxMb' , first=True)
    if(company  is  None  or currency is None  ):
        print("No stock with given name,try again ")
        return False
    else:
        stock = r.html.find('div.iAIpCb.PZPZlf', first=True).find('span', first=True)
        stock = stockABB(stock.text)
        return float(price) , company.text , stock
