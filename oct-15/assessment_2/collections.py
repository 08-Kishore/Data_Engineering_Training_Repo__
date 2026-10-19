from statistics import mean


list_of_costs=[25000,30000,45000,12500]

print(sum(list_of_costs))
print(max(list_of_costs))
print(min(list_of_costs))
print(mean(list_of_costs))

cities=["Delhi","Mumbai","New York","Delhi","Hyderabad"]
print(set(cities))

dict1={
    "shipment_id":101,
    "shipment_weight":30,
    "costs":20000,
    "city":"Delhi"
}
dict2=[
    {
        "shipment_id":101,
        "shipment_weight":30,
        "costs":20000,
        "city":"Delhi"
    },
    {
        "shipment_id":102,
        "shipment_weight":20,
        "costs":2000,
        "city":"Hyderabad"
    }
]
filer=filter(lambda s:s["costs"], dict2)
print(list(filer))