class Event():
    #setting default values for all major values
    #program will specify all values are required for input
    
    def __init__(self, startTime = "", endTime = "",inputDate = "", location = "None", category = "None", repeat = 0):

        self.startHr = int(startTime.split(":")[0])
        self.startMinute = int(startTime.split(":")[1])

        self.endHr = int(endTime.split(":")[0])
        self.endMinute = int(endTime.split(":")[1])
        
        self.location = location
         
        dated = inputDate.split("/")
        self.day = int(dated[0])
        self.month = int(dated[1])
        self.year = int(dated[2])

        # category is a string that represents the type of event
        self.category = category

        #0 represents no repeat and is value by default. 1 represents every week, 2 every other week, etc
        self.repeat = repeat 

    #helper functions
    def conflict(self,otherEvent):
        print(self.year, otherEvent.year)
        if(self.year == otherEvent.year and self.month == otherEvent.month and self.day == otherEvent.day):
            print("\n")
            #looking at hour overlap
            if(self.startHr < otherEvent.startHr and self.endHr > otherEvent.endHr):
                return True
            elif(self.startHr > otherEvent.startHr and self.endHr < otherEvent.endHr):
                return True
            #looking at minute overlap
            elif(self.startHr == otherEvent.startHr and self.endHr == otherEvent.endHr): # same start hour and end hour
                if(self.startMinute < otherEvent.startMinute and self.endMinute > otherEvent.endMinute):
                    return True
                elif(self.startMinute > otherEvent.startMinute and self.endMinute < otherEvent.endMinute):
                    return True
            elif(self.startHr == otherEvent.startHr): # only same start hour
                if(self.startMinute < otherEvent.startMinute and otherEvent.endHr > otherEvent.endHr):
                    return True
                elif(self.startMinute > otherEvent.startMinute and otherEvent.endHr < otherEvent.endHr):
                    return True
            elif(self.endHr == otherEvent.endHr): # only same end hour
                if(self.endMinute < otherEvent.endMinute and otherEvent.startHr > otherEvent.startHr):
                    return True
                elif(self.endMinute > otherEvent.endMinute and otherEvent.startHr < otherEvent.startHr):
                    return True
        else:
            return False


    #return functions
