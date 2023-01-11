import numpy as np
import pandas as pd

def get_past_and_future_data(n_days=365):
    data = {}

    for mean, variance, col in [
        (50, 3, 'temperature'),
        (3, .1, 'fuel_price'),
        (30, 3, 'cpi'),
        (8, .1, 'unemployment')
    ]:
        data[col] = np.random.normal(mean, variance, n_days).round(2)
    for col in [
        'net_cost_price_in_thousands',
        'average_user_points',
        'average_critic_points',
        'average_items_sold_in_thousands',
        'revenue_in_thousands'
    ]:
        data[col] = np.random.uniform(10, 100, n_days).round(2)

    return pd.DataFrame(data)
