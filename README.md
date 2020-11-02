# Continuity_tester
Continuity tester using Micropython in pyboard v1.1

## Getting Started
A basic working project to show the working of continuity tester
the front panel of the project is shown below.

![](https://github.com/santoshkrishnanr/Continuity_tester/blob/main/Front_Panel.png)

* 1,2,3,4,5 are the LED representing the testing wire.
* TEST Button initiates the testing process.
* Short Circuit, InterConnection, and No Connection are the LED representing the Errors.
 
### Instructions to use:

 * One end of the  wire/ cable to be tested is plugged on the left-hand side of the panel
 and the other end of the cable is connected to the right-hand side of the panel (for easy plug-in and out this opposite direction is selected)
 * When the TEST button is pressed. These are the condition checked and shown as output.
 
        * Proper Connection IF all the wire in the cable is connected Proper 
        LED 1,2,3,4,5 glows.
        
        * Short Circuit IF any wire in the cable is damaged or shorted 
        LED representing Short circuit glows and just showing the
        properly connected wire in LED 1,2,3,4,5 with a buzzer sound!!
        
        * InterConnection IF any wire in the cable is interconnected 
        LED representing InterConnection glows and just shows the 
        properly connected wire in LED 1,2,3,4,5 with a buzzer sound!!
        
        * NO Connection IF any or none of the wire is not connected 
        LED representing NO Conenction glows and none of the LED between (1-5) glows for 
        NO Connection and with a buzzer sound!
        
        * * There won't be any buzzer sound if all the wire are connected proper!!

 * until the board is reset the Buzzer won't stops even after the cable is removed showing fault in connection.

## Circuit Diagram 

* Below is the internal circuit diagram with pyboard.
 ![](https://github.com/santoshkrishnanr/Continuity_tester/blob/main/CircuitDiagram.png)
 
        * Connector A on the Left side shows the socket/plug for connecting one end of cable 
        * Connector B on the Right side shows the socket/plug for connecting another end of cable
        * Reset Button, Battery, and LED are connected as shown above.
    
## Program
    
* For any internal changes in programming can be done using [tester.py](https://github.com/santoshkrishnanr/Continuity_tester/blob/main/tester.py)
 

## To Quickly run program without LED connection on pyboard_v1.1
* Download [tester.py](https://github.com/santoshkrishnanr/Continuity_tester/blob/main/tester.py)
  and the latest version of [pyboard.py](https://github.com/micropython/micropython/blob/master/tools/pyboard.py)
  with pyserial library on your computer. 
  
* Connect Jumper wire between Y1:Y6, Y2:Y7, Y3:Y8, Y4:Y10, Y5:Y11 pins 
* And Run (for Linux)

 ```
 $ sudo python pyboard.py tester.py
 ```

* As per the jumper wire connection between pins you get error conditions
  on screen.  
 
 ````
    * Connected 
    * Short circuit
    * Inter Connection
    * Short and Inter Connection
    * No Connection
 ````

* happy coding !!