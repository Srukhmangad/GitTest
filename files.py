#f=open("product.CSv","r")
#f.readline()
#for i in f:
#    str=i.split(',')
#    print("Price of "+ str[1] + " is "+str[2])

f1=open("Book1.csv","a")
f1.write("\n")
f1.write("Extra")
f1.close()


f1=open("Book1.csv","r") 
print(f1.read())
   
