# Animal class defined here
class animal:
    # initializing the name of the animal as a string arms length float value, legs length float value, eyes amount integer, if it has a tail as a boolean, and if it is furry as a boolean
    def __init__(self, name, armsLength, legsLength, eyesAmount, tail, furry):
        self.name = name 
        self.armsLength = armsLength 
        self.legsLength = legsLength
        self.eyesAmount = eyesAmount
        self.tail = tail
        self.furry = furry

    #prints out the data into a easy to understand way.
    def printer(self):
        print("The "+ self.name + " has a arm length of "+ str(self.armsLength)+" cm, a leg length of "+str(self.legsLength)+" cm, and "+str(self.eyesAmount)+" eyes")
        if(self.tail == True):
            print("It has a tail.")
        else:
            print("It does not havve a tail.")
        if(self.furry == True):
            print("This is a furry friend.")
        else:
            print("This is friend is not furry")

# We add the the class with the arugments to a variable and use its print function to print out our statements we want
def main():
    # These are inputed as the attributes of a meerkat (arms and legs are estimates because there are no real measures out there)
    meerkats = animal("meerkat", 10.0, 10.0, 2, True, True)
    meerkats.printer()

# Executes the main program when script is run
if __name__=="__main__":
    main()
        
