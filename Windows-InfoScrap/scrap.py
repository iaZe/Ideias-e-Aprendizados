import platform, socket, psutil, subprocess

def get_hostname():
    hostname = socket.gethostname()
    return "Hostname: " + hostname

def get_OS():
    Os = platform.system()
    return "Sistema Operacional: " + Os

def get_Processor():
    cmd = "powershell.exe Get-WmiObject Win32_Processor"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode('utf-8')

def get_Motherboard():
    cmd = "powershell.exe Get-WmiObject Win32_BaseBoard"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode('utf-8')

def get_Ram():
    ram = psutil.virtual_memory()
    return "Memoria RAM: \nTotal: %d MB" % (ram.total / 1024 ** 2)

def get_physical_disk():
    cmd = "powershell.exe Get-PhysicalDisk"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode('utf-8')

def get_installed_programs():        
    cmd = "powershell.exe Get-WmiObject Win32_Product"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    
    out, err = proc.communicate()
    return out.decode('utf-8')

def replace_whitespace():
    with open('output.txt', 'r') as file:
        data = file.read()
        data = data.replace('\n\n', '\n')
        data = data.replace('\n\n\n', '\n')
    with open('output.txt', 'w') as file:   
        file.write(data)

def save_output():
    file = open("output.txt", "w")
    file.write(get_hostname() + " \n")
    file.write(get_OS())
    file.write(get_Processor())
    file.write(get_Motherboard())
    file.write(get_Ram() + " \n")
    file.write(get_physical_disk() + " \n")
    def get_network():
        network = psutil.net_if_addrs()
        for interface_name, interface_addresses in network.items():
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    file.write("Interface de rede: " + interface_name + " \nIP: " + address.address + " \n")
    get_network()
    file.write("Programas instalados: \n")
    file.write(get_installed_programs())
    file.close()

save_output() 
replace_whitespace()

#for line in os.popen('systeminfo'): print(line.rstrip())


