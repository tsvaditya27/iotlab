from time import sleep
import RPi.GPIO as GPIO
import sys
motor_channel=(35,37,29,22)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(motor_channel,GPIO.OUT)
GPIO.setup(7,GPIO.IN)
motor_dir = raw_input('select dir a/c\t:')

def output(a, b, c, d):
       GPIO.output(motor_channel,(a, b, c, d))
       sleep(0.02)

H = GPIO.HIGH
L = GPIO.LOW

while True:
       try:
        
              if motor_dir == 'a':
                     print 'anti-clockwise'
                     output(H, L, L, H)
                     output(H, H, L, L)
                     output(L, H, H, L)
                     output(L, L, H, H)                  
                  
              elif motor_dir == 'c':
                     print 'clockwise'
                     output(H, L, L, H)
                     output(L, L, H, H)
                     output(L, H, H, L)
                     output(H, H, L, L)
                  
              else:
                     print 'invalid Direction'
                     break
                  
       except KeyboardInterrupt:
              motor_dir = raw_input('select dir a/c, 0 = exit\t:')
              if motor_dir == '0':
                     break
