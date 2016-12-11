import time
import wiringpi

# the value of the 'other' resistor
SERIESRESISTOR=560
 
# What pin to connect the sensor to
SENSORPIN=22
 
def main():
    while True:
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(22, 0)
        reading = wiringpi.analogRead(SENSORPIN)
       
        print("Analog reading ")
        print(reading)
       
        # convert the value to resistance
        reading = (1023 / reading)  - 1
        reading = SERIESRESISTOR / reading
        print("Sensor resistance ") 
        print(reading)
        
        time.sleep(1)

if __name__ == "__main__":
     main()