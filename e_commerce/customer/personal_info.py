def get_by_email(data, value):
    return data.loc[data['Email'] == value]

def get_by_address(data, value):
    return data.loc[data['Address'] == value]
                   
def get_by_Product_Category(data, value):
    return data.loc[data['Product_Category'] == value]