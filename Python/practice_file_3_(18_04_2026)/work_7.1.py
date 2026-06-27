#7.1 : Student marks → calculate total & average


math = float(input("Enter your Maths marks:"))
sci = float(input("Enter your Science marks:"))
eng = float(input("Enter your English marks:"))

total = math + sci + eng

print("Total marks = ",total)

avg = ( math + sci + eng)/3

print("Your average marks is " , avg ,".")
