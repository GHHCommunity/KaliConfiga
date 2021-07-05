import os
import time
import colorama
from colorama import Fore

if os.geteuid() != 0:
    exit(Fore.RED+ "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
print(Fore.RED + '''
 

                                                                          
,--. ,--.        ,--.,--. ,-----.                ,---.,--.                
|  .'   / ,--,--.|  |`--''  .--./ ,---. ,--,--, /  .-'`--' ,---.  ,--,--. 
|  .   ' ' ,-.  ||  |,--.|  |    | .-. ||      \|  `-,,--.| .-. |' ,-.  | 
|  |\   \  '-'  ||  ||  |'  '--'\  '-' '|  ||  ||  .-'|  |' '-' '\ '-'  | 
`--' '--' `--`--'`--'`--' `-----' `---' `--''--'`--'  `--'.`-  /  `--`--' 
                                                          `---' ''')
print(Fore.WHITE + "                                                     Author Name:" + Fore.GREEN + "R00tDev1l")
print(Fore.WHITE + "                                                     Author Email:" + Fore.GREEN + "indradas4863@gmail.com")   
print(Fore.WHITE + "                                                     Date Created:" + Fore.GREEN + "01/07/2021")
print(Fore.WHITE + "                                                     Join Our Facebook Group:" + Fore.GREEN + "https://www.facebook.com/grayhathackerscommunity")
print(Fore.WHITE + "")
######################################################################################################################################################################
def install_more_packgages():
    print("")
    print(Fore.WHITE + "Author Name:" + Fore.GREEN + "Joy Ghosh")
    print(Fore.WHITE + "Tool Name:" + Fore.GREEN + "Zero-Instal")
    print(Fore.WHITE + "Date Created:" + Fore.GREEN + "22/03/2021")
    print("")
    os.system('curl -s https://raw.githubusercontent.com/JoyGhoshs/0install/main/0install | bash')
    print("")
    print(Fore.WHITE + "Github Link:" + Fore.GREEN + "https://github.com/JoyGhoshs")
    print("")
######################################################################################################################################################################
os.system('rm /etc/apt/sources.list')
os.system('echo "deb https://kali.download/kali/ kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 1 configuration complete")
print(Fore.WHITE + "")
os.system('echo "deb https://ftp.debian.org/debian stable main contrib non-free" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 2 configuration complete")
print(Fore.WHITE + "")
os.system('echo "deb https://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 3 configuration complete")
print(Fore.WHITE + "")
os.system('echo "deb https://http.kali.org/kali kali-last-snapshot main non-free contrib" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 4 configuration complete")
print(Fore.WHITE + "")
os.system('echo "deb https://http.kali.org/kali kali-experimental main non-free contrib" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 5 configuration complete")
print(Fore.WHITE + "")
os.system('echo "deb-src https://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 6 configuration complete")
print(Fore.WHITE + "")
os.system('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 7 configuration complete")
print(Fore.WHITE + "")
os.system('echo "deb http://ftp.de.debian.org/debian buster main" | sudo tee -a /etc/apt/sources.list')
print(Fore.GREEN + "[✔]Source 8 configuration complete")
######################################################################################################################################################################
print(Fore.WHITE + "")
print(Fore.RED + "[⌛]Updating your system.Please wait until the update finished.(-_-)")
print(Fore.WHITE + "")
os.system('apt-get update')
print("")
print(Fore.GREEN + "[✔]Update Finished!")
######################################################################################################################################################################
try:
	print(Fore.WHITE + "")
	print(Fore.RED + "Configuring and Updating Pip in python2.7 and Pip3 in python3")
	print(Fore.WHITE + "")
	os.system('wget https://raw.githubusercontent.com/Darkhaxxor005/PythonPIPs/main/get-pip.py')
	print("")
	os.system('wget https://raw.githubusercontent.com/Darkhaxxor005/PythonPIPs/main/get-pip3.py')
	print(Fore.WHITE + "")
	os.system('python3 get-pip3.py')
	print("")
	os.system('pip3 install --upgrade pip')
	print("")
	os.system('python get-pip.py')
	print("")
	os.system('pip install --upgrade pip')
	os.system('rm get-pip.py')
	os.system('rm get-pip3.py')
	os.system('pip --version')
	print("")
	os.system('pip3 --version')
except:
	pass
######################################################################################################################################################################
#If you want to install docker just remove the # before the entire code and make it executeable.
#try:
#	print(Fore.GREEN + "Installing Docker in your system")
#	print(Fore.WHITE + "")
#	os.system('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -')
#	print("")
#	os.system('echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" | sudo tee /etc/apt/sources.list.d/docker.list')
#	print("")
#	os.system('sudo apt update')
#	print("")
#	os.system('sudo apt remove docker docker-engine docker.io')
#	print("")
#	os.system('sudo apt install docker-ce -y')
#	print("")
#except:
#	pass
######################################################################################################################################################################

os.system('apt list --upgradeable')
print("")
try:
	ver1 = int(input(Fore.GREEN + "[" + Fore.RED + "Recommended" + Fore.GREEN +"]Do you want to upgrade these following packages(1.Yes/2.No)?=>"))
	if ver1 == 1:
		print(Fore.WHITE + "")
		os.system('apt-get upgrade')
		ver2 = int(input(Fore.GREEN + "[" + Fore.BLUE + "Optional" + Fore.GREEN + "]Do you want to install some extra packages(1.Yes/2.No)?=>"))
		if ver2 == 1:
			install_more_packgages()
			print(Fore.GREEN + "[✔]Upgrade Successfull.\n[✔]Extra Packages installation successful.")
			time.sleep(1)

		elif ver2 == 2:
			print(Fore.GREEN + "[✔]Upgrade Successfull." + Fore.RED + "\n[✘]Extra Packages not installed.")
			time.sleep(1)

		else:
			print(Fore.RED + "Invalid Input[Exiting]")

	elif ver1 == 2:
		print("")
		ver2 = int(input(Fore.GREEN + "[" + Fore.BLUE + "Optional" + Fore.GREEN + "]Do you want to install some extra packages(1.Yes/2.No)?=>")
		if ver2 == 1:
			install_more_packgages()
			print(Fore.RED + "[✘]Upgrade not successfull." + Fore.GREEN + "\n[✔]Extra Packages installation successful.")
			time.sleep(1)

		elif ver2 == 2:
			print("")
			print(Fore.RED + "[✘]Upgrade not successfull.\n[✘]Extra Packages installation not successful.")
			print(Fore.WHITE + "")
			time.sleep(1)

        	
		else:
			print(Fore.RED + "Invalid Input[Exiting]")
	else:
		print(Fore.RED + "Invalid Input[Exiting]")
        

	print(Fore.GREEN + '''

   Kali Linux Configuration Complete!.................
	 		 ______       _             
	 		|  ____|     (_)            
	 		| |__   _ __  _  ___  _   _ 
	 		|  __| | '_ \| |/ _ \| | | |
	 		| |____| | | | | (_) | |_| |
	 		|______|_| |_| |\___/ \__, |
	 		            _/ |       __/ |
 	 		           |__/       |___/ 
                                     .................................''')

except KeyboardInterrupt:
	os.system('exit') 
