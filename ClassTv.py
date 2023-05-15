#create the class
class Tv:
    #create a parameterized constructor
    def __init__(self,channel,volume_level, on_off):
        #attributes of the TV
        self.channel = channel
        self.volume_level = volume_level
        self.on_off = on_off

    #methods
    def tv(self):
        print()
    
    def turn_on(self):
        self.on_off = True
        print("Turn on this TV.")
    
    def turn_off(self):
        self.on_off = False
        print("Turn off this TV.")
    
    def get_channel(self):
        channel = int(input("Enter your desired channel: "))
        self.channel = channel
    
    def set_channel(self,channel):
        print("Your desired channel is" + str(channel))
    
    def get_volume(self):
        volume_level = int(input("Enter your desired volume level: "))
        self.volume_level = volume_level

    def set_channel(self,volume_level):
        print("Your desired channel is" + str(volume_level))

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





        

