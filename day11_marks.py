marks={"maths": 99, "science": 95, "english": 89, "history": 96, "geography": 95}
total=0
n=0
for i in marks.values():
    total+=i
    n+=1
print("Total marks:", total)
print("Number of subjects:", n)
print("Average marks:", total/n)