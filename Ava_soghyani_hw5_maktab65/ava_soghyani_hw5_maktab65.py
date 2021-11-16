#vorude ettelaaat marbut be melk va malek
import pandas as pd
from os import write
import re #for checking email address
import csv # for save data in exel file
from csv import DictWriter

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
class Address:
    def __init__(self,city_name,street_name,plate_num,post_code):
        self.city_name=city_name
        self.street_name=street_name
        self.plate_num=plate_num
        self.post_code=post_code
    
    def show_address(self):
        return f"the case is in: {self.city_name} ,{self.street_name},{self.plate_num},{self.post_code}"
      
    def edit_address(self,num,new_value):
       if num=='1':
           self.city_name=new_value
       elif num=='2': 
           self.street_name=new_value 
       elif num=='3': 
           self.plate_num=new_value
       elif num=='4':
           self.post_code=new_value    

    def __str__(self):
         return f" {self.city_name} ,{self.street_name},{self.plate_num},{self.post_code}"
    def __repr__(self):
         return f" {self.city_name} ,{self.street_name},{self.plate_num},{self.post_code}"

class Person:
    def __init__(self,first_name,last_name,email,code_meli,phone_num):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.code_meli=code_meli
        self.phone_num=phone_num
    @staticmethod      
    def validation_email_address (email):
        if(re.search(regex,email)):   
            return True
        else:   
            return False 
    @staticmethod     
    def validation_code_melli(codemeli):
        if len(codemeli)==10:
            return True
        else:
            return False   
           
    def edit_person_file(self,num,new_value):
       if num=='1':
            self.first_name=new_value
       elif num=='2': 
            self.last_name=new_value 
       elif num=='3': 
            self.email=new_value
       elif num=='4':
            self.code_meli=new_value   
       elif num=='4':
            self.phone_num=new_value 
                 
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email},{self.code_meli}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.email},{self.code_meli}"


class Owner(Person):
    pass

class Renter(Person):
    pass

class Melk:
    def __init__(self,index,owner,renter,area,address,phone,active_or_deactive,mortgage_amount,rent_amount,sale_price,rent_or_sale):
        self.index=index
        self.owner=owner
        self.renter=renter
        self.area=area
        self.address=address
        self.phone=phone
        self.active_or_deactive=active_or_deactive
        self.mortgage_amount=mortgage_amount
        self.rent_amount=rent_amount
        self.sale_price=sale_price
        self.rent_or_sale=rent_or_sale

    def edit_melk_detail(self,new_value):
        while True:
            print("\n1-owner\n 2-renter\n3-area\n4-address\n5-phone\n6-active ot deactive\n 7-mortgage amount\n8-rent amount\n 9-sale price\n 10-rent or sale\n11-break")
            num=input('which one do you want to edit : ')
            if num=='1':
                    self.owner=new_value
            elif num=='2': 
                    self.renter=new_value 
            elif num=='3':
                    self.area=new_value   
            elif num=='4':
                    self.address=new_value                
            elif num=='5':
                    self.phone=new_value
            elif num=='6':
                    self.active_or_deactive=new_value
            elif num=='7':
                    self.mortgage_amount=new_value
            elif num=='8':
                    self.rent_amount=new_value
            elif num=='9':
                    self.sale_price=new_value
            elif num=='10':
                    self.rent_or_sale=new_value
            elif num=='11':
                break
              
    
    def show_melk_detail(self):
        return f""" owner is: {self.owner}
                    renter is: {self.renter}
                    apartment area is: {self.area}
                    address of the apartment is: {self.address}
                    the apartment phone number is: {self.phone}
                    the apartment is : {self.active_or_deactive}
                    the apatment mortgage amount is: {self.mortgage_amount}
                    the aparment rent amount is: {self.rent_amount}
                    the apartment sales price is: {self.sale_price}
                    the apartment is for:{self.rent_or_sale} """
    def __str__(self):
             return f""" {self.owner},{self.renter},{self.area},{self.address},{self.phone},{self.active_or_deactive},{self.mortgage_amount}
             ,{self.rent_amount},{self.sale_price},{self.rent_or_sale} """                   
        
