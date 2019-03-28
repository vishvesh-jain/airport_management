
from Information import Information


class PriorityQueue:

    
    queue = [Information]      
    tempQueue = [Information]  
    length = None              
    tempQueueLength = 0        

    
    def __init__(self):
        self.queue = []
        self.tempQueue = []
        self.length = 0
        self.tempQueueLength = 0

    
    def add(self, ID, sub_time, req_start, length):
        if self.length == 0:
            self.queue.append(Information(ID, sub_time, req_start, length))
            self.length += 1

    
        elif self.queue[0].subTime < sub_time:

    
            if self.tempQueueLength == 0:
                self.tempQueue.append(Information(ID, sub_time, req_start, length))
                self.tempQueueLength += 1

    
            else:
                self.sort_by_sub_time(self.tempQueue, self.tempQueueLength,Information(ID, sub_time, req_start, length))
                self.tempQueueLength += 1
    
        else:
            self.sort_by_sub_time(self.queue, self.length, Information(ID, sub_time, req_start, length))
            self.length += 1

    
    def pop(self):
        self.length -= 1
        return self.queue.pop(0)

    
    def peek(self):
        if self.length != 0:
            return self.queue[0]
        else:
            return 0

    def sort_by_sub_time(self, array, size, obj):
        for x in range(0, size, 1):
            if obj.subTime < array[x].subTime:
                array.insert(x, obj)
                break
        array.append(obj)
        return array


    def increase_time(self, time):
        for x in range(0, self.length, 1):
            for y in range(0, self.tempQueueLength, 1):

                if self.tempQueue[y].subTime == time:

                    if self.queue[x].slotReq > self.tempQueue[y].slotReq:

                        self.queue.insert(x, self.tempQueue[y])
                        self.tempQueue.remove(self.tempQueue[y])
                        self.tempQueueLength -= 1
                        self.length += 1