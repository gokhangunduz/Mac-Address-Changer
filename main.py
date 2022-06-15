import subprocess

def userinputs():
    data1 = input("Interface :")
    data2 = input("New Mac Address :")
    changemacaddress(data1, data2)

def changemacaddress(interface, mac_address):
    print("Mac Address Changer Started!")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    checknewmacaddress(interface,mac_address)

def checknewmacaddress(data1,data2):
    if str(subprocess.check_output(["ifconfig",data1])).find(data2) == -1:
        print("Error!")
    else:
        print("Succesful!")

def main():
    userinputs()
main()