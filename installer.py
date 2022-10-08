import os


def install(package):
    print(f"Installing {package}")
    os.system(f"pip install {package}")


install("portablemc")
input("Finished installing PingasLauncher. Now you can launch it through main.py file.\nPress Enter To Exit")
