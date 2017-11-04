## Blinds open gradual.py script by Edward George www.Etechprojects.wordpress.com ##
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
    print ('current state ' + state)
    Gpio = config.get('blinds', 'gpio pin open') # -> "Gpio"
    print ('Gpio pin ' + Gpio)
    GpioInt = int(re.search(r'\d+', Gpio).group()) #extracts an intiger figure from the string to stop a value error when outputing the GPIO pin
    openTime = config.get('blinds', 'open time(secs)') # -> "closeTime"
    print ('Overall open time ' + openTime + ' seconds')
    openTime = float(openTime)
    divOpenTime = float(openTime)/5
    print ('Gradual open time ' + str(divOpenTime) + ' seconds this will repeat 5 times')
    print ('')

    #setup GPIO pin
    GPIO.setup(GpioInt, GPIO.OUT) #uses the integer figure to setup the GPIO pin

    loop = 0

    if state == 'closed':
        for x in range(0, 5):
            loop += 1
            print ('Gradual opening stage ' + str(loop) + '/5')
            GPIO.output(GpioInt, True)
            time.sleep(divOpenTime)
            GPIO.output(GpioInt, False)
            time.sleep(15)
            
        config.set('blinds', 'state', 'open')
        print ('')
        print ('blinds now open')
        with open('/home/pi/Homeautomation/Blinds/Blinds config.conf', 'w') as f:
            config.write(f)
            f.close
            
    elif state == 'unknown':
        print ('')
        print ('set state in config file in home directory!')
        
    elif state == 'open':
        print ('')
        print ('blinds already open!')
        
    else:
        print ('')
        print ('could not reach config file or unavalible value set as state in config file!')

except KeyboardInterrupt:
    config.read('/home/pi/Homeautomation/Blinds/Blinds config.conf') #read config file
    config.set('blinds', 'state', 'unknown')
    with open('/home/pi/Homeautomation/Blinds/Blinds config.conf', 'w') as f:
            config.write(f)
            f.close
    print ('Stopped!!')
    
except:
    config.read('/home/pi/Homeautomation/Blinds/Blinds config.conf') #read config file
    config.set('blinds', 'state', 'unknown')
    with open('/home/pi/Homeautomation/Blinds/Blinds config.conf', 'w') as f:
            config.write(f)
            f.close
    print ('Other error or exception occurred!')

finally:  
    GPIO.cleanup()
