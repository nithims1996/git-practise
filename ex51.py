print ("hotel saravana")
user=(input("what do you want?"))
biriyani=250
meals=200
if user=="biriyani":
 print ("biriyani is available")
 count=(int(input("how many do you want?")))
 bill=count*biriyani
 print(f"you have to pay {bill} for {count} biriyani")
elif user=="meals":
 print ("meals is available")
 count=(int(input("how many do you want?")))
 bill=count*meals
 print(f"you have to pay {bill} for {count}meals")
else:
 print(f"sorry ,we don't have {user} availability")