class Apartment(Melk):
    def __init__(self,index,owner,renter,room_num,area,floor,floor_num,address,phone,active_or_deactive,mortgage_amount,rent_amount,sale_price,rent_or_sale,
    parking):
        Melk.__init__(self,index,owner,renter,area,address,phone,active_or_deactive,mortgage_amount,rent_amount,sale_price,rent_or_sale)
        self.room_num=room_num
        self.floor=floor
        self.floor_num=floor_num
        self.parking=parking

    def show_apartment_detail(self):
        return f""" {self.index}{self.owner},{self.renter},{self.room_num},{self.area},{self.floor},{self.floor_num}, {self.address},{self.phone}
                    ,{self.active_or_deactive},{self.mortgage_amount},{self.rent_amount},{self.sale_price},{self.rent_or_sale},{self.parking} """              
   
class Home(Melk):
    def __init__(self,index,owner,renter,room_num,area,floor,address,phone,active_or_deactive,
        mortgage_amount,rent_amount,sale_price,rent_or_sale,garden_area):
        Melk.__init__(self,owner,renter,area,address,phone,active_or_deactive,mortgage_amount,rent_amount,sale_price,rent_or_sale)
        self.room_num=room_num
        self.floor=floor
        self.garden_area=garden_area
    def show_home_detail(self):
        return f""" {self.index}{self.owner},{self.renter},{self.room_num},{self.area},{self.floor},{self.address},{self.phone},{self.active_or_deactive}
        ,{self.mortgage_amount},{self.rent_amount},{self.sale_price},{self.rent_or_sale},{self.garden_area} """

class Store(Melk):
       def show_store_detail(self):
        return f""" {self.index}{self.owner},{self.renter},{self.area},{self.address},{self.phone},{self.active_or_deactive},{self.mortgage_amount}
                    ,{self.rent_amount},{self.sale_price},{self.rent_or_sale}"""

class RealEstate:
     @staticmethod
     def search_home_by_sale(value,file):
       
         with open(file, 'r') as data:
            for line in csv.DictReader(data):
                if line['R or S']==value:
                    list_a.append(line)
            return list_a        
          
     @staticmethod
     def search_by_area(value,file):
         with open(file, 'r') as data:
            for line in csv.DictReader(data):
                if line['area']==value:
                    list_a.append(line)
            return list_a

     @staticmethod
     def search_by_rent_amount(value,file):
         with open(file, 'r') as data:
            for line in csv.DictReader(data):
                if line['rent amount']==value:
                    print(line)

     @staticmethod
     def search_by_mortgage_amount(value,file):
         with open(file, 'r') as data:
            for line in csv.DictReader(data):
                if line['mortgage amount']==value:
                    print(line)

     @staticmethod
     def search_by_sale_price(value,file):
         with open(file, 'r') as data:
            for line in csv.DictReader(data):
                if line['sale price']==value:
                    print(line) 

     @staticmethod
     def search_by_rent_or_sale(value,file):
         with open(file, 'r') as data:
            for line in csv.DictReader(data):
                if line['R or S']==value:
                    print(line) 


class Transaction:
    def __init__(self,buyer,owner,renter,date_of_contract,date_of_expire):
        self.buyer=buyer
        self.owner=owner
        self.renter=renter
        self.date_of_contract=date_of_contract
        self.date_of_expire=date_of_expire
    @staticmethod
    def rent (a):
        if a['R or S']=='rent':
            a['A or D']='deactive'

    @staticmethod        
    def sale(a):
        if a['R or S']=='sale':
            a['A or D']='deactive'      
        
    def __str__(self):
        return f"the owner is {self.owner} and the buyer is {self.buyer} and the renter is{self.renter}"
                             

def get_data_address():
    city=input("Enter the ctiy:")
    street=input("Enter the street:")
    plate_num=int(input("Enter the plate number:"))
    post_code=int(input("Enter the postal code:"))
    address=Address(city,street,plate_num,post_code)
    return address
