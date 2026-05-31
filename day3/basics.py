# data types
name ="surendra"
age=21
sports="cricket"
print(name)     
print(age)
print(sports)

#list
sports=["cricket","football","basketball"]
print(sports)
sports.append("tennis")
print(sports)
sports.remove("football")
print(sports)
print(sports[1])

# Dictionary
person={"name":"surendra","age":21,"city":"chennai"}
print(person["name"])
person["email"]="surendrareddy49175@gmail.com"
print(person)

#conditions
age=17
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#for loop
bikes=["KTM","BMW","Royal Enfield"]
for bike in bikes:
    print(bike)

for i in range(5):
    print(i)        

#while loop

count=1
while count<=5:
    print(count)
    count+=1
