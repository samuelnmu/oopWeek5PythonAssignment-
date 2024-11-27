class machine:
    def specs(self):
        return "4500cc"      
class colorMachine:
    def specs(self):
        return "Mate"              
#polymorphisim
for ride in [machine(), colorMachine()]:
    print(ride.specs())
    
    
