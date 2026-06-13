# იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე
# მათი სახელები + კომპანიის სახელი.

table = {
"companies": [
{
"name": "TechCorp",
"employees": [
{"name": "Ana", "salary": 3000},
{"name": "Beka", "salary": 4500}
]
},
{
"name": "SoftPlus",
"employees": [
{"name": "Nino", "salary": 5000},
{"name": "Giorgi", "salary": 2500}
]
}
]
}


for company in table["companies"]:
    for employee in company["employees"]:
        if employee["salary"] > 4000:
            print(f"{employee["name"]} - {company["name"]}")