import os
import time

def menu():
    os.system("clear")
    
    print("""\033[31m

    ______                             ______            __
   / ____/___ ________  __            /_  __/___  ____  / /
  / __/ / __ `/ ___/ / / /  ______     / / / __ \/ __ \/ / 
 / /___/ /_/ (__  ) /_/ /  /_____/    / / / /_/ / /_/ / /  
/_____/\__,_/____/\__, /             /_/  \____/\____/_/   
                 /____/                                    

                   \033[94mCreated By Toxic-Omega

\033[32m[ \033[31m0 \033[32m] Install All

\033[32m[ \033[31m1 \033[32m] Install Kali-Linux       \033[32m[ \033[31m11 \033[32m] Start Kali-Linux
\033[32m[ \033[31m2 \033[32m] Install Ubuntu           \033[32m[ \033[31m22 \033[32m] Start Ubuntu
\033[32m[ \033[31m3 \033[32m] Install Debian           \033[32m[ \033[31m33 \033[32m] Start Debian
\033[32m[ \033[31m4 \033[32m] Install Parrot-OS        \033[32m[ \033[31m44 \033[32m] Start Parrot-OS
\033[32m[ \033[31m5 \033[32m] Install Leap             \033[32m[ \033[31m55 \033[32m] Start Leap
\033[32m[ \033[31m6 \033[32m] Install Tumbleweed       \033[32m[ \033[31m66 \033[32m] Start Tumbleweed

\033[32m[ \033[31mx \033[32m] Exit
""")
loop = True
while loop:
    menu()
    what = input(">> ")
