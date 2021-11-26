#get information of seller using name
def getName(seller,name):
    return seller.loc[seller['Name'] == name]

#get information of seller using email
def getEmail(seller,email):
    return seller.loc[seller['Email'] == email]

#get information of seller using product category
def getCategory(seller,category):
    return seller.loc[seller['Product_Category'] == category]

#get information of seller using country
def getCountry(seller,country):
    return seller.loc[seller['Country'] == country]
    