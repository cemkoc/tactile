print 'Using imageproc-settings'
BS_COMPORT = '/dev/tty.usbserial-AH01H2DU' # ron
# BS_COMPORT = 'COM4'
#BS_COMPORT = 'COM3' # duncan, ROBOPROC
BS_BAUDRATE = 230400  //ron's
# BS_BAUDRATE = 57600

DEST_ADDR = '\x20\x52'

motor_gains_set = False
steering_gains_set = False
steering_rate_set = False
pkts = 0
bytesIn = 0
count2deg = 2000.0/(2**15-1)

imudata = [[]] * 300 # HACK should use numSamples
statedata = []
dutycycles = []
ROBOTS = []

# Cross-module variable sharing; these need default values
imudata = []
dataFileName = ''
leadinTime = 0
leadoutTime = 0
angRateDeg = "NOT SET"  #This is only for writing the file header
angRate = "NOT SET"
motorGains = "NOT SET"
steeringGains = "NOT SET"
runtime = 0
numSamples = 0
moveq = "NOT SET"

robotQueried = False
maxQueries = 8
