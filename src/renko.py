import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Renko:
    def __init__(self, brick_size=100):
        self.brick_size = brick_size

    def build(self, df: pd.DataFrame) -> pd.DataFrame:
        prices = df['close'].values
        bricks = []
        last_close = prices[0]
        direction = 0

        for p in prices:
            diff = p - last_close
            bricks_count = int(diff // self.brick_size)
            if bricks_count != 0:
                for i in range(abs(bricks_count)):
                    last_close += self.brick_size * np.sign(bricks_count)
                    direction = np.sign(bricks_count)
                    bricks.append({'close': last_close, 'dir': direction})

        renko_df = pd.DataFrame(bricks)
        return renko_df

    def plot(self, renko_df: pd.DataFrame, path=None):
        up = renko_df[renko_df['dir'] == 1]
        down = renko_df[renko_df['dir'] == -1]
        plt.figure(figsize=(10,5))
        plt.plot(up.index, up['close'], 'g', drawstyle='steps-post', linewidth=2)
        plt.plot(down.index, down['close'], 'r', drawstyle='steps-post', linewidth=2)
        plt.title(f"Renko Chart (brick={self.brick_size})")
        if path:
            plt.savefig(path)
        else:
            plt.show()
