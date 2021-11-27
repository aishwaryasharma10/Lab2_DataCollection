import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def total_purchase(data, value):
    dummy = pd.DataFrame()
    dummy = data[data['Email'] == value]
    total = dummy['Price'].sum()
    return total

def sale_by_category(data, value):
    category = "Electronics"
    dummy = pd.DataFrame()
    dummy = data[data['Product_Category'] == value]
    total = dummy['Price'].sum()
    return total

def category_analysis(data, c_list):
    n = len(c_list)
    total = [None]*n
    for i in range(n):
        total[i] = sale_by_category(data, c_list[i])
    fig = plt.figure()
    plt.bar(np.array(c_list), np.array(total))
    plt.title("Total sale of different categories")
    plt.xlabel("Category")
    plt.ylabel("Total sale ($)")
    plt.show()
