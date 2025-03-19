import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders.groupby('customer_number')[['order_number']].count().reset_index()
    result = result[result['order_number'] == result['order_number'].max()][['customer_number']]
    return result