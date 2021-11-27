#This module is basically for the graphical representation of the data 
import matplotlib.pyplot as plt

#Bar graph displaying quantity with respect to the product category
def showQuantity(seller):
    quantity=seller['Quantity']
    category=seller['Product_Category']
    
    fig = plt.figure()
    plt.bar(quantity,category)
    
    plt.title('Quantities in each category')
    plt.xlabel('Quantity')
    plt.ylabel('Category')
    plt.show()

#Bar graph displaying price with respect to the product 
def showPrice(seller):
    price=seller['Product_Price']
    p_name=seller['Product_Name']
    
    fig = plt.figure()
    plt.bar(p_name,price, color=['orange','green','red','blue'])
    
    
    plt.title('Prices of the Products')
    plt.xlabel('Products')
    plt.ylabel('Price')
    plt.show()
    
#Scatter plot displaying product category with respect to the company name
def showCategory(seller):
    category=seller['Product_Category']
    name=seller['Name']
    
    fig = plt.figure()
    plt.scatter(name,category)
    
    
    plt.title('Different company category')
    plt.xlabel('Company name')
    plt.ylabel('Category')
    plt.show()