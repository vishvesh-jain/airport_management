
from time import sleep
from PriorityQueue import PriorityQueue


class Scheduler:

   
    Queue = None  
    results = []  
    TotalTime = 0 

    
    def __init__(self):
        self.Queue = PriorityQueue()
        self.results = []
        self.TotalTime = self.read_file()

    
    
    def read_file(self):
        self.TotalTime = 10
        with open("Compilers_Python.txt", "r") as fo:
            for line in fo:
                
                string = line.split(',')
                
                ID = string[0].strip()
                sub_time = int(string[1].strip())
                req_start = (string[2].strip())
                length = int(string[3].strip())

                
                self.TotalTime += length

                
                self.Queue.add(ID, sub_time, req_start, length)
        return self.TotalTime

    
    
    def displayQueue(self, time):
    
        displayString = ("At time " + str(time) + " the queue would look like: ")

        for x in range(0, self.Queue.length, 1):
    
            if x == 0:
                displayString += (str(self.Queue.queue[x].Id) + "(Started at " + str(self.Queue.queue[x].actualStartTime) + ")")
            else:
                startTime = self.Queue.queue[x - 1].length + self.Queue.queue[x - 1].actualStartTime + 1
                self.Queue.queue[x].actualStartTime = startTime
                displayString += (", " + str(self.Queue.queue[x].Id) + "(Scheduled for " + str(startTime) + ")")

        return ''.join(displayString)

    
    def start(self):
        time = 0
        self.Queue.queue[0].actualStartTime = time

        while time < self.TotalTime:
    
            self.Queue.increase_time(time)

    
            displayString = self.displayQueue(time)

    
            print(displayString)
            del displayString

    
            if self.takenOff(time) == 1:
                sleep(1)
                time += 1
                if self.Queue.length != 0:
                    self.Queue.queue[0].actualStartTime = time
                    print("\tplane took off")
                else:
                    print("\tplane took off")
                    break

            else:
    
                sleep(1)
                time += 1
    
        print(''.join(self.results))

        return

    def takenOff(self, time):
        temp = self.Queue.peek()
        if temp.actualStartTime + temp.length == time:
            temp.actualEndTime = time
            result = self.Queue.pop()
            string = str(result.Id) + "(" + str(result.actualStartTime) + "-" + str(result.actualEndTime) + "), "
            string2 = ''.join(string)
            self.results.append(string2)
            return 1
        return 0

