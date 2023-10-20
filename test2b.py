name = input("Enter students name")
lastname = input("Enter students lastname")
examscore1 = float(input("Enter examscore1:"))
examscore2 = float(input("Enter examscore2:"))
examscore3 = float(input("Enter examscore3:"))
mean =(examscore1 + examscore2 + examscore3)/3
if mean>=17:
    print("great")
if mean>=12 and mean<17:
    print("Normal")
if mean<12:
    print("Fail")