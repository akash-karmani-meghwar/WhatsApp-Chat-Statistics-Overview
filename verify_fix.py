import pandas as pd

try:
    data = ["9/13/22, 16:59 - ", "8/4/24, 21:02 - "]
    df = pd.DataFrame({'message_date': data})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')
    print("Verification Successful:")
    print(df['message_date'])
except Exception as e:
    print("Verification Failed:")
    print(e)
