# Zadanie 4.1 - pracownicy z nazwiskiem na litere J (filter + lambda)

employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry",
             "JACKSON Peter", "JOHNSON Rick",
             "LEWIS Terry", "CLARKE Robin"]

# filter() zostawia tylko te elementy, dla ktorych lambda zwroci True
# e[0] to pierwsza litera napisu, czyli pierwsza litera nazwiska
emp_J = list(filter(lambda e: e[0] == "J", employees))

# kazdego pracownika w osobnej linii
for e in emp_J:
    print(e)
