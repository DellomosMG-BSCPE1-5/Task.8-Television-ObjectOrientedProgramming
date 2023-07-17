from ClassTv import Tv
from colorama import Fore, Style


#FOR TELEVISION 1
print(Fore.YELLOW + "\n\nFor Telivision 1: \n" + Fore.BLUE + "=" * 105 + Fore.WHITE + Style.NORMAL)

#construct a TV Object
television_1 = Tv()
#access method inside class
television_1.set_channel()
television_1.set_volume()
print(Fore.YELLOW + "\nTv1's channel is " + str(television_1.get_channel()) + " and volume level is " + str(television_1.get_volume()))
print(Fore.BLUE + "=" * 105)


#FOR TELEVISION 2
print(Fore.YELLOW + "\n\nFor Telivision 2: \n" + Fore.BLUE + "=" * 105 + Fore.WHITE + Style.NORMAL)

#construct a TV Object
television_2 = Tv()
#access method inside class
television_2.set_channel()
television_2.set_volume()
print(Fore.YELLOW + "\nTv2's channel is " + str(television_2.get_channel()) + " and volume level is " + str(television_2.get_volume()))
print(Fore.BLUE + "=" * 105 + "\n")
