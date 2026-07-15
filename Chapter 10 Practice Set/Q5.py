class Train:
    def Tickets(self,TicketsAvailable,TrainNo):
        self.TicketsAvailable=TicketsAvailable
        self.TrainNo=TrainNo
        return (f"The tickets available in TrainNo {self.TrainNo} are {self.TicketsAvailable}")
    def Seats(self,TrainNo,Seatsleft):
        self.TrainNo=TrainNo
        self.Seatsleft=Seatsleft
        return (f"The seats available in TrainNo {self.TrainNo} are {self.Seatsleft}")
    def FareInfo(self,TrainNo,TicketPrice):
        self.TicketPrice=TicketPrice
        self.TrainNo=TrainNo
        return (f"The prices of tickets of TrainNo {self.TrainNo} are Rs{self.TicketPrice}")
from random import randint
TicketAvailable=randint(1,100)
TrainNo=randint(1,21)
Seatsleft=randint(1,51)
TicketPrice=99
A=Train()
print(A.Tickets(TicketAvailable,TrainNo))
print(A.Seats(TrainNo,Seatsleft))
print(A.FareInfo(TrainNo,TicketPrice))