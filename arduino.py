import serial
import time

def arduino_control():
     print('THIS IS A SCRIPT THAT ALLOWS A USER TO TURN AN LED ON AND OFF FOR THE ARDUINO')
     print("Type 'H' to turn the LED ON")
     print("Type 'L' to turn the LED ON")
     print("Type 'q' to QUIT")

     s=serial.Serial('COM3',9600)
     time.sleep(2)

     command='L'
     while command!='q':
          command=input('Select: H = on, L = off, q = quit\n')
          s.write(command.encode('ascii')) #this is sending data in ASCII format for the arduino to understand
          time.sleep(0.5)
     
     print('q entered! Exciting the Program')
     s.close()

if __name__ == '__main__':
     arduino_control()