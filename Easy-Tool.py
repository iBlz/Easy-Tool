import os
import time

def menu():
    os.system("clear")
    
    print("""
    
  ______                     _______             _ 
 |  ____|                   |__   __|           | |
 | |__    __ _  ___  _   _     | |  ___    ___  | |
 |  __|  / _` |/ __|| | | |    | | / _ \  / _ \ | |
 | |____| (_| |\__ \| |_| |    | || (_) || (_) || |
 |______|\__,_||___/ \__, |    |_| \___/  \___/ |_|
                      __/ |                        
                     |___/                         

[ 1 ] Kali-Linux
[ 2 ] Ubuntu
[ 3 ] Debian
[ 4 ] Parrot-OS
[ 5 ] Leap
[ 6 ] Tumbleweed
[ 7 ] 
[ 8 ] 
[ 9 ] 
[ x ] Exit
""")
loop = True
while loop:
    menu()
    what = input(">> ")
#------------------------------------------------------------------------------
    if what == "1":
        os.system("clear")
        os.system("rm -rf kali.sh")
        os.system("rm -rf start-kali.sh")
        os.system("rm -rf kali-binds")
        os.system("rm -rf kali-fs")
        print(" ")
        print("Installing Kali-Linux...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
        os.system("cd /data/data/com.termux/files/home/")
        
        os.system("clear")
        print(" ")
        print("Kali-Linux sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""
    
  ______                     _______             _ 
 |  ____|                   |__   __|           | |
 | |__    __ _  ___  _   _     | |  ___    ___  | |
 |  __|  / _` |/ __|| | | |    | | / _ \  / _ \ | |
 | |____| (_| |\__ \| |_| |    | || (_) || (_) || |
 |______|\__,_||___/ \__, |    |_| \___/  \___/ |_|
                      __/ |                        
                     |___/                         

[ 1 ] Start Kali-Linux
[ 2 ] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            print(" ")
            print("To exit type exit")
            print(" ")
            time.sleep(2)
            os.system("clear")
            os.system("./start-kali.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
    elif what == "x":
        os.system("clear")
        print(" ")
        print("Exiting...")
        print(" ")
        exit
        break
#------------------------------------------------------------------------------
    elif what == "2":
        os.system("clear")
        os.system("rm -rf start-ubuntu.sh")
        os.system("rm -rf ubuntu-binds")
        os.system("rm -rf ubuntu-fs")
        os.system("rm -rf ubuntu.sh")
        print(" ")
        print("Installing Ubuntu...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("Ubuntu sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""
    
  ______                     _______             _ 
 |  ____|                   |__   __|           | |
 | |__    __ _  ___  _   _     | |  ___    ___  | |
 |  __|  / _` |/ __|| | | |    | | / _ \  / _ \ | |
 | |____| (_| |\__ \| |_| |    | || (_) || (_) || |
 |______|\__,_||___/ \__, |    |_| \___/  \___/ |_|
                      __/ |                        
                     |___/                         

[ 1 ] Start Ubuntu
[ 2 ] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            print(" ")
            print("To exit type exit")
            print(" ")
            time.sleep(2)
            os.system("clear")
            os.system("./start-ubuntu.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
#------------------------------------------------------------------------------
    elif what == "3":
        os.system("clear")
        os.system("rm -rf start-debian.sh")
        os.system("rm -rf debian-binds")
        os.system("rm -rf debian-fs")
        os.system("rm -rf debian.sh")
        print(" ")
        print("Installing Debian...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("Debian sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""
    
  ______                     _______             _ 
 |  ____|                   |__   __|           | |
 | |__    __ _  ___  _   _     | |  ___    ___  | |
 |  __|  / _` |/ __|| | | |    | | / _ \  / _ \ | |
 | |____| (_| |\__ \| |_| |    | || (_) || (_) || |
 |______|\__,_||___/ \__, |    |_| \___/  \___/ |_|
                      __/ |                        
                     |___/                         

[ 1 ] Start Debian
[ 2 ] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            print(" ")
            print("To exit type exit")
            print(" ")
            time.sleep(2)
            os.system("clear")
            os.system("./start-debian.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
#------------------------------------------------------------------------------
    elif what == "4":
        os.system("clear")
        os.system("rm -rf start-parrot.sh")
        os.system("rm -rf parrot-binds")
        os.system("rm -rf parrot-fs")
        os.system("rm -rf parrot.sh")
        print(" ")
        print("Installing Parrot-OS...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("Parrot-OS sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""
    
  ______                     _______             _ 
 |  ____|                   |__   __|           | |
 | |__    __ _  ___  _   _     | |  ___    ___  | |
 |  __|  / _` |/ __|| | | |    | | / _ \  / _ \ | |
 | |____| (_| |\__ \| |_| |    | || (_) || (_) || |
 |______|\__,_||___/ \__, |    |_| \___/  \___/ |_|
                      __/ |                        
                     |___/                         

[ 1 ] Start Parrot-OS
[ 2 ] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            print(" ")
            print("To exit type exit")
            print(" ")
            time.sleep(2)
            os.system("clear")
            os.system("./start-parrot.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
#------------------------------------------------------------------------------
    elif what == "5":
        os.system("clear")
        os.system("rm -rf opensuse-leap-binds")
        os.system("rm -rf opensuse-leap-fs")
        os.system("rm -rf opensuse-leap.sh")
        os.system("rm -rf start-leap.sh")
        print(" ")
        print("Installing Leap...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("Leap sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""
    
  ______                     _______             _ 
 |  ____|                   |__   __|           | |
 | |__    __ _  ___  _   _     | |  ___    ___  | |
 |  __|  / _` |/ __|| | | |    | | / _ \  / _ \ | |
 | |____| (_| |\__ \| |_| |    | || (_) || (_) || |
 |______|\__,_||___/ \__, |    |_| \___/  \___/ |_|
                      __/ |                        
                     |___/                         

[ 1 ] Start Leap
[ 2 ] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            print(" ")
            print("To exit type exit")
            print(" ")
            time.sleep(2)
            os.system("clear")
            os.system("./start-leap.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
#------------------------------------------------------------------------------
    elif what == "6":
        os.system("clear")
        os.system("./start-tumbleweed.sh")
        print(" ")
        print("Installing Tumbleweed...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("Tumbleweed sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""
    
  ______                     _______             _ 
 |  ____|                   |__   __|           | |
 | |__    __ _  ___  _   _     | |  ___    ___  | |
 |  __|  / _` |/ __|| | | |    | | / _ \  / _ \ | |
 | |____| (_| |\__ \| |_| |    | || (_) || (_) || |
 |______|\__,_||___/ \__, |    |_| \___/  \___/ |_|
                      __/ |                        
                     |___/                         

[ 1 ] Start Tumbleweed
[ 2 ] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            print(" ")
            print("To exit type exit")
            print(" ")
            time.sleep(2)
            os.system("clear")
            os.system("./start-tumbleweed.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
#------------------------------------------------------------------------------
        