import json

with open("employees.json","r") as f:
    emplys = json.load(f)

for emp in emplys:
    if emp["salary"]>75000:
        print(emp)

for emp in emplys:
    if 'Python' in emp["skills"]:
        print(emp)

for emp in emplys:
    print(emp["name"],emp["performance"]["rating"])

for emp in emplys:
    if emp["performance"]["rating"]>4.5:
        print(emp)

srt=sorted(emplys,key=lambda x: x["performance"]["rating"],
                reverse=True)
for emp in srt:
    print(emp)

for emp in emplys:
    if emp["employee_id"]==303:
        emp["skills"].append("MongoDB")

with open("employees.json","w") as f:
    json.dump(emplys,f,indent=4)
    print("hi")
