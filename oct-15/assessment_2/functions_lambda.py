dict1=[{},{}]
def shipping_cost(weight,price):
    return weight*price

def shipping_category(weight):
    if weight>20:
        return 'Heavy'
    elif 10 <= weight <= 20:
        return 'Medium'
    else:
        return 'Light'

#res=filter(lambda s:s["status"]=='Delivered',dict1])
#print(list(res))
