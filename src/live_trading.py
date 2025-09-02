import argparse, asyncio
from binance import AsyncClient, BinanceSocketManager
from src.renko import Renko

async def main(symbol, brick_size):
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.kline_socket(symbol=symbol, interval='1m')
    renko = Renko(brick_size)
    prices = []

    async with ts as stream:
        async for msg in stream:
            c = float(msg['k']['c'])
            prices.append(c)
            if len(prices) > 200:
                import pandas as pd
                df = pd.DataFrame({'close': prices[-200:]})
                r_df = renko.build(df)
                if len(r_df) > 2 and r_df.iloc[-1]['dir'] != r_df.iloc[-2]['dir']:
                    sig = "BUY" if r_df.iloc[-1]['dir']==1 else "SELL"
                    print(f"Signal: {sig} at {r_df.iloc[-1]['close']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="BTCUSDT")
    parser.add_argument("--brick-size", type=int, default=50)
    args = parser.parse_args()
    asyncio.run(main(args.symbol, args.brick_size))