#------------------------------------------------------------------------------
    if what == "1":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Kali-Linux...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Kali-Linux sucesfully installed...")
        print(" ")
        print("""\033[31m

    ______                             ______            __
   / ____/___ ________  __            /_  __/___  ____  / /
  / __/ / __ `/ ___/ / / /  ______     / / / __ \/ __ \/ / 
 / /___/ /_/ (__  ) /_/ /  /_____/    / / / /_/ / /_/ / /  
/_____/\__,_/____/\__, /             /_/  \____/\____/_/   
                 /____/                                    
                 
                   \033[94mCreated By Toxic-Omega

\033[32m[ \033[31m1 \033[32m] Start Kali-Linux
\033[32m[ \033[31m2 \033[32m] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            time.sleep(2)
            os.system("ls")
            os.system("clear")
            os.system("./start-kali.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
#------------------------------------------------------------------------------
    elif what == "2":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Ubuntu...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Ubuntu sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""\033[31m
        
    ______                             ______            __
   / ____/___ ________  __            /_  __/___  ____  / /
  / __/ / __ `/ ___/ / / /  ______     / / / __ \/ __ \/ / 
 / /___/ /_/ (__  ) /_/ /  /_____/    / / / /_/ / /_/ / /  
/_____/\__,_/____/\__, /             /_/  \____/\____/_/   
                 /____/                                    
                 
                   \033[94mCreated By Toxic-Omega

\033[32m[ \033[31m1 \033[32m] Start Ubuntu
\033[32m[ \033[31m2 \033[32m] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            time.sleep(2)
            os.system("ls")
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
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Debian...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Debian sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""\033[31m
        
    ______                             ______            __
   / ____/___ ________  __            /_  __/___  ____  / /
  / __/ / __ `/ ___/ / / /  ______     / / / __ \/ __ \/ / 
 / /___/ /_/ (__  ) /_/ /  /_____/    / / / /_/ / /_/ / /  
/_____/\__,_/____/\__, /             /_/  \____/\____/_/   
                 /____/                                     
        
                   \033[94mCreated By Toxic-Omega

\033[32m[ \033[31m1 \033[32m] Start Debian
\033[32m[ \033[31m2 \033[32m] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            time.sleep(2)
            os.system("ls")
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
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Parrot-OS...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Parrot-OS sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""\033[31m
    
    ______                             ______            __
   / ____/___ ________  __            /_  __/___  ____  / /
  / __/ / __ `/ ___/ / / /  ______     / / / __ \/ __ \/ / 
 / /___/ /_/ (__  ) /_/ /  /_____/    / / / /_/ / /_/ / /  
/_____/\__,_/____/\__, /             /_/  \____/\____/_/   
                 /____/                                    

                   \033[94mCreated By Toxic-Omega

\033[32m[ \033[31m1 \033[32m] Start Parrot-OS
\033[32m[ \033[31m2 \033[32m] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            time.sleep(2)
            os.system("ls")
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
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Leap...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Leap sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""\033[31m
    
    ______                             ______            __
   / ____/___ ________  __            /_  __/___  ____  / /
  / __/ / __ `/ ___/ / / /  ______     / / / __ \/ __ \/ / 
 / /___/ /_/ (__  ) /_/ /  /_____/    / / / /_/ / /_/ / /  
/_____/\__,_/____/\__, /             /_/  \____/\____/_/   
                 /____/                                    

                   \033[94mCreated By Toxic-Omega

\033[32m[ \033[31m1 \033[32m] Start Leap
\033[32m[ \033[31m2 \033[32m] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            os.system("clear")
            time.sleep(2)
            os.system("ls")
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
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Tumbleweed...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/home/")
        os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh")
        os.system("cd /data/data/com.termux/files/home/")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Tumbleweed sucesfully installed...")
        print(" ")
        time.sleep(3)
        print("""\033[31m
    
    ______                             ______            __
   / ____/___ ________  __            /_  __/___  ____  / /
  / __/ / __ `/ ___/ / / /  ______     / / / __ \/ __ \/ / 
 / /___/ /_/ (__  ) /_/ /  /_____/    / / / /_/ / /_/ / /  
/_____/\__,_/____/\__, /             /_/  \____/\____/_/   
                 /____/                                    

                   \033[94mCreated By Toxic-Omega

\033[32m[ \033[31m1 \033[32m] Start Tumbleweed
\033[32m[ \033[31m2 \033[32m] Go to Menu
""")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "1":
            os.system("exit")
            time.sleep(2)
            os.system("ls")
            os.system("clear")
            os.system("./start-tumbleweed.sh")
        if rmenu == "2":
            os.system("clear")
            menu()
        else:
            exit
#------------------------------------------------------------------------------
    elif what == "11":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Starting Kali-Linux...")
        print(" ")
        time.sleep(3)
        os.system("ls")
        os.system("clear")
        os.system("./start-kali.sh")
#------------------------------------------------------------------------------
    elif what == "22":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Starting Ubuntu...")
        print(" ")
        time.sleep(3)
        os.system("ls")
        os.system("clear")
        os.system("./start-ubuntu.sh")
#------------------------------------------------------------------------------
    elif what == "33":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Starting Debian...")
        print(" ")
        time.sleep(3)
        os.system("ls")
        os.system("clear")
        os.system("./start-debian.sh")
#------------------------------------------------------------------------------
    elif what == "44":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Starting Parrot...")
        print(" ")
        time.sleep(3)
        os.system("ls")
        os.system("clear")
        os.system("./start-parrot.sh")
#------------------------------------------------------------------------------
    elif what == "55":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Starting Leap...")
        print(" ")
        time.sleep(3)
        os.system("ls")
        os.system("clear")
        os.system("./start-leap.sh")
#------------------------------------------------------------------------------
    elif what == "66":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Starting Tumbleweed...")
        print(" ")
        time.sleep(3)
        os.system("ls")
        os.system("clear")
        os.system("./start-tumbleweed.sh")
#------------------------------------------------------------------------------
    elif what == "0":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Are you sure you want to install all? [y/n]")
        print(" ")
        rmenu = input(">> ")
        if rmenu == "y":
            os.system("clear")
            print(" ")
            print("\033[32m[\033[31m*\033[32m] This will take long time...")
            print(" ")
            time.sleep(3)
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
            os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
            os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh")
            exit
        if rmenu == "2":
            os.system("clear")
            exit
        else:
            exit
#------------------------------------------------------------------------------
    elif what == "x":
        os.system("ls")
        os.system("clear")
        print(" ")
        print("Exiting...")
        print(" ")
        exit
        break
#------------------------------------------------------------------------------
