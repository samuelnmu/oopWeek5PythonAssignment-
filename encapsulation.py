class XmassTurkey:
    def __init__(self):
        self._turkey = 20
        
    def slaughter(self):
        if self._turkey > 0:
            self._turkey -= 1
            print("Turkey slaughtered")
        else:
            print("All Turkeys slaughtered!")
            
festive = XmassTurkey()
festive.slaughter() 