import os, requests, time, random, sys
import pprint


def GeoIP():
    ip_input = input('  IP: ')
    response = requests.get("http://extreme-ip-lookup.com/json/" + ip_input)
    response.json()
    pprint.pprint(response.json())
    time.sleep(10)
    Main()
class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
        self.options()
        while self.gg == True:
            choose = input(str('  root@GeoIP:  '))
            if(choose == str(1)):
                self.cls()
                self.start_logo()
                GeoIP()


    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def start_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
 ██████╗ ███████╗ ██████╗     ██╗██████╗ 
██╔════╝ ██╔════╝██╔═══██╗    ██║██╔══██╗
██║  ███╗█████╗  ██║   ██║    ██║██████╔╝
██║   ██║██╔══╝  ██║   ██║    ██║██╔═══╝ 
╚██████╔╝███████╗╚██████╔╝    ██║██║     
 ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝╚═╝     
                                                                        
        """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def options(self):
        print(self.y + '        [Type "1" To Start!] ' + self.c +' Geo IP Tool. ')

Main()
