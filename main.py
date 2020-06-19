import os
from dotenv import load_dotenv

from alpha_vantage.timeseries import TimeSeries

load_dotenv()
ts = TimeSeries(key=os.getenv('API_KEY'))

# Get json object with the intraday data and another with the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
print(meta_data)