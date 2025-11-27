import sys
if len(sys.argv)==6:
  script_name=sys.argv[0]
  sub1=sys.argv[1]
  sub2=sys.argv[2]
  sub3=sys.argv[3]
  sub4=sys.argv[4]
  sub5=sys.argv[5]
else:
  script_name=sys.argv[0]
  sub1=75
  sub2=98
  sub3=25
  sub4=63
  sub5=58
avg = (sub1+sub2+sub3+sub4+sub5)/5
if avg >=85:
  grade= "A"
elif avg >= 70:
  grade= "B"
elif avg >= 65:
  grade= "C"
elif avg >=45:
  grade= "D"
else:
  grade= "fail"
print("average marks is ",avg)
print("grade is :",grade)
  
  
