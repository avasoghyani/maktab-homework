#vorude ettelaaat marbut be melk va malek
import re
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
        return f"first name is :{self.first_name}\n last name is :{self.last_name}\n email address is: {self.email}\n code meli is :{self.email}\n phone number is:{self.phone_num}"
    def __repr__(self):
        return f"first name is :{self.first_name}\n last name is :{self.last_name}\n email address is: {self.email}\n code meli is :{self.email}\n phone number is:{self.phone_num}"
class Apartment:
    def __init__(self,owner,renter,room_num,area,floor,floor_num,address,phone,active_or_deactive,
        mortgage_amount,rent_amount,sale_price,rent_or_sale,parking):
        self.owner=owner
        self.renter=renter
        self.room_num=room_num
        self.area=area
        self.floor=floor
        self.floor_num=floor_num
        self.address=address
        self.phone=phone
        self.active_or_deactive=active_or_deactive
        self.mortgage_amount=mortgage_amount
        self.rent_amount=rent_amount
        self.sale_price=sale_price
        self.rent_or_sale=rent_or_sale
        self.parking=parking


    def show_apartment_detail(self):
        return f""" owner is: {self.owner},
                    renter is: {self.renter}
                    number of the apartment room is: {self.room_num}
                    apartment area is: {self.area}
                    the apartment is in floor: {self.floor}
                    number of the apartment floor is: {self.floor_num}
                    address of the apartment is: {self.address}
                    the apartment phone number is: {self.phone}
                    the apartment is : {self.active_or_deactive}
                    the apatment mortgage amount is: {self.mortgage_amount}
                    the aparment rent amount is: {self.rent_amount}
                    the apartment sales price is: {self.sale_price}
                    the apartment is for:{self.rent_or_sale}
                    the apartment has parking or no: {self.parking} """

    def edit_apartment_detail(self,num,new_value):
       if num=='1':
            self.owner=new_value
       elif num=='2': 
            self.renter=new_value 
       elif num=='3': 
            self.room_num=new_value
       elif num=='4':
            self.area=new_value   
       elif num=='5':
            self.floor=new_value  
       elif num=='6':
            self.floor_num=new_value
       elif num=='7':
            self.address=new_value                
       elif num=='8':
            self.phone=new_value
       elif num=='9':
            self.active_or_deactive=new_value
       elif num=='10':
            self.pmortgage_amount=new_value
       elif num=='11':
            self.rent_amount=new_value
       elif num=='12':
            self.sale_price=new_value
       elif num=='13':
            self.rent_or_sale=new_value
       elif num=='14':
            self.parking=new_value
    def __repr__(self):
                return f"""
                    owner is: {self.owner}
                    renter is: {self.renter}
                    number of the apartment room is: {self.room_num}
                    apartment area is: {self.area}
                    the apartment is in floor: {self.floor}
                    number of the apartment floor is: {self.floor_num}
                    address of the apartment is: {self.address}
                    the apartment phone number is: {self.phone}
                    the apartment is : {self.active_or_deactive}
                    the apatment mortgage amount is: {self.mortgage_amount}
                    the aparment rent amount is: {self.rent_amount}
                    the apartment sales price is: {self.sale_price}
                    the apartment is for:{self.rent_or_sale}
                    the apartment has parking or no: {self.parking} """       
class Home:
        pass
class Shop:
    pass
class RealEstate:
     @staticmethod
     def search_home_by_sale(search_value,home_list,sale_list=[],rent_list=[]):
          for i in home_list:
               if search_value=='sale':
                    sale_list.append(i)
               else:
                     rent_list.append(i)
          print(sale_list) 
          print(rent_list)         
     @staticmethod
     def search_home_by_area(search_value,area_you_want,home_list,list_by_area=[]):
          for i in home_list:
               if search_value==area_you_want:
                    list_by_area.append(i)
          print(home_list)          
             
home_list=[]
person_list=[]
address_list=[]
while True:
     print("1-Add Address and show address list \n 2-Add person\n 3-Add home\n 4-Edit person profile \n 5-Edit Address\n 6-Edit Home\n 7-Search home ")
     key=input("what opperation do ypu want to do?please enter the key number:")
     if key=="1":
          city=input("Enter the ctiy:")
          street=input("Enter the street:")
          plate_num=int(input("Enter the plate number:"))
          post_code=int(input("Enter the postal code:"))
          melk=Address(city,street,plate_num,post_code)
          address_list.append(melk)
          print(melk.show_address())      
          print(address_list)
     elif key=="2":
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
          person_list.append(person)
          print(person_list)
     elif key=="3":
          owner=person.first_name
          renter=person.first_name
          room_num=input("enter the home rooms:")
          area=input("enter the home area:")
          floor=input("enter the home floors:")
          floor_num=input("enter the home floor:")
          address=melk
          phone=input("enter the home phone:")
          active_or_deactive=input("enter the home active ordeactive:")
          mortgage_amount=input("enter the home mortgage amount:")
          rent_amount=input("enter the home rent amount:")
          sale_price=input("enter the home price:")
          rent_or_sale=input("enter the home is for sale or rent:")
          parking=input("enter the home has parkong or no:")
          home=Apartment(owner,renter,room_num,area,floor,floor_num,address,phone,active_or_deactive,mortgage_amount,rent_amount,
          sale_price,rent_or_sale,parking)
          print(home)
          home_list.append(home)


     elif key=="4":
          #print(person_list)
         # b=int(input("wich item in list do ypu want to change?enter the item andis:"))
          c=input("what do you want to change:\n 1-name \n2-lastname\n 3-emali address\n 4-code meli\n 5-phone number\n") 
          s=input("enter the new value:")
          person.edit_person_file(c,s)
          print(person)
          print("change has done")        
     elif key=="5":
          z=input("what do you want to change:\n 1-city \n2-street\n 3-plate number\n 4-postalcode\n") 
          p=input("enter the new value:")
          melk.edit_address(z,p)
          print(melk)
          print("change has done") 
     elif key=="7":
                     
     elif key=="8":
          break
# melk1=Address("gorgan","dokhaniat",21,2345678)
# print(melk1.show_address())
# shakhse1=Person('ava','soghyai','ava.soghyani@yahoo.com',"210254671",'09125168497')
# print(shakhse1.email)
# m=shakhse1.email
# n=shakhse1.code_meli
# Person.validation_email_address(m)
# Person.validation_code_melli(n)
# melk1.edit_address('1','tehran')
# print(melk1)
# shakhse1.edit_person_file('2','ettehadi')
# print(shakhse1)
# apartment1=Apartment('ava','reza','4','210','6','6','minagol','32534217',True,
#         5000000000,500000,9000000000,'sale',True)
# apartment1.show_apartment_detail()
# print(apartment1)
# apartment1.edit_apartment_detail("2",'marjan')        
# print(apartment1)