nama = [
  { 'name': 'Peter', 'age': 16 },
  { 'name': 'Mark', 'age': 18 },
  { 'name': 'John', 'age': 27 },
  { 'name': 'Jane', 'age': 14 },
  { 'name': 'Tony', 'age': 24}
]
ety_plus=[]
for i in range(len(nama)):
    a = nama[i].get("age")
    if a<=25:
        ety_plus.append(nama[i].get('name'))
#ety_plus
#nama