def get_data_person():
    name=input("Enter the name:")
    last_name=input("Enter the last name:")
    while True:
        email=input("Enter the email address:")
        m=Person.validation_email_address(email)
        if m==False:
            print("enter the valid email address") 
        else: 
             break          
    while True:    
        code_meli=input("Enter the meli code:")
        n=Person.validation_code_melli(code_meli)
        if n==False:
            print("enter the valid meli code")
        else:
            break            
    phone=input("Enter the phone number:")
    person=Person(name,last_name,email,code_meli,phone)
    return person
def get_data_apartment():
    index=int(input('enter the number of input follow the uper list'))
    owner=get_data_person()
    renter=None
    room_num=input("enter the home rooms:")
    area=input("enter the home area:")
    floor=input("enter the home floors:")
    floor_num=input("enter the home floor:")
    address=get_data_address()
    phone=input("enter the home phone:")
    active_or_deactive=input("enter the home active ordeactive:")
    mortgage_amount=input("enter the home mortgage amount:")
    rent_amount=input("enter the home rent amount:")
    sale_price=input("enter the home price:")
    rent_or_sale=input("enter the home is for sale or rent:")
    parking=input("enter the home has parkong or no:")
    aparteman=Apartment(index,owner,renter,room_num,area,floor,floor_num,address,phone,active_or_deactive,mortgage_amount,rent_amount,
          sale_price,rent_or_sale,parking)
    return aparteman

def get_data_home():
    index=int(input('enter the number of input follow the uper list'))
    owner=get_data_person()
    renter=None
    room_num=input("enter the home rooms:")
    area=input("enter the home area:")
    floor=input("enter the home floors:")
    address=get_data_address()
    phone=input("enter the home phone:")
    active_or_deactive=input("enter the home active ordeactive:")
    mortgage_amount=input("enter the home mortgage amount:")
    rent_amount=input("enter the home rent amount:")
    sale_price=input("enter the home price:")
    rent_or_sale=input("enter the home is for sale or rent:")
    garden_area=input("enter the garden area:")
    home=Home(index,owner,renter,room_num,area,floor,address,phone,active_or_deactive,mortgage_amount,rent_amount,
          sale_price,rent_or_sale,garden_area)
    return home

def get_data_store():
    index=int(input('enter the number of input follow the uper list'))
    owner=get_data_person()
    renter=None
    area=input("enter the home area:")
    address=get_data_address()
    phone=input("enter the home phone:")
    active_or_deactive=input("enter the home active ordeactive:")
    mortgage_amount=input("enter the home mortgage amount:")
    rent_amount=input("enter the home rent amount:")
    sale_price=input("enter the home price:")
    rent_or_sale=input("enter the home is for sale or rent:")
    store=Store(index,owner,renter,area,address,phone,active_or_deactive,mortgage_amount,rent_amount,
          sale_price,rent_or_sale)
    return store  
list_a=[]
list_apartment=[]
field_names = ['index','owner','renter','room_num','area','floor','floor_num','address','phone','active_or_deactive','mortgage_amount','rent_amount',
          'sale_price','rent_or_sale','parking']

