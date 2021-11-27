import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def total_purchase(data, value):
    dummy = pd.DataFrame()
    dummy = data[data['Email'] == value]
    total = dummy['Price'].sum()
    new = list(data[data['Email'] == value]['Name'].head(1))
    result = pd.DataFrame({"Name": new, "Total_purchasings": total})
    return result

def sale_by_category(data, value):
    dummy = pd.DataFrame()
    dummy = data[data['Product_Category'] == value]
    total = dummy['Price'].sum()
    return total

def sale_by_brand(data, value):
    dummy = pd.DataFrame()
    dummy = data[data['Brand_Name'] == value]
    total = dummy['Price'].sum()
    return total

def cust_by_city(data):
    city_count = data.groupby('Address')['Email'].nunique()
    new_df = pd.DataFrame({'City': city_count.index, 'Number_of_Customers': city_count.values})
    return new_df