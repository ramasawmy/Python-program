def format_name(name_input, surname_input, sta_input, des_input,get_price):

    print("********************")
    print("name :", name_input )
    print("surname :", surname_input)
    print("your starting station is at", sta_input )
    print("your destination is at", des_input)
    print("********************")

def get_price():
    price = (20*10*1.15)
    return price

bill = get_price()



name1 = input("enter your name:")
surname1 = input("enter your surname:")
sta1 = input("enter your starting station :")
des1 = input("enter your destination:")
pric1 = input("price is Rs:")


format_name(name1, surname1, sta1, des1, pric1)

