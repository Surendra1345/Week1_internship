# functions

def greet(name):
    print("Hello,"+name)
def add(a,b):
    return a+b
greet("surendra")
print(add(5,10))

#ARGS 
def calculate(*args):
    total=0
    for item in args:
        total+=item
    return total
    print(calculate(2,39))
    print(calculate(5,10,15))
#KWARGS
def show_info(**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)
    show_info(name="dhoni",age=39)
    print()
    show_info(name="dhoni",age=39,team="CSK",natioan="India")

#OOPS
class phone:
    def __init__(self, brand, model, charge):
        self.brand= brand
        self.model= model
        self.charge= charge
    def call(self):
        print(self.brand+" calling...")
    def message(self):
        print(self.brand+" messaging")
   

class smartphone(phone):
    def __init__(self, brand, model, charge, app_store):
        super().__init__(brand, model, charge)
        self.app_store=app_store
    def install_app(self,app_name):
        print("installing",app_name)
    def take_photo(self):
        print("taking photo")
phone1=phone("sumsung","glaxy",100)
phone2=phone("Google","pixel",80)
phone1.call()
phone1.message()
smartphone1=smartphone("Realme","11pro",90,"playstore")
smartphone1.call()
smartphone1.message()
smartphone1.install_app("WhatsApp")
smartphone1.take_photo()    

#JSON
import json
data={"name":"surendra","age":21,"city":"chennai"}
with open("data.json","w") as f:
    json_data=json.dumps(data)
    f.write(json_data)
with open("data.json","r") as f:
    loads_data=json.load(f)
    print(loads_data)
print("Name:",loads_data["name"])
print("Age:",loads_data["age"])
print("City:",loads_data["city"])
