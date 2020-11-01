#!/bin/bash

from pyb import Pin
import time

# Pin connection for Sending side of connector A
s_1 = Pin('Y1', Pin.OUT_PP)
s_2 = Pin('Y2', Pin.OUT_PP)
s_3 = Pin('Y3', Pin.OUT_PP)
s_4 = Pin('Y4', Pin.OUT_PP)
s_5 = Pin('Y5', Pin.OUT_PP)

# Pin connection for Receiving side of connector B
r_1 = Pin('Y6', Pin.IN, Pin.PULL_DOWN)
r_2 = Pin('Y7', Pin.IN, Pin.PULL_DOWN)
r_3 = Pin('Y8', Pin.IN, Pin.PULL_DOWN)
r_4 = Pin('Y10', Pin.IN, Pin.PULL_DOWN)
r_5 = Pin('Y11', Pin.IN, Pin.PULL_DOWN)


# LED Pin connection corresponding to the connector position.
LED1_output = Pin('X17', Pin.OUT_PP)
LED2_output = Pin('X18', Pin.OUT_PP)
LED3_output = Pin('X19', Pin.OUT_PP)
LED4_output = Pin('X20', Pin.OUT_PP)
LED5_output = Pin('X21', Pin.OUT_PP)

# LED pin connection for Error identification.
LED_short_circuit = Pin('X1', Pin.OUT_PP)
LED_inter_connection = Pin('X2', Pin.OUT_PP)
LED_no_connection = Pin('X3', Pin.OUT_PP)

# Pin connection for buzzer.
buzzer = Pin('X10', Pin.OUT_PP)

buzz = 0
Sending = [s_1, s_2, s_3, s_4, s_5]
Receiving = [r_1, r_2, r_3, r_4, r_5]


# This Function takes each input and tests with all the outputs(other side of wire)
# s_test is the one end of wire (L,N,E..) and checks if the r_test is correct
#  _test is wire to be tested and compared with others for error.

def testing(s_test, r_test):
    global buzz # if error buzzer gets flagged.
    s_test.high()  # setting the sending_test wire to high
    output_led = 0
    Receiving.remove(r_test) # remove the test wire from list for comparision.

    # compare for short circuit. if the output is in testing and other wire.
    if sum([r.value() for r in Receiving]) is 1 and r_test.value() is 1:
        print('short circuit ')
        LED_short_circuit.on()
        buzz = 1

    # compare for inter connection between testing wire and other wire.
    elif sum([r.value() for r in Receiving]) is 1 and r_test.value() is 0:
        print('inter connection')
        LED_inter_connection.on()
        buzz = 1

    # compare for both the cases inter connection and short circuit.
    elif sum([r.value() for r in Receiving]) > 1:
        print('Short and inter connected')
        LED_inter_connection.on()
        LED_short_circuit.on()
        buzz = 1

    # for proper connection test wire value should be true and others false
    elif sum([r.value()for r in Receiving])is 0 and r_test.value()is 1:
        output_led = 1
        print('connected ')

    # if no wire is connected
    else:
        print('No connection')
        LED_no_connection.on()
        buzz = 1

    # adding back the receiver_testing wire in receiving list
    Receiving.append(r_test)
    s_test.low()
    return output_led


# for sending_pin,testing_pin in zip(sending,receiving):
#   testing(sending_pin,testing_pin)

# condition for testing each wire from sending end and actual receiving end.

if (testing(s_1, r_1)) is 1:
    LED1_output.on()

if (testing(s_2, r_2)) is 1:
    LED2_output.on()

if (testing(s_3, r_3)) is 1:
    LED3_output.on()

if (testing(s_4, r_4)) is 1:
    LED4_output.on()

if (testing(s_5, r_5)) is 1:
    LED5_output.on()

# to display the error flg
print(buzz)

# if any error start the buzzer. else sleep  after 3 min to save power
# using machine.deepsleep()

while (buzz>0):

    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
    time.sleep(0.5)


