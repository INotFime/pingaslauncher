# Importing Needed Packages
import os
import dearpygui.dearpygui as dpg
import webbrowser

# Lists For Preset Versions And window Positions
verlist = ["MineReam", "MCC Island", "Latest", "Custom"]
accountpos = [0, 125]
custompos = [350, 125]
aboutpos = [650, 287]

# Creating Main Window
dpg.create_context()
dpg.create_viewport(title='PingasLauncher', width=854, height=480)

# Creating Functions
def verselect():
    ver = dpg.get_value("verlist")
    ismsa = dpg.get_value("msaenabled")
    if ver == "MineReam":
        mineream()
    elif ver == "MCC Island":
        if ismsa == True:
            mccisland()
        else:
            dpg.configure_item("error_onlylicense", show=True)
    elif ver == "Latest":
        latest()
    else:
        custom()

def custom():
    ismsa = dpg.get_value("msaenabled")
    email = dpg.get_value("email")
    folder = dpg.get_value("versionfolder")
    version = dpg.get_value("versionselected")
    if ismsa == True:
        os.system(f'portablemc --main-dir {folder} start {version} -l {email} -m')
    else:
        os.system(f'portablemc --main-dir {folder} start {version} -u {email}')

def mineream():
    ismsa = dpg.get_value("msaenabled")
    email = dpg.get_value("email")
    if ismsa == True:
        os.system(f'portablemc --main-dir G:/PyProjects/PingasLauncher/versions/mineream start fabric:1.19.2 -l {email} -m -s mineream.aboba.host')
    else:
        os.system(f'portablemc --main-dir G:/PyProjects/PingasLauncher/versions/mineream start fabric:1.19.2 -u {email} -s mineream.aboba.host')

def mccisland():
    email = dpg.get_value("email")
    os.system(f'portablemc --main-dir G:/PyProjects/PingasLauncher/versions/mcc start fabric:1.19.2 -l {email} -m -s play.mccisland.net')

def latest():
    ismsa = dpg.get_value("msaenabled")
    email = dpg.get_value("email")
    if ismsa == True:
        os.system(f'portablemc start -l {email} -m')
    else:
        os.system(f'portablemc start -u {email}')

def settingsshow():
    ver = dpg.get_value("verlist")
    if ver == "Custom":
        dpg.configure_item("customversion", show=True)
    else:
        dpg.configure_item("customversion", show=False)

def hyperlink(text, address):
    b = dpg.add_button(label=text, callback=lambda:webbrowser.open(address))
    dpg.bind_item_theme(b, "hyperlinkTheme")

# Setting Theme For Hyperlinks
with dpg.theme(tag="hyperlinkTheme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [29, 151, 236, 25])
        dpg.add_theme_color(dpg.mvThemeCol_Text, [29, 151, 236])

# Creating Windows
with dpg.window(label="Game", tag="gamelauncher", autosize=True):
    dpg.add_button(label="Launch", callback=verselect)
    dpg.add_listbox(items=verlist, label="Select Preset Version", tag="verlist", callback=settingsshow)

with dpg.window(label="Account Settings", tag="account", autosize=True, pos=accountpos):
    dpg.add_checkbox(label="MSA Account?", tag="msaenabled")
    dpg.add_input_text(label="Email Or Nickname", hint="Type account email or nickname if offine mode", tag="email")

with dpg.window(label="Version Settings", tag="customversion", autosize=True, pos=custompos, show=False):
    dpg.add_input_text(label="Version", hint="Type verison name", tag="versionselected")
    dpg.add_text("For list of supported versions refer to versions.txt file")
    dpg.add_separator()
    dpg.add_input_text(label="Folder", hint="Type game folder", tag="versionfolder", default_value="%appdata%/.minecraft")
    dpg.add_separator()
    dpg.add_text("Running game with modloaders hasn't been implemented yet")

with dpg.window(label="Error!", modal=True, show=False, tag="error_onlylicense", no_title_bar=True):
    dpg.add_text("You can launch into the server only through the license!")
    dpg.add_separator()
    dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("error_onlylicense", show=False))

with dpg.window(label="Error!", modal=True, show=False, tag="error_wip", no_title_bar=True):
    dpg.add_text("This part of launcher is Work In Progress!")
    dpg.add_separator()
    dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("error_wip", show=False))

with dpg.window(label="About", tag="about", pos=aboutpos):
    dpg.add_text("Created by JustPast#1433")
    hyperlink("GitHub", "https://github.com/INotFime/pingaslauncher")
    dpg.add_separator()
    dpg.add_text("Used:")
    hyperlink("DearPyGui", "https://github.com/hoffstadt/DearPyGui")
    hyperlink("portablemc", "https://github.com/mindstorm38/portablemc")

# Rendering Main Window
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()