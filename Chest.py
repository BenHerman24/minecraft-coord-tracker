maxChestItemAmout = 3456

class Chest:
    ''' a chest you can add and remove from '''
    def __init__(self, startItemNumber):
        self.items = startItemNumber
    
    def addItems(self, amount):
        ''' add items to the chest '''
        if self.items + amount > maxChestItemAmout:
            self.items = maxChestItemAmout
        else:
            self.items += amount

    def removeItems(self, amount):
        ''' remove items to the chest '''
        if self.items - amount < 0:
            self.items = 0
        else:
            self.items -= amount

    def isFull(self):
        ''' returns true if the chest is full '''
        return self.items == maxChestItemAmout

    def isEmpty(self):
        ''' returns true if the chest is empty '''
        return self.items == 0