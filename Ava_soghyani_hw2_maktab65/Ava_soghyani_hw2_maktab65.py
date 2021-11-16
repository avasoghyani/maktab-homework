class Ticket:
    def __init__(self):
        self.credit = 0
        self.one_trip_cost = 500
    def __repr__(self):
        return f"your credit is: {self.credit} and every trip cost:{self.one_trip_cost}"

    def show_credit(self):
        return f"your credit is:{self.credit}"

    def add_credit(self):
        added_cash = int(input('enter the credit amount you want to sharzh:'))
        self.credit = self.credit + added_cash
        return f"your ticket sharzh {self.credit} tooman"

    def check_credit(self):
        if self.credit < 0 :
            print('you dont have any credit please buy a new ticket or sharzh your card')


    def los_credit(self):
        self.credit = self.credit - self.one_trip_cost
        if self.credit>=0 :
             return f"your credit is finish"
        else:
             return f"your credit after using your card: {self.credit}"
class TicketA(Ticket):
    def __init__(self):
         super().__init__()
         self.credit = 500

class TicketB(Ticket):
 pass

class TicketC(Ticket):
    def __init__(self):
        super().__init__()
        self.time_credit = 0
        self.today_time = 27

    def show_time_credit(self):
        self.time_credit = int(input('enter your card expire time:'))
        return f"your ticket expire at {self.time_credit} "

    def check_expire_time(self):
        if self.time_credit < self.today_time:
            n =self.today_time-self.time_credit
            print(f'your ticket is expire {n} day ago')
        else:
            print('you can use your ticket')

ticket_type=input('please enter the ticket type:')
if ticket_type=='taksafare':
    ticket_1=TicketA()
    print(ticket_1)
    for i in range (2):
        ticket_1.los_credit()
        ticket_1.check_credit()
        i+=1

if ticket_type=='etebari':
    ticket_2=Ticket()
    print(ticket_2)
    print(ticket_2.add_credit())

if ticket_type=='zamani':
    ticket_3 = TicketC()
    print(ticket_3.add_credit())
    print(ticket_3.show_time_credit())
    print(ticket_3.check_expire_time())
