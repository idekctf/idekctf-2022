from math import inf
import os
import sys

import numpy as np
from sklearn.metrics import mean_squared_error

np.set_printoptions(threshold=sys.maxsize, suppress=True)

n_days = 365
prev_mse = inf
n_reqs = 0
n_reqs_lim = 7000

def get_data(n_days=365):
    try:
        from secret import get_past_and_future_data

        return get_past_and_future_data(n_days)
    except ImportError:
        import pandas as pd

        # One week of data. Real-time data will cover a whole year
        return pd.DataFrame({
            'temperature': [50.74, 52.24, 48.26, 45.4 , 52.08, 51.17, 52.2],
            'fuel_price': [5.6, 5.73, 5.89, 5.23, 5.57, 5.38, 5.85],
            'cpi': [30.92, 28.99, 33.4 , 33.92, 29.53, 27.98, 28.],
            'unemployment': [6.24, 6.26, 6.33, 6.1 , 6.36, 6.35, 6.49],
            'net_cost_price_in_thousands': [13.22, 84.96, 37.67, 21.6 , 41.73,  6.82, 44.3 ],
            'average_user_points': [60.51, 81.75, 33.48, 16.83, 23.15, 76.8 , 66.96],
            'average_critic_points': [45.06, 12.44, 90.38, 43.52, 12.82, 44.89, 54.66],
            'average_items_sold_in_thousands': [45.36, 44.36, 67.79, 57.46, 85.43, 84.58,  10.53],
            'revenue_in_thousands': [41.32, 39.11, 68.07, 63.65, 46.04, 53.79, 96.7]
        })

train_data = np.array(get_data(n_days=n_days))
X_train, y_train = train_data[:, :-1], train_data[:, -1]

print('As a manager, you realize that revenue forecasting '
      'is critical to manage your business\'s growth. '
      'Fortunately, you just completed a two-hour crash course '
      'on machine learning and are now an AI guru. \n'
      'Given access to a daily revenue report from 2022, '
      'how well can you predict how things turn out in 2023?')

input('Press any key to continue... ')

print(f'Data for 2022:\n {X_train}')
print(f'Revenue (in thousands) for 2022:\n {y_train}')

test_data = np.array(get_data(n_days=n_days))
X_test, y_test = test_data[:, :-1], test_data[:, -1]

# Data quality checks: Assert that there are no outliers
assert test_data.min() >= 0 and test_data.max() <= 100

print(f'Data for 2023:\n {X_test}')

while n_reqs < 7000:
    print(f'\nYou have {n_reqs_lim - n_reqs} more attempts')
    n_reqs += 1
    preds = input('Enter your predictions for \'Revenue\' '
                  '(in thousands) for 2023:\n')
    try:
        preds = np.fromstring(preds, dtype=float, sep=' ')
        mse = mean_squared_error(preds, y_test, squared=False)

        if mse < .07:
            try:
                with open('flag.txt', 'rb') as f:
                    flag = f.read()
            except FileNotFoundError:
                flag = 'flag'
            print(f'Well done! Here\'s your flag: {flag}')

        if mse > prev_mse:
            print('Are you sure your model is working? '
                  'Maybe use a neural network for better results.')

        prev_mse = mse
    except ValueError:
        print('Oops! Something went wrong!')

