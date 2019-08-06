student={"Name":"Ananth", "Age":42}
aa=student.get("Name")
print(aa)


"""students=[
    {"Name":"Ananth", "Age":42}
]
print(students("name"))"""


student["Name"]="Muruganantham"
aa=student.keys();
print("\n\nPrinting Keys")
for ke in aa:
    print(f"{ke}")
print("\n\nPrinting Values")
val=student.values();
for va in val:
    print(f"{va}")
# del student["Name"] -- to delete the item from the dictionary
students_all = [
        {"Name":"Muruganantham", "Age":40},
        {"Name":"Ananth", "Age":41},
        {"Name":"Karthi","Age":39}
    ]

print("\n\nPrinting Dictionary")
for eachstu in students_all:
    for stu in eachstu:
        print("{0} : {1} ".format(stu, eachstu.get(stu)))
   #



