import pandas as pd
import math
from matplotlib import pyplot as plt

headers = ["Date", "Open", "High", "Low", "Close", "ADJ", "Volume"]


def ALFA(N):
    return 2 / (N + 1)


def EMA(list, N, current):
    const = 1 - ALFA(N)
    close_data = list[max((current - N), 0):current] # funkcja max, aby zapobiec braniu danych wcześniejszych niż badane
    denominator = [const ** i for i in range(len(close_data))]
    numerator = [a * b for a, b in zip(denominator, reversed(close_data))]
    return sum(numerator) / sum(denominator)


def MACD(data, current):
    return EMA(data, 12, current) - EMA(data, 26, current)


def SIGNAL(macd, current):
    return EMA(macd, 9, current)


def analyze_stock(macd, signal, close_prices, stocks, money):
    length = len(macd)
    for i in range(1, length):
        if macd[i - 1] > signal[i - 1] and macd[i] < signal[i]:
            # przecina od gory, sprzedajemy akcje
            stocks_to_sell = math.floor(stocks * 0.2)
            money = money + stocks_to_sell * close_prices[i]
            stocks = stocks - stocks_to_sell

        if macd[i - 1] < signal[i - 1] and macd[i] > signal[i]:
            # przecina od dołu, kupujemy
            stocks_to_buy = math.floor(money / close_prices[i])
            money = money - stocks_to_buy * close_prices[i]
            stocks = stocks + stocks_to_buy

    stocks_to_buy = math.floor(money / close_prices[-1])
    money = money - stocks_to_buy * close_prices[-1]
    stocks = stocks + stocks_to_buy
    return (stocks*close_prices[length-1] + money) / (1000*close_prices[0])


if __name__ == '__main__':
    company = "WIG20"
    ds = pd.read_csv(f"{company}.csv", names=headers)
    close_prices = ds.loc[:, 'Close'].tolist()
    dates = [d.date() for d in pd.to_datetime(ds['Date'], format="%Y-%m-%d")]
    macd = []
    signal = []

    for i in range(1, 1000):
        macd.append(MACD(close_prices, i))
    for i in range(1, 1000):
        signal.append(SIGNAL(macd, i))

    print(f'Zysk: {analyze_stock(macd, signal, close_prices, 1000, 0)}')
    plt.figure(figsize=(12, 5))
    plt.grid()
    plt.plot(dates[0:len(close_prices)], close_prices, label='Cena')
    plt.xlabel('Data')
    plt.xticks(rotation=30)
    plt.ylabel('Wartość')
    plt.title(f'Wartość akcji {company}')
    plt.savefig(f'{company}_wartosc.png',bbox_inches='tight')
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.grid()
    plt.plot(dates[0:len(macd)], macd, label='MACD')
    plt.plot(dates[0:len(signal)], signal, label='SIGNAL')
    plt.xlabel('Data')
    plt.xticks(rotation=30)
    plt.ylabel('Wartość')
    plt.title(f'Wskaźnik {company}')
    plt.legend()
    plt.savefig(f'{company}.png',bbox_inches='tight')
    plt.show()
