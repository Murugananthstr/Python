student={"Name":"Ananth", "Age":42}

try:
    name=student["Name"]
    last_name=student["last_name"]
except KeyError:
    print("Opps Key Error")

print("Code executes completed here !")
