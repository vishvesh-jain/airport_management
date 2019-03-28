class Information:

    Id = None               
    subTime = None          
    slotReq = None          
    length = None           
    actualStartTime = 0     
    actualEndTime = 0       

    def __init__(self, Id, subTime, slotReq, length):
        self.Id = Id
        self.subTime = subTime
        self.slotReq = slotReq
        self.length = length

    def __str__(self):
        tup = str(self.Id), ",", str(self.subTime), ",", str(self.slotReq), ",", str(self.length)
        return ''.join(tup)

