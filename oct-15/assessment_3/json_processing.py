import json


with open("staff.json", "r") as f:
    staff = json.load(f)


print("Datatype:", type(staff))


print("\nAll Staff Names:")
for emp in staff:
    print(emp["name"])


print("\nEmployees from Operations:")
for emp in staff:
    if emp["department"] == "Operations":
        print(emp)


print("\nEmployees with salary > 75000:")
for emp in staff:
    if emp["salary"] > 75000:
        print(emp)


print("\nEmployees with Python skill:")
for emp in staff:
    if "Python" in emp["skills"]:
        print(emp)


print("\nName, Rating, Events Handled:")
for emp in staff:
    print(emp["name"], emp["performance"]["rating"], emp["performance"]["events_handled"])


print("\nPerformance rating > 4.5:")
for emp in staff:
    if emp["performance"]["rating"] > 4.5:
        print(emp)


all_skills = []
for emp in staff:
    all_skills.extend(emp["skills"])
print("\nAll Skills:", all_skills)


unique_skills = set(all_skills)
print("\nUnique Skills:", unique_skills)


sorted_by_salary = sorted(staff, key=lambda x: x["salary"], reverse=True)
print("\nSorted by Salary:")
for emp in sorted_by_salary:
    print(emp["name"], emp["salary"])


sorted_by_rating = sorted(staff, key=lambda x: x["performance"]["rating"], reverse=True)
print("\nSorted by Rating:")
for emp in sorted_by_rating:
    print(emp["name"], emp["performance"]["rating"])


for emp in staff:
    if emp['staff_id'] == 503:
        emp["skills"].append("Pandas")


with open("staff_updated.json", "w") as f:
    json.dump(staff, f, indent=4)

print("\nUpdated staff data saved to staff_updated.json")
