#create the class
class Tv:
    #create a parameterized constructor
    def __init__(self):
        #attributes of the TV
        self.channel = int(input("Enter your desired channel: "))
        self.volume_level = int(input("Enter your desired volume level: "))
 


    #methods
    def tv(self):
        self.tv_number = int(input("What is the number of your Tv? Enter the number that corresponds to your Tv: "))
        return(self.tv_number)
    
    def turn_on(self):
        self.on_off = True

    def turn_off(self):
        self.on_off = False
    
    def get_channel(self):
        channel = int(input("Enter your desired channel: "))
        self.channel = channel
    
    def set_channel(self,channel):
        print("Your desired channel is" + str(channel))
    
    def get_volume(self):
        volume_level = int(input("Enter your desired volume level: "))
        self.volume_level = volume_level
        return(self.volume_level)
    
    def set_volume(self):
        return(self.volume_level)
    
    def channel_up(self):
        channel_up = self.channel + 1
        print (channel_up)
    
    def channel_down(self):
        channel_down = self.channel - 1
        print (channel_down)

    def volume_up(self):
        volume_up = self.volume_level + 1
        print (volume_up)
    
    def volume_down(self):
        volume_down = self.volume_level - 1
        print (volume_down)





        

