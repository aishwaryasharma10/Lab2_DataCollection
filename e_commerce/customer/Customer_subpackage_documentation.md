# Function Detail for the subpackage customer

**customer** is the subpackage under package e_commerce that contains the information about the customers who are buy products. A data frame called **'cust_data'** is used which contains the data about the customers including the information as below: 
- "Name" - name of customer
- "Email" - email address of customer
- "Address" - city of customers
- "Product_Name" - product purchased
- "Product_Category" - category of product
- "Price" - Price of the product 
- "Rating" - Rating of product by customer
- "Date" - Purchase date
- "Brand_Name" - Company name of the product
A list of avialable categories is created in list 'category_list'.


This subpackage customer has three modules. Description of each module is as given below:

1. **Module - personal_info.py** This is the module which displays the information of the customers. This has three functions in it and the description of each function is as follows:

    - **get_by_email(cust_data, email)**: This function provides all the information of customer whose email address is entered.        
            - input : dataframe of customers 'cust_data' and email address of customer (string).
            - output: prints all the information of customer by given email address (dataframe).        
    - **get_by_address(cust_data,city)**: This function provides all the information of customer who are from given city.        
            - input : dataframe of customers 'cust_data' and city name (string).
            - output: prints all the information of customer who are from given city (dataframe).            
    - **get_by_Product_Category(cust_data, category)**: This function provides all the information of customer who bought products of given category.             - input : dataframe of customers 'cust_data' and category name (string).
            - output: prints all the information of customer of given category (dataframe).  
            
 2. **Module - orders.py** This module shows the information of orders by customers and sales. This has four functions in it and the description of each function is as follows:

    - **total_purchase(cust_data, email)**: This function displays the total amount (in CAD) of orders of customer whose email address is entered. It searches all the orders by that customer and returns the addition of price of all the orders.
            - input : dataframe of customers 'cust_data' and email address of customer (string).
            - output: prints the total purchasing (in CAD) of customer as a single value.        
    - **sale_by_category(cust_data, category)**: This function display the total sales in CAD of the given category. It adds the price of all the products sold of that category and returns a single value.        
            - input : dataframe of customers 'cust_data' and category name (string).
            - output: prints total sales (in CAD) of that category as a single value.            
    - **sale_by_brand(cust_data, Brand_Name)**: This function display the total sales in CAD of the given brand. It adds the price of all the products sold of that brand and returns a single value.        
            - input : dataframe of customers 'cust_data' and category name (string).
            - output: prints total sales (in CAD) of that brand as a single value. 
    - **cust_by_city(cust_data)**: This function provides the number of customer from each city. It counts the number of customers in each city using their unique email id, and count is done by using group by function.                     
            - input : dataframe of customers 'cust_data'.
            - output: prints the total number of customers from each city (dataframe).  

2. **Module - analysis.py** This module displays the analysis of cust_data. This has two functions and one class (with one function) with child class (with one function) in it and their description is as follows:

    - **category_analysis(cust_data, category_list)**: This function displays the total sales of each category. The total sales of each category are calculated by using the function 'sale_by_category' defined in Module 'oredr.py'. 
            - input : dataframe of customers 'cust_data' and takes the list of categories as input (predefined).
            - output: a bar graph to show the total sales category wise.        
    - **brand_analysis(cust_data)**: This function displays the total sales of each brand. Total sales are calculated by using group by function and then matplotlib is used for graphical representation of results.
            - input : dataframe of customers 'cust_data'.
            - output: a bar graph to show the total sales brand wise.  
     - **rank_cal(cust_data)** This is class used to define class object which takes cust_data as an argument and it has two function in it:
                 - **__init__(self,cust_data)**: This function initializes the data.
                 - **avg_rating("Mark")**: This class function takes one argument brand name and calculates the rank of given brand name as average of all the ratings, and then returns the average as a single value.
                 - **rank_analysis(cust_data)** This is child class of 'rank_cal' which inherits the 'rank_cal' class. It has two function, described as follows:
                         - **__init__(self,cust_data)**: This function calls the '__init__' function of parent class 'rank_cal' for initialization.
                         - **ranking()**: This is a child class function and calculates and displays the ranking of all the brands. This function calls the parent class function 'avg_rating' to calculate the rank of brands and then display the rank of all the brands in bar graph.
                                 
