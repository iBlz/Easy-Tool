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
[ 2 ] 
[ 3 ] 
[ 4 ] 
[ 6 ] 
[ 5 ] 
[ 7 ] 
[ 8 ] 
[ 9 ] 
[ x ] Exit
""")
loop = True
while loop:
    menu()
    what = input(">> ")
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
        os.system("cd Kali-Linux")
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
[ x ] Exit
""")
        print(" ")
        rmenu = input(">>")
        if rmenu == "1":
            os.system("exit")
            os.system("./start-kali.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        if rmenu == "x":
            os.system("clear")
            print(" ")
            print("Exiting...")
            print(" ")
            exit
        else:
            menu()
    elif what == "x":
        os.system("clear")
        print(" ")
        print("Exiting...")
        print(" ")
        exit
        break