# Meerkat class defined here
class Meerkat:
    # initializing the arms length float value, legs length float value, eyes amount integer, if it has a tail as a boolean, and if it is furry as a boolean
    def __init__(self):
        self.armsLength = 10.0 # estimates because there are no real measures out there
        self.legsLength = 10.0 # estimates because there are no real measures out there
        self.eyesAmount = 2
        self.tail = True
        self.furry = True

    #prints out the data into a easy to understand way.
    def printer(self):
        print("The meerkat has a arm length of "+ str(self.armsLength)+" cm, a leg length of "+str(self.legsLength)+" cm, and "+str(self.eyesAmount)+" eyes")
        if(self.tail == True):
            print("It has a tail.")
        else:
            print("It does not havve a tail.")
        if(self.furry == True):
            print("This is a furry friend.")
        else:
            print("This is friend is not furry")

# We add the the class to a variable and use its print function to print out our statements we want
def main():
    meerkats = Meerkat()
    meerkats.printer()

# Executes the main program when script is run
if __name__=="__main__":
    main()
        
