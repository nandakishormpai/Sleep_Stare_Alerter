import os

resp=input("Do you have Visual Studio 2015 build tools installed? (y/n)\n")
if(resp=="n" or resp=="N"):
    os.system('start https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe')

resp=input("\nDo you have CMake v3.8.2 installed? (y/n)\n")
if(resp=="n"or resp=="N"):
    os.system('msiexec /ahttps://github.com/Kitware/CMake/releases/download/v3.18.0/cmake-3.18.0-win64-x64.msi')

print("Requirements being installed. Please wait...")

try:
	os.system('pip install -r requirements.txt')
except:
    os.system('pip3 install -r requirements.txt')




    