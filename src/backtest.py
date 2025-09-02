import argparse
import pandas as pd
from binance.client import Client
from src.renko import Renko

def fetch_ohlcv(symbol="BTCUSDT", interval="1h", limit=500):
    client = Client()
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=['ts','o','h','l','c','v','ct','qav','ntrades','tbbav','tbqav','ignore'])
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    df = df.astype({'o':'float','h':'float','l':'float','c':'float','v':'float'})
    df = df.rename(columns={'o':'open','h':'high','l':'low','c':'close','v':'volume'})
    return df[['ts','open','high','low','close','volume']]

def run(symbol, interval, brick_size):
    df = fetch_ohlcv(symbol, interval)
    renko = Renko(brick_size)
    r_df = renko.build(df)
    signals = []
    for i in range(1,len(r_df)):
        if r_df.loc[i,'dir'] != r_df.loc[i-1,'dir']:
            sig = "BUY" if r_df.loc[i,'dir']==1 else "SELL"
            signals.append((r_df.loc[i].name, r_df.loc[i,'close'], sig))
    print("Signals:", signals[-10:])
    renko.plot(r_df, path="notebooks/sample_renko.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="BTCUSDT")
    parser.add_argument("--interval", default="1h")
    parser.add_argument("--brick-size", type=int, default=100)
    args = parser.parse_args()
    run(args.symbol, args.interval, args.brick_size)
