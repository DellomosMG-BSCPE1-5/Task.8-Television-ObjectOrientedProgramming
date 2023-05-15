from ClassTv import Tv
from colorama import Fore, Style

#FOR TELEVISION 1
print(Fore.YELLOW + "\n\nFor Telivision 1: \n" + Fore.BLUE + "=" * 105 + Fore.WHITE + Style.NORMAL)
#construct a TV Object
television_1 = Tv()
print(Fore.BLUE + "=" * 105)
#access method inside class
print(Fore.WHITE + "Tv1's channel is " + str(television_1.get_channel()) + " and volume level is " + str(television_1.get_volume()))



#FOR TELEVISION 2
print(Fore.YELLOW + "\n\nFor Telivision 2: \n" + Fore.BLUE + "=" * 105 + Fore.WHITE + Style.NORMAL)
#construct a TV Object
television_2 = Tv()
print(Fore.BLUE + "=" * 105)
#access method inside class
print(Fore.WHITE +"Tv2's channel is " + str(television_2.get_channel()) + " and volume level is " + str(television_2.get_volume()))