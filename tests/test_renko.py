from src.renko import Renko
import pandas as pd

def test_renko_build():
    df = pd.DataFrame({'close':[100,150,200,250,300]})
    renko = Renko(brick_size=50)
    r_df = renko.build(df)
    assert not r_df.empty
    assert all(col in r_df.columns for col in ['close','dir'])
