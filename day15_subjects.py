student1={"Math","Python","DBMS","OS"}
student2={"Python","DBMS","CN","OS"}

both = student1 & student2
diff = student1 - student2
union = student1 | student2

print("BOTH STUDENT HAVE",both)
print("ONLY STUDENT 1 HAS",diff)
print("ALL STUDENTS HAVE",union)
