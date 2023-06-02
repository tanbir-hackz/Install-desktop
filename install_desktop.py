import os

#Import Color

# Info
print("")
print("\033[1;32m Install Desktop \n")
print("")
print("Created By Tanbir Rohoman")
print("")
print("")

# Option
print("1. Install Desktop")
print("")
op = input("Select A Option : ")
print("")


#Instal Pkg
try:
  os.system("apt update && apt upgrade  && pkg install x11-repo tigervnc nano aterm xfce4 ")
except:
 print("Sorry!!")

#Run Tigervc
try:
 os.system("vncserver && vncserver -kill :1 && cd .vnc && nano xstartup")
except:
 print("")

#Run
try:
 os.system("vncserver -geometry 1280x720")
except:
 print("")

#Done 
print("\033[1;32m Tnx For Install Dekstop. This Python File Created By Tanbir Rohoman \n")
