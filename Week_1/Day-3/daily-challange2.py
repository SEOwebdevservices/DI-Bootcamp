#Challenge 1: Letter Index Dictionary
#user_word = input("enter a word:")
#out_dict = {}
#for i, char in enumerate(user_word):
 #   if char in out_dict:
 #       out_dict[char].append(i)
 #   else:
#       out_dict.update({char :[i]})
#print(out_dict)        

#Challenge 2: Affordable Items
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
wallet = wallet.replace("$", "").replace(",", "")
basket = []

for item_name, price in items_purchase.items():
    price = price.replace("$", "").replace(",", "")
    price = int(price)
    
    if price <= wallet:
        basket.append(item_name)
    else:
        continue
    if basket:
        basket = sorted(basket)
        print("basket")

else:
    print("nothing")   
