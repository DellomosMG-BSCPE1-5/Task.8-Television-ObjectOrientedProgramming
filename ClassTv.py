
#create the class
class Tv:
    #create a parameterized constructor
    def __init__(self, on = "ON", channel = "", volume_level = ""):
        #attributes of the TV
        self.on = on
        self.channel = channel
        self.volume_level = volume_level

    #methods
    def turn_on(self):
        if self.on == "ON":
            print("Your TV is already ON.")
        else:
            print("Turning On the TV...")
            self.on = "ON"     

    def turn_off(self):
        if self.on == "OFF":
            print("Your TV is already OFF.")
        else:
            print("Turning Off the TV...")
            self.on = "OFF"

    def get_channel(self):
        self.channel = int(input("Enter your desired channel (1-120 only): "))
        return(self.channel)
    
    def set_channel(self, channel):
        self.channel = channel
        print("You have set the channel into " + str(self.volume_level))

    def get_volume(self):
        self.volume_level = int(input("Enter your desired volume level (1-7 only): "))
        return(self.volume_level)
    
    def set_volume(self, volume_level):
        self.volume_level = volume_level
        print("You have set the volume into " + str(self.volume_level))

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