
#Xbee settings
BS_COMPORT = '/dev/tty.usbserial-AH01H2DU'
# BS_BAUDRATE = 230400     # Use this setting if your Xbee is set to baud rate of 57600
BS_BAUDRATE = 57600
#BS_BAUDRATE = 111111    # Use this setting if your Xbee is set to baud rate of 115200

ROBOTS = []

#This message will be removed in the future. It is here to facilitate from the changeover
#to use of imageproc-settings in projects.
print "shared_multi.py from imageproc-settings"
### Adding these 3 lines because I found this in Josh's Server Dump -- cem
## update: adding these lines solved it ! experiment_multibot_tactile runs...
prevStamp = 0
forces_saved = None
points = [0,0]
