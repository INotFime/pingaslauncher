# Importing Needed Packages
import os
import dearpygui.dearpygui as dpg
import webbrowser

# Lists For Preset Versions And window Positions
verlist = ["Latest", "Custom"]
accountpos = [0, 125]
custompos = [350, 125]
aboutpos = [650, 263]
rconpos = [0,240]

# Creating Main Window
dpg.create_context()
dpg.create_viewport(title='PingasLauncher', width=854, height=480)

# Creating Functions
def verselect():
    ver = dpg.get_value("verlist")
    if ver == "Latest":
        latest()
    else:
        custom()

def custom():
    ismsa = dpg.get_value("msaenabled")
    email = dpg.get_value("email")
    folder = dpg.get_value("versionfolder")
    version = dpg.get_value("versionselected")
    if ismsa:
        os.system(f'portablemc\portablemc.exe --main-dir {folder} start {version} -l {email} -m')
    else:
        os.system(f'portablemc\portablemc.exe --main-dir {folder} start {version} -u {email}')

def latest():
    ismsa = dpg.get_value("msaenabled")
    email = dpg.get_value("email")
    if ismsa:
        os.system(f'portablemc\portablemc.exe start -l {email} -m')
    else:
        os.system(f'portablemc\portablemc.exe start -u {email}')

def settingsshow():
    ver = dpg.get_value("verlist")
    if ver == "Custom":
        dpg.configure_item("customversion", show=True)
    else:
        dpg.configure_item("customversion", show=False)

def hyperlink(text, address):
    b = dpg.add_button(label=text, callback=lambda:webbrowser.open(address))
    dpg.bind_item_theme(b, "hyperlinkTheme")

def ban():
    nick = dpg.get_value("bannick")
    reason = dpg.get_value("banreason")
    ip = dpg.get_value("rconip")
    port = dpg.get_value("rconport")
    password = dpg.get_value("rconpass")
    os.system(f'mcrcon -H {ip} -P {port} -p {password} "ban {nick} {reason}"')

def terminal():
    ip = dpg.get_value("rconip")
    port = dpg.get_value("rconport")
    password = dpg.get_value("rconpass")
    os.system(f'mcrcon\mcrcon.exe -H {ip} -P {port} -p {password}')

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
    dpg.add_separator()
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

with dpg.window(label="RCON Server", tag="rcon", autosize=True, pos=rconpos):
    dpg.add_input_text(label="RCON IP", hint="Enter Server IP", tag="rconip")
    dpg.add_input_text(label="RCON Port", hint="Enter RCON Port", tag="rconport", default_value="25575")
    dpg.add_input_text(label="RCON Password", hint="Enter RCON Password", password=True, tag="rconpass")
    dpg.add_separator()
    dpg.add_input_text(label="Player Nickname", hint="Enter Player Nickname", tag="bannick")
    dpg.add_input_text(label="Reason", hint="Enter Reason (if needed)", tag="banreason")
    dpg.add_button(label="Ban Player", callback=ban)
    dpg.add_separator()
    dpg.add_button(label="Open Terminal (in cmd)", callback=terminal)

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
    hyperlink("mcrcon", "https://github.com/Tiiffi/mcrcon")

# Rendering Main Window
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
