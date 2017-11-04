## Curtains closed.py script by Edward George www.Etechprojects.wordpress.com ##
## copyright under open sorce GNU licence ##

#import neccessary modules
import time
import RPi.GPIO as GPIO
from ConfigParser import SafeConfigParser
import re

try:
    #set values for imported modules
    config = SafeConfigParser() 
    GPIO.setmode(GPIO.BCM) #set GPIO numbering as BCM

    #get values from config files and turn them into strings
    config.read('/home/pi/Homeautomation/Curtains/Curtains config.conf') #read config file 
    state = config.get('curtains', 'state') # -> "state"
    print 'current state ' + state
    closeTime = config.get('curtains', 'close time(secs)') # -> "closeTime"
    print 'close time ' + closeTime + ' seconds'
    closeTime = float(closeTime)
    Gpio = config.get('curtains', 'gpio pin close') # -> "Gpio"
    print 'Gpio pin ' + Gpio
    GpioInt = int(re.search(r'\d+', Gpio).group()) #extracts an intiger figure from the string to stop a value error when outputing the GPIO pin

    #setup GPIO pin
    GPIO.setup(GpioInt, GPIO.OUT) #uses the integer figure to setup the GPIO pin

    if state == 'open':
        GPIO.output(GpioInt, True)
        time.sleep(closeTime)
        GPIO.output(GpioInt, False)
        config.set('curtains', 'state', 'closed')
        print ''
        print 'curtains now closed'
        with open('/home/pi/Homeautomation/Curtains/Curtains config.conf', 'w') as f:
            config.write(f)
            f.close
            
    elif state == 'unknown':
        print ''
        print 'set state in config file in home directory!'
        
    elif state == 'closed':
        print ''
        print 'curtains already closed!'
        
    else:
        print ''
        print 'could not reach config file or invalid value set as state in config file!'

except KeyboardInterrupt:
    config.read('/home/pi/Homeautomation/Curtains/Curtains config.conf') #read config file
    config.set('curtains', 'state', 'unknown')
    with open('/home/pi/Homeautomation/Curtains/Curtains config.conf', 'w') as f:
            config.write(f)
            f.close
    print 'Stopped!!'
    
except:
    config.read('/home/pi/Homeautomation/Curtains/Curtains config.conf') #read config file
    config.set('curtains', 'state', 'unknown')
    with open('/home/pi/Homeautomation/Curtains/Curtains config.conf', 'w') as f:
            config.write(f)
            f.close
    print "Other error or exception occurred!"

finally:  
    GPIO.cleanup()

