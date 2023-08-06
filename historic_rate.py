import urllib.request
import json
import datetime

def get_historical_data(start_currency, end_currency, date):
    #Make sure date is in the correct format
    if not isinstance(date, datetime.date):
        raise ValueError("Date must be in 'datetime.date' format")

    # Convert date to string format used by the API
    date = date.strftime('%Y-%m-%d')

    #put your vantage API key here. It is free and you can get it from https://www.alphavantage.co/support/#api-key
    api_key = 'C8CQO0XZ6H6GN6QR'

    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={start_currency}&to_symbol={end_currency}&apikey={api_key}'

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    if 'Time Series FX (Daily)' in data and date in data['Time Series FX (Daily)']:
        return data['Time Series FX (Daily)'][date]
    else:
        raise ValueError(f"No data available for the currency pair {start_currency}/{end_currency} on {date}.")

#Define the currencies you plan to use here
start_currency = 'EUR'
end_currency = 'USD'

#example call to the function
date = datetime.date(2023, 7, 25)
data = get_historical_data(start_currency, end_currency, date)

print(f"On {date}, the exchange rate between {start_currency} and {end_currency} was as follows:")
print(f"Open: {data['1. open']}")
print(f"High: {data['2. high']}")
print(f"Low: {data['3. low']}")
print(f"Close: {data['4. close']}")