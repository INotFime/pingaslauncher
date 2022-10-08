# Importing Needed Packages
import os


# Creating Functions
def custom(ismsa, email, folder, version):
    if ismsa:
        if folder == "":
            os.system(f'portablemc\portablemc.exe start {version} -l {email} -m')
        else:
            os.system(f'portablemc\portablemc.exe --main-dir {folder}  start {version} -l {email} -m')
    elif not ismsa:
        if folder == "":
            os.system(f'portablemc\portablemc.exe start {version} -u {email}')
        else:
            os.system(f'portablemc\portablemc.exe --main-dir {folder}  start {version} -u {email}')
    else:
        print("You answered in question 'Is your account MSA? (Microsoft or Offline Acocunt?) (Yes or No)' not True or False selected offline mode")
        if folder == "":
            os.system(f'portablemc\portablemc.exe start {version} -u {email}')
        else:
            os.system(f'portablemc\portablemc.exe --main-dir {folder}  start {version} -u {email}')

def latest(ismsa, email):
    if ismsa:
        os.system(f'portablemc\portablemc.exe start -l {email} -m')
    else:
        os.system(f'portablemc\portablemc.exe start -u {email}')


def ban(nick, reason, ip, port, password):
    os.system(f'mcrcon\mcrcon.exe -H {ip} -P {port} -p {password} "ban {nick} {reason}"')


def terminal(ip, port, password):
    cmd = f'mcrcon\mcrcon.exe -H {ip} -p {password} -P {port}'
    print(cmd)
    os.system(cmd)


def close():
    exit("Closed launcher")


print("PingasLaucher (Terminal Edition)\n")
print(
    "This version does not have GUI\nbecause lack of version of GUI package for 32bit systems\nand creator`s laziness\n")

input("Press Enter to continue\n")

while True:
    command = input("Please enter command you want to execute (Type 'help' if you need list of commands)\n")
    if command == "help":
        print("Available Commands:\n"
              "latest - Starts Latest Version Of Game\n"
              "exit - Closes launcher")

    elif command == "latest":
        ismsa = input("Is your account MSA? (Microsoft or Offline Acocunt?) (Yes or No) ")
        email = input("Type your nickname or email if you selected Yes ")
        latest(ismsa, email)

    elif command == "custom":
        ismsa = input("Is your account MSA? (Yes or No) ")
        email = input("Type your nickname or email if you selected Yes ")
        version = input(
            "Type version of your game (Dont Type Anything And Press Enter For Latest) (please check versions.txt for list of versions) ")
        folder = input("Type folder of your game (Dont Type Anything And Press Enter For Default) ")
        print(folder)
        if version == None:
            if folder == None:
                custom(ismsa, email, "%appdata%\.minecraft", None)
            else:
                custom(ismsa, email, version, folder)
        custom(ismsa, email, folder, version)

    elif command == "terminal":
        ip = input("Type server IP ")
        port = input("Type server port ")
        password = input("Type RCON password ")
        terminal(ip, port, password)

    elif command == "ban":
        ip = input("Type server IP ")
        port = input("Type server port ")
        password = input("Type RCON password ")
        nick = input("Type player to ban")
        reason = input("Type reason for ban")
        ban(nick, reason , port, password)

    elif command == "exit":
        close()
    else:
        print("\nUnknown Command! Please Check If You Wrote It Correctly\n")
