# python script to genrate can messages 
import os
print("Sending sample mobileye data")
x = 1
while True:
    os.system('cansend can1 766#F1CDFED480EC880F')
    os.system('cansend can1 767#F07F5FCC')
    os.system('cansend can1 768#E03102D480EC8811')
    os.system('cansend can1 769#F07F7CAB')
    os.system('cansend can1 600#0000')
    x += 1000