print(list_apartment)
while True:
    print('1-Add\n2-search\n3-break')
    key=int(input('what do you want to do? : '))
    if key==1:
        print('\n1-Apartment \n2-home \n3-Store')
        key2=int(input('which case you want to add : '))
        if key2==1:
            print(list_apartment)
            apartment=get_data_apartment()
            a=vars(apartment)
            list_apartment.append(a)
            with open('apartment1.csv', 'a') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                dictwriter_object.writerow(a)
                f_object.close()
            print(list_apartment)
            print(apartment.show_apartment_detail())       
        if key2==2:
            home=get_data_home()
            print(home.show_home_detail())
        if key2==3:
           store=get_data_store()
           print(store.show_store_detail())
    if key==2:
        print("which one do you looking for ?\n search by:")
        print('\n1-area\n2-mortgage amount\n3-rent amount\n4-sale price\n5-sale or rent')
        value=int(input('enter the case number:'))
        if value==1:
            print('\n1-apartment \n2-home \n3-store')
            value1=int(input('selected number : '))
            if value1==1:
          
                search_area=input("enter the area you want to search:")
                RealEstate.search_by_area(search_area,'apartment1.csv')
                case=input('you look case for rent or sale:')
                if case=='rent':
                    # for i,item in enumerate(list_a):
                    #     if item['R or S']=='rent':
                    #         print(f"{i} {item}")

                    # mm=int(input('whick case you want to rent?'))
                    # for i in range(len(list_a)):
                    #     if i==mm:
                    #         item=list_a.pop(i)
                    # print(f"you rent this case: \n {item}")   
                    # list_a=[]

                    with open('apartment1.csv', newline='') as csvfile:

                        reader = csv.DictReader(csvfile, delimiter=',')

                        for i,row in enumerate (reader):
                            if row['R or S']=='rent' and row['area']=='120':
                                print(f"{i} {row}")
                            # nn=int(input('select one of this case:'))
                            # if i==nn:
                            #     row['A or D']= 'deactive'  
                    df = pd.read_csv("apartment1.csv")
                    #df.loc[1,['S or R','A or D']] = ['sold out','deactive']
                    df.loc[2, 'R or S'] = 'sold out'
                    df.to_csv("apartment1.csv", index=False)

                if case=='sale': 
                    if item['R or S']=='sale':
                        print(f"{i} {item}")

                    mm=int(input('whick case you want to rent?'))
                    for i in range(len(list_a)):
                        if i==mm:
                            item=list_a.pop(i)
                    print(f"you rent this case: \n {item}")   
                    list_a=[]
                         
                
                
                

              
            if value1==2:
                search_area=input("enter the area you want to search:")
                RealEstate.search_by_area(search_area,'home.csv')
            if value1==3:
                search_area=input("enter the area you want to search:")
                RealEstate.search_by_area(search_area,'store.csv')
        if value==2:
            print('\n1-apartment \n2-home \n3-store')
            value1=int(input('selected number : '))
            if value1==1:
                search_mortgage=input("enter the mortgage amount you want to search:")
                RealEstate.search_by_mortgage_amount(search_mortgage,'apartment1.csv')
            if value1==2:
                search_mortgage=input("enter the mortgage amount you want to search:")
                RealEstate.search_by_mortgage_amount(search_mortgage,'home.csv')
            if value1==3:
                search_mortgage=input("enter the mortgage amount you want to search:")
                RealEstate.search_by_mortgage_amount(search_mortgage,'store.csv')   
        if value==3:
            print('\n1-apartment \n2-home \n3-store')
            value1=int(input('selected number : '))
            if value1==1:
                search_rent=input("enter the rent amount you want to search:")
                RealEstate.search_by_rent_amount(search_rent,'apartment1.csv')
            if value1==2:
                search_rent=input("enter the rent amount you want to search:")
                RealEstate.search_by_rent_amount(search_rent,'home.csv')
            if value1==3:
                search_rent=input("enter the rent amount you want to search:")
                RealEstate.search_by_rent_amount(search_rent,'store.csv') 
        if value==4:
            print('\n1-apartment \n2-home \n3-store')
            value1=int(input('selected number : '))
            if value1==1:
                search_sale=input("enter the sale price you want to search:")
                RealEstate.search_by_sale_price(search_sale,'apartment1.csv')
            if value1==2:
                search_sale=input("enter the sale price you want to search:")
                RealEstate.search_by_sale_price(search_sale,'home.csv')
            if value1==3:
                search_sale=input("enter the sale price you want to search:")
                RealEstate.search_by_sale_price(search_sale,'store.csv')  
        if value==5:
            print('\n1-apartment \n2-home \n3-store')
            value1=int(input('selected number : '))
            if value1==1:
                search=input("you want to search for sale or rent?")
                RealEstate.search_by_rent_or_sale(search,'apartment1.csv')
            if value1==2:
                search_sale=input("you want to search for sale or rent?")
                RealEstate.search_by_rent_or_sale(search,'home.csv')
            if value1==3:
                search_sale=input("you want to search for sale or rent?")
                RealEstate.search_by_rent_or_sale(search,'store.csv')                        
    if key==3:
        break
