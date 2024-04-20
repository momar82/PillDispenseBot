import pyfirmata
import time

def rightServo():
    closePostion = 6
    openPostion = 72
    pin9 = board.get_pin('d:9:s')
    pin9.write(closePostion)
    time.sleep(1)
    pin9.write(openPostion)
    time.sleep(2)
    pin9.write(closePostion)
    time.sleep(1)
    
def leftServo():
    closePostion = 160
    openPostion = 75
    pin10 = board.get_pin('d:10:s')
    pin10.write(closePostion)
    time.sleep(1)
    pin10.write(openPostion)
    time.sleep(2)
    pin10.write(closePostion)
    time.sleep(1)
    
def main():

    global board
    board=pyfirmata.Arduino('/dev/ttyACM0')
    
    leftServo()
    rightServo()
        
   

main()