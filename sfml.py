#Made by @shivampatel887


import sys
import os


command = "ls | grep "+ sys.argv[1] +".cpp"
fileWithExt = str(os.popen(command).read())


if (sys.argv[1]+".cpp\n") == fileWithExt:
    print("Start Compiling...")
    command = "g++ -c " + fileWithExt
    os.system(command)
    command = str("g++ "+ sys.argv[1] + ".o -o " + sys.argv[1] +  " -lsfml-graphics -lsfml-window -lsfml-system -lsfml-audio")
    os.system(command)
    command = "rm " + sys.argv[1] + ".o" 
    os.system(command)
    print("Running Output File ... \n")
    command = "./"+ sys.argv[1]
    os.system(command)
    print("Thanks for using our script")
    command = "ls | grep " + sys.argv[1]
    temp = sys.argv[1] + "\n"
    binary = os.popen(command).read()
    if(binary == temp):
        command = "rm " + sys.argv[1]    
        os.system(command)

else:
    print("\nParameter Error!")

sys.exit()



