#create the class
class Tv:
    #create a parameterized constructor
    def __init__(self):
        #attributes of the TV
        self.channel = int(input("Enter your desired channel: "))
        self.volume_level = int(input("Enter your desired volume level: "))
        self.on = "On"

    #methods
    def tv(self):
        self.television = (input("Create your own television. Type 'tv', underscore(_), and the number you want. Example: 'tv_1':  "))
        return(self.television)
    
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False
    
    def get_channel(self):
        return(self.channel)
    
    def set_channel(self, channel):
        self.channel = channel

    def get_volume(self):
        return(self.volume_level)
    
    def set_volume(self, volume_level):
        self.volume_level = volume_level

    def channel_up(self):
        channel_up = self.channel + 1
        print ("Channel: " + str(channel_up))
    
    def channel_down(self):
        channel_down = self.channel - 1
        print ("Channel: " + str(channel_down))

    def volume_up(self):
        volume_up = self.volume_level + 1
        print ("Channel: " + str(volume_up))
    
    def volume_down(self):
        volume_down = self.volume_level - 1
        print ("Channel: " + str(volume_down))





        

