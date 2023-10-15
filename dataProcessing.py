import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

data = pd.read_csv('nonnecessities.csv')
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
data['Month'] = data['Date'].dt.month
data['DayOfWeek'] = data['Date'].dt.dayofweek  # Monday: 0, Sunday: 6
data['IsWeekend'] = data['DayOfWeek'].isin([5, 6]).astype(int)  # Binary indicator for weekends

X = data[['Month', 'DayOfWeek', 'IsWeekend']]
y = data['Price']

model = LinearRegression()
model.fit(X, y)

last_date = data['Date'].max()

future_dates = [last_date + timedelta(days=i) for i in range(1, 61)]  # 2 months ahead (30 days/month)

future_data = pd.DataFrame({
    'Month': [date.month for date in future_dates],
    'DayOfWeek': [date.dayofweek for date in future_dates],
    'IsWeekend': [int(date.dayofweek in [5, 6]) for date in future_dates]
})

predicted_spending = model.predict(future_data)

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Price'], label='Current Spending', marker='o')
plt.plot(future_dates, predicted_spending, label='Future Predictions', marker='x')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Current Spending vs. Future Predictions (2 Months Ahead from Last Date)')
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('wantsProj.png')
print("done")

#NONNESSESITY avg monthly
data = pd.read_csv('nonnecessities.csv')
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M')
monthly_avg = data.groupby('Month')['Price'].mean()
nnMonthavg = monthly_avg
print("done")

#NESSESITY avg monthly
data = pd.read_csv('necessities.csv')
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M')
monthly_avg = data.groupby('Month')['Price'].mean()
nMonthavg = monthly_avg
print("done")