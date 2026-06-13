import json

table = {
"company": {
"departments": [
{"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
{"name": "HR", "employees": [{"name": "Nino"}]}
]

}
}


for department in table["company"]["departments"]:
    for employee in department["employees"]:
        print(employee["name"])