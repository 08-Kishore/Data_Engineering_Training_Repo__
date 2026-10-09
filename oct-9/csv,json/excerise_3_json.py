import json

with open("projects.json") as f:
    projects = json.load(f)

print("Datatype of returned object:", type(projects))

print("\nProject Names:")
for p in projects:
    print(p["project_name"])

print("\nProjects with budget > 400000:")
for p in projects:
    if p["budget"] > 400000:
        print(p["project_name"], "-", p["budget"])

print("\nProjects using Python:")
for p in projects:
    if "Python" in p["technologies"]:
        print(p["project_name"])

total_budget = sum(p["budget"] for p in projects)
print("\nTotal Budget of all projects:", total_budget)

all_tech = [tech for p in projects for tech in p["technologies"]]
print("\nAll Technologies:", all_tech)

unique_tech = set(all_tech)
print("\nUnique Technologies:", unique_tech)

print("\nTeam Members:")
for p in projects:
    for member in p["team"]:
        print(f"Name: {member['name']}, Role: {member['role']}, Experience: {member['experience']} years")

print("\nTeam Members with >3 years experience:")
for p in projects:
    for member in p["team"]:
        if member["experience"] > 3:
            print(f"{member['name']} ({member['role']}) in {p['project_name']}")

total_members = sum(len(p["team"]) for p in projects)
print("\nTotal Team Members:", total_members)

sorted_by_budget = sorted(projects, key=lambda x: x["budget"], reverse=True)
print("\nProjects sorted by budget (High → Low):")
for p in sorted_by_budget:
    print(p["project_name"], "-", p["budget"])

sorted_by_name = sorted(projects, key=lambda x: x["project_name"])
print("\nProjects sorted by name (A → Z):")
for p in sorted_by_name:
    print(p["project_name"])

print("\nTeam Members sorted by experience within each project:")
for p in projects:
    sorted_team = sorted(p["team"], key=lambda m: m["experience"])
    print(f"\n{p['project_name']} Team:")
    for member in sorted_team:
        print(f"Name: {member['name']}, Role: {member['role']}, Experience: {member['experience']} years")
