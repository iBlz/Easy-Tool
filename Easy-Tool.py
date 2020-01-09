import os
import time

def menu():

    os.system("clear")
    time.sleep(1)
    print("""

  _                        _  _               
 | |                      | |(_)              
 | |      ___    __ _   __| | _  _ __    __ _ 
 | |     / _ \  / _` | / _` || || '_ \  / _` |
 | |____| (_) || (_| || (_| || || | | || (_| |
 |______|\___/  \__,_| \__,_||_||_| |_| \__, |
                                         __/ |
                                        |___/ 

""")
    time.sleep(1)
    os.system("clear")
    print("""

  _                        _  _                   
 | |                      | |(_)                  
 | |      ___    __ _   __| | _  _ __    __ _     
 | |     / _ \  / _` | / _` || || '_ \  / _` |    
 | |____| (_) || (_| || (_| || || | | || (_| |  _ 
 |______|\___/  \__,_| \__,_||_||_| |_| \__, | (_)
                                         __/ |    
                                        |___/     

""")
    time.sleep(1)
    os.system("clear")
    print("""

  _                        _  _                      
 | |                      | |(_)                     
 | |      ___    __ _   __| | _  _ __    __ _        
 | |     / _ \  / _` | / _` || || '_ \  / _` |       
 | |____| (_) || (_| || (_| || || | | || (_| |  _  _ 
 |______|\___/  \__,_| \__,_||_||_| |_| \__, | (_)(_)
                                         __/ |       
                                        |___/        

""")
    time.sleep(1)
    os.system("clear")
    print("""

  _                        _  _                         
 | |                      | |(_)                        
 | |      ___    __ _   __| | _  _ __    __ _           
 | |     / _ \  / _` | / _` || || '_ \  / _` |          
 | |____| (_) || (_| || (_| || || | | || (_| |  _  _  _ 
 |______|\___/  \__,_| \__,_||_||_| |_| \__, | (_)(_)(_)
                                         __/ |          
                                        |___/                

""")
    os.system("clear")
    time.sleep(1)
    print("""

  _                        _  _               
 | |                      | |(_)              
 | |      ___    __ _   __| | _  _ __    __ _ 
 | |     / _ \  / _` | / _` || || '_ \  / _` |
 | |____| (_) || (_| || (_| || || | | || (_| |
 |______|\___/  \__,_| \__,_||_||_| |_| \__, |
                                         __/ |
                                        |___/ 

""")
    time.sleep(1)
    os.system("clear")
    print("""

  _                        _  _                   
 | |                      | |(_)                  
 | |      ___    __ _   __| | _  _ __    __ _     
 | |     / _ \  / _` | / _` || || '_ \  / _` |    
 | |____| (_) || (_| || (_| || || | | || (_| |  _ 
 |______|\___/  \__,_| \__,_||_||_| |_| \__, | (_)
                                         __/ |    
                                        |___/     

""")
    time.sleep(1)
    os.system("clear")
    print("""

  _                        _  _                      
 | |                      | |(_)                     
 | |      ___    __ _   __| | _  _ __    __ _        
 | |     / _ \  / _` | / _` || || '_ \  / _` |       
 | |____| (_) || (_| || (_| || || | | || (_| |  _  _ 
 |______|\___/  \__,_| \__,_||_||_| |_| \__, | (_)(_)
                                         __/ |       
                                        |___/        

""")
    time.sleep(1)
    os.system("clear")
    print("""

  _                        _  _                         
 | |                      | |(_)                        
 | |      ___    __ _   __| | _  _ __    __ _           
 | |     / _ \  / _` | / _` || || '_ \  / _` |          
 | |____| (_) || (_| || (_| || || | | || (_| |  _  _  _ 
 |______|\___/  \__,_| \__,_||_||_| |_| \__, | (_)(_)(_)
                                         __/ |          
                                        |___/                

""")
    time.sleep(2)
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
        print(" ")
        print("Installing Kali-Linux...")
        print(" ")
        time.sleep(4)
        os.system("mkdir Kali-Linux")
        os.system("cd /data/data/com.termux/files/home/Kali-Linux")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
        os.system("cd /data/data/com.termux/files/home/Easy-Tool")
        os.system("clear")
        print(" ")
        print("Kali-Linux sucesfully installed...")
        print(" ")
        os.system("clear")
        time.sleep(2)
        print(" ")
        print(" To start/exit Kali-Linux follow steps..")
        print(" ")
        print(" ****************")
        print(" Start Kali-Linux")
        print(" ****************")
        print(" 1. Exit Easy-Tool")
        print(" 2. Type cd Kali-Linux && ./start-kali.sh")
        print(" ****************")
        print(" Exit Kali-Linux")
        print(" ****************")
        print(" 1. To exit type exit")
        print(" ")
        rmenu = input("Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "x":
        os.system("clear")
        print(" ")
        print("Exiting...")
        print(" ")
        exit
        break