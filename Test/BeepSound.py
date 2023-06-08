# Import the library that allows us to play sound
import winsound 

times=2 # Number of times to beep
frequency=1000 # Beep frequency in Hz
duration=1000 # Beep duration in ms

# Function to play beep sound
def beepsound():
    for i in range(times): # Number of beeps
        # Beep
        winsound.Beep(frequency,duration)        
beepsound() # function call 