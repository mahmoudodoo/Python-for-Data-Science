
import pandas as pd
import numpy as np

# Generate a sample time series data
rng = pd.date_range('2020-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)

# Resample the data to monthly frequency
monthly_ts = ts.resample('M').mean()

print(monthly_ts)
