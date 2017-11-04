## Blinds open.py script by Edward George www.Etechprojects.wordpress.com ##
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
    config.read('/home/pi/Homeautomation/Blinds/Blinds config.conf') #read config file 
    state = config.get('blinds', 'state') # -> "state"
    print 'current state ' + state
    openTime = config.get('blinds', 'open time(secs)') # -> "closeTime"
    print 'open time ' + openTime + ' seconds'
    openTime = float(openTime)
    Gpio = config.get('blinds', 'gpio pin open') # -> "Gpio"
    print 'Gpio pin ' + Gpio
    GpioInt = int(re.search(r'\d+', Gpio).group()) #extracts an intiger figure from the string to stop a value error when outputing the GPIO pin

    #setup GPIO pin
    GPIO.setup(GpioInt, GPIO.OUT) #uses the integer figure to setup the GPIO pin

    if state == 'closed':
        GPIO.output(GpioInt, True)
        time.sleep(openTime)
        GPIO.output(GpioInt, False)
        config.set('blinds', 'state', 'open')
        print ''
        print 'blinds now open'
        with open('/home/pi/Homeautomation/Blinds/Blinds config.conf', 'w') as f:
            config.write(f)
            f.close

    elif state == 'unknown':
        print ''
        print 'set state in config file in home directory!'
        
    elif state == 'open':
        print ''
        print 'blinds already open!'
        
    else:
        print ''
        print 'could not reach config file or unavalible value set as state in config file!'

except KeyboardInterrupt:
    config.read('/home/pi/Homeautomation/Blinds/Blinds config.conf') #read config file
    config.set('blinds', 'state', 'unknown')
    with open('/home/pi/Homeautomation/Blinds/Blinds config.conf', 'w') as f:
            config.write(f)
            f.close
    print 'Stopped!!'
    
except:
    config.read('/home/pi/Homeautomation/Blinds/Blinds config.conf') #read config file
    config.set('blinds', 'state', 'unknown')
    with open('/home/pi/Homeautomation/Blinds/Blinds config.conf', 'w') as f:
            config.write(f)
            f.close
    print "Other error or exception occurred!"

finally:  
    GPIO.cleanup()
            


