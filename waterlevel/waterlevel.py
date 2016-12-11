import time
import wiringpi2

# the value of the 'other' resistor
SERIESRESISTOR=560
 
# What pin to connect the sensor to
SENSORPIN=22
 
def main():
    for pin in range(50):
        wiringpi2.wiringPiSetupGpio()
        wiringpi2.pinMode(pin, 0)
        reading = wiringpi.analogRead(pin)
       
        print("Analog reading ")
        print(reading)
       
        if reading != 0:
            # convert the value to resistance
            reading = (1023 / reading)  - 1
            reading = SERIESRESISTOR / reading
            print("Sensor resistance ") 
            print(reading)        
        
        #time.sleep(1)

if __name__ == "__main__":
     main()
