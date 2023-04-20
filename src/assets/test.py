import RPi.GPIO as GPIO
import time

global pwmobj                    # declare the pmwobj as a global variable
RPI_Pin = 18                     # define the RPI GPIO Pin we will use with PWM
RPI_DutyCycle = int(input('Enter a duty cycle percentage from 0-100 in integer format : '))   # user defines the Duty Cycle in percentage
RPI_Freq = 100              # define the frequency in Hz
RPI_CircTime = 310                # the time you want the circuit to run for (secs)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)              # set actual GPIO BCM Numbers
GPIO.setup(RPI_Pin, GPIO.OUT)         # set RPI_PIN as OUTPUT mode
GPIO.output(RPI_Pin, GPIO.LOW)        # set RPI_PIN LOW to at the start
pwmobj = GPIO.PWM(RPI_Pin, RPI_Freq)  # Initialise instance and set Frequency
pwmobj.start(0)                       # set initial Duty cycle to 0 & turn on PWM

def start():
    pwmobj.ChangeDutyCycle(RPI_DutyCycle)               # Set PWM Duty Cycle to 50%
    time.sleep(RPI_CircTime)                             # Keep circuit running for 60 secs

def destroy():
    pwmobj.stop()                                               # stop PWM

if __name__ == '__main__':                                      # Program entry point
    print ('Circuit Turned on with Duty Cycle of ', RPI_DutyCycle)  # Print duty cycle
    try:
        start()                                                 # call start function
    except KeyboardInterrupt:                                   # Watches for Ctrl-C
        destroy()                                               # call destroy funct
    finally:
        destroy()                                               # call destroy funct
