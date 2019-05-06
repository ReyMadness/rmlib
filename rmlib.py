def TaskManager():
    import keyboard
    keyboard.press_and_release("ctrl+shift+esc")

def Screenshot():
    import pyscreenshot
    im = pyscreenshot.grab()
    im.save('screenshot.png')

def WriteText(text):
    import keyboard
    keyboard.write(text)

def GetMousePosition():
    import mouse
    pos = mouse.get_position()
    return(pos)

def GetMonitorResolution():
    from win32api import GetSystemMetrics
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    return(str(width) + "x" + str(height))

def GetIP():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return(IP)

def GetUsername():
    import socket, os
    name1 = os.environ.get('USERNAME')
    name2 = socket.gethostname()
    return(name1 + " (" + name2 + ")")

def GetOS():
    import platform
    return(platform.system() + " " + platform.release())

def GetHardware():
    import wmi
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    cpu_info = computer.Win32_Processor()[0].Name
    gpu_info = computer.Win32_VideoController()[0].Name
    ram_info = float(os_info.TotalVisibleMemorySize) / 1048576
    ram = str(round(float('{0}'.format(ram_info)))) + " GB"
    mb = str(GetHardwareMotherboard())
    return(cpu_info, gpu_info, ram, mb)

def GetHardwareCPU():
    import wmi
    computer = wmi.WMI()
    cpu_info = computer.Win32_Processor()[0].Name
    return(cpu_info)

def GetHardwareGPU():
    import wmi
    computer = wmi.WMI()
    gpu_info = computer.Win32_VideoController()[0].Name
    return(gpu_info)

def GetHardwareRAM():
    import wmi
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    ram_info = float(os_info.TotalVisibleMemorySize) / 1048576
    ram = str(round(float('{0}'.format(ram_info)))) + " GB"
    return(ram)

def GetHardwareMotherboard():
    import win32com
    motherboard_details = []
    strComputer = "."
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
    colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_BaseBoard")
    for objItem in colItems:
	    main_board = {
		    'name': objItem.Name,
		    'description': objItem.Description,
		    'manufacturer': objItem.Manufacturer,
		    'model': objItem.Model,
		    'product': objItem.Product,
		    'serialNumber': objItem.SerialNumber,
		    'version': objItem.Version
	    }
	    motherboard_details.append(main_board)
    mass = str(motherboard_details[0]).split()
    a = len(mass)
    i = 0
    while(i<a):
        if(mass[i] == "'manufacturer':"):
            b = mass[i+1][1:][:-2]
        if(mass[i] == "'product':"):
            c = ""
            while(mass[i+1] != "'serialNumber':"):
                c = c + mass[i+1] + " "
                i += 1
        if(mass[i] == "'serialNumber':"):
            d = mass[i+1][1:][:-2]
        i += 1
    motherboard = b + " " + c[1:][:-3] + " " + d
    i = 0
    return(motherboard)

def Dir():
    import os
    return(os.getcwd())

def Chdir(text):
    import os
    try:
        os.chdir(text)
    except:
        return("ERROR")

def Listdir():
    import os
    return(os.listdir())

def Mkdir(name):
    import os
    os.mkdir(name)

def Remove(name):
    import os
    os.remove(name)

def Rmdir(name):
    import os
    os.rmdir(name)

def Rename(name, new_name):
    import os
    os.rename(name, new_name)

def Clear():
    i = 0
    while(i<30):
        print("\n")
        i += 1
    i = 0

def KillProcess(name):
    import subprocess
    try:
        command = "TASKKILL /IM {}".format(name) + " /F"
        subprocess.check_call(command, shell=True)
    except:
        return("Can't kill '{}".format(name) + "' process")
    else:
        pass

def StartSteamGame(id):
    import subprocess
    if(str(id) == "PUBG"):
        id = 578080
    if(str(id) == "CSGO"):
        id = 730
    if(str(id) == "GTAV"):
        id = 271590
    subprocess.call("start steam://run/{}".format(str(id)), shell=True)

def Start(name):
    import os
    os.system('"' + str(name) + '"')

def Download(link):
    import wget
    wget.download(link)

def Exit():
    exit()

def Speech(text):
    import warnings, os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame import mixer
    from gtts import gTTS
    warnings.filterwarnings("ignore")
    tts = gTTS(text=text, lang='ru')
    tts.save("music.mp3")
    mixer.init()
    mixer.music.load('music.mp3')
    mixer.music.play()
    while(True):
        if(mixer.music.get_busy()):
            pass
        else:
            break
    mixer.music.stop()
    mixer.quit()
    Remove('music.mp3')

def Location():
    from json import load
    from urllib.request import urlopen
    url = 'https://ipinfo.io/' + GetIP() + '/json'
    res = urlopen(url)
    data = load(res)
    loc = ""
    for attr in data.keys():
        if(attr == "city"):
            loc = data[attr]
        if(attr == "region"):
            loc = data[attr] + ", {}".format(loc)
        if(attr == "country"):
            loc = data[attr] + ", {}".format(loc)
        if(attr == "org"):
            loc = loc + ". Провайдер: {}".format(data[attr])
        if(attr == "postal"):
            loc = loc + ". {}".format(data[attr])
        if(attr == "loc"):
            loc = loc + ". {}".format(data[attr])
    return(loc)

def SetImageOnDesktop(image):
    import ctypes
    SPI_SETDESKWALLPAPER = 20
    if(image[2] != "/"):
        im = str(Dir()) + "/" + image
    else:
        im = image
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, im, 0)

def DownloadVideo(link):
    from pytube import YouTube
    try:
        yt = YouTube(link)
    except:
        DownloadVideo(link)
    print(yt.title)
    stream = yt.streams.first()
    stream.download()
    print("Downloaded")

def DoCommand(command):
    import subprocess
    subprocess.call(command, shell=True)

