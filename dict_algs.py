ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    },
        {
        "name": "petja",
        "age": 10,
    }
    ],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    },
    {
        "name": "pavel",
        "age": 15 ,
    }
    ],
}

emps = [ivan, darja]

for el in emps:
    for el1 in el["children"]:
        if el1['age'] > 18:
            print(el["name"])
