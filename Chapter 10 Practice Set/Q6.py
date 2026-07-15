class Train:
    ticket="The tickets are available"
    status=30
    trains=5
    def info(Udit):
        return(f"{Udit.ticket} No.={Udit.status} and you are travelling in indian railways in which trains running are {Udit.trains}")
N=Train()
print(Train.info(Train))
#No it does not create any impact 