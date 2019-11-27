import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    
#==========================================
# Purpose: 
#   A constructor that initializes a Pokemon object 
# Input Parameter(s): 
#   line is  a single string representing the line in the CSV file that 
#   contains the Pokemon’s data  
# Return Value(s): 
#   None    
#==========================================
    
    def __init__(self,line):
        lst = line.split(',')
        self.dex = lst[0]
        self.name = lst[1]
        self.catchRate = int(lst[2]) 
        self.speed = int(lst[3])
        
#==========================================
# Purpose: 
#   Creates a string representation of the Pokemon (their name)      
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   A string - the Pokemon's name       
#==========================================
        
    def __str__(self):
        return self.name


#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    
#==========================================
# Purpose: 
#   A constructor that initializes the Safari Simulator, a game that simulates 
#   catching Pokemon 
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None    
#==========================================    
    
    def __init__(self, master=None):
        print("In SafariSimulator init")
        
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        fp = open('pokedex.csv')
        lines = fp.readlines()
        self.pokemon = []
        for i in range(1,len(lines)):
            self.pokemon.append(Pokemon(lines[i]))
        fp.close()
        
        #Have some way of keeping track of the number of Safari balls left
        #starting at 30, and stop the Safari adventure once that number reaches 0.
        self.ballsLeft = 30 
        
        #Keep track of all captured Pokémon
        self.captured = []
        
        #Initialize any instance variables you want to keep track of
        self.prob = 0
        self.string = ''
        
        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()

        #Call nextPokemon() method here to initialize your first random pokemon
        self.nextPokemon()

#==========================================
# Purpose: 
#   Creates the widgets used in the Safari Simulator 
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None    
#========================================== 

    def createWidgets(self):
        print("In createWidgets")
        #See the image in the instructions for the general layout required
        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()
        
        #You need to create an additional "throwButton"
        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Safari Ball ("+str(self.ballsLeft)+" left)"
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack()

        #A label for status messages has been completed for you as an example:
        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        #You need to create two additional labels:

        #Complete and pack the pokemonImageLabel here.
        self.imageLabel = tk.Label()
        self.imageLabel.pack()

        #Complete and pack the catchProbLabel here.
        self.catchProbLabel = tk.Label(bg="grey")
        self.catchProbLabel.pack(fill="x", padx=5, pady=5)

#==========================================
# Purpose: 
#   Updates the Pokemon in the Simulator (and the corresponding widgets)
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None    
#========================================== 

    def nextPokemon(self):
        print("In nextPokemon")
        
        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        self.currentPokemon = random.choice(self.pokemon)
        
        self.prob = min((self.currentPokemon.catchRate+1),151)/449.5
        self.percent = int(100*self.prob)
        
        self.messageLabel['text'] = "You encountered a wild "+str(self.currentPokemon)
        self.catchProbLabel['text'] = "Your chance of catching it is "+str(self.percent)+"%!"

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
        self.photo = tk.PhotoImage(file = 'sprites/'+self.currentPokemon.dex+'.gif')
        self.imageLabel['image'] = self.photo
        

#==========================================
# Purpose: 
#   Simulates throwing a ball to try to catch a Pokemon 
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None    
#========================================== 
        
    def throwBall(self):
        print("In throwBall")
        
        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
        if random.random() < (self.prob):
            self.captured.append(self.currentPokemon)
            self.nextPokemon()
        else:
            self.messageLabel['text'] = "Aargh! It escaped!"
        
        self.ballsLeft -= 1    
        
        self.throwButton["text"] = "Throw Safari Ball ("+str(self.ballsLeft)+" left)"
        
        if self.ballsLeft == 0:
            self.endAdventure()

#==========================================
# Purpose: 
#   Displays messages at the end of the game 
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None    
#==========================================         
        
    def endAdventure(self):
        print("In endAdventure")
        
        #This method must: 

            #Display adventure completion message
            #List captured pokemon
        
        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.
        
        for poke in self.captured:
            self.string += str(poke)+'\n'
        
        self.runButton.pack_forget()
        self.throwButton.pack_forget()
        self.messageLabel['text'] = 'You’re out of balls, I hope you had fun!'
        self.imageLabel.pack_forget()
        
        if len(self.pokemon) == 0:
            self.catchProbLabel['text'] = 'Oops, you caught 0 Pokemon.'
        else:
            self.catchProbLabel['text'] = 'You caught '+str(len(self.captured))+' Pokemon:\n'+self.string 




#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
