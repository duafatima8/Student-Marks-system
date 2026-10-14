student_data=[]

while True:
  name = input("Enter your name: ")
  sub1 = input("Enter your first subject: ")
  sub1_marks = int(input(f"Enter how much did you got in {sub1}"))
  sub2 = input("Enter your second subject: ")
  sub2_marks = int(input(f"Enter how much did you got in {sub2}"))
  sub3 = input("Enter your third subject: ")
  sub3_marks = int(input(f"Enter how much did you got in {sub3}"))
  sub4 = input("Enter your last subject: ")
  sub4_marks = int(input(f"Enter how much did you got in {sub4}"))
  
  
  def obtained():
    return sub1_marks+sub2_marks+sub3_marks+sub4_marks

  total_obtained:int=obtained()

  def per():
    return total_obtained/400*100

  percentage = per()

  if percentage >= 90:
    grade = "A+"

  elif  percentage >= 80:
    grade = "A"

  elif percentage >= 70:
    grade = "B"

  elif percentage >= 60 :
    grade = "C"

  elif percentage >= 50:
    grade ="D"

  else:
    grade = "F"


  print(f"""  {name} has got {total_obtained} marks,
  {percentage}% percentage
  and {grade} grade.""")
