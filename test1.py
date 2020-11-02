
def testing_tester(Send,Receive):

    buzz = 0
    Sending = Send
    Receiving = Receive


    def check_connection(s_test, r_test, i):
        global buzz
        output_led = error1 = error2 = error3 = 0
        s_test[0] = 1
        Receiving.remove(r_test)

        if sum(r[0] for r in Receiving) is 1 and r_test[0] is 1:  # and r_test is 1:
        #print('short circuit ')
            error1 = 1
            buzz = 1

        elif sum([r[0] for r in Receiving]) is 1 and r_test[0] is 0:
            #print('inter connection')
            error2 = 1
            buzz = 1

        elif sum([r[0] for r in Receiving]) > 1:
            #print('Short and inter connected')
            error1= error2 = 1
            buzz = 1

        # for proper connection test wire value should be true and others false
        elif sum([r[0] for r in Receiving]) is 0 and r_test[0] is 1:
            output_led = 1
            # print('connected ')

        # if no wire is connected
        else:
            #print('No connection')
            # LED_no_connection.on()
            error3 = 1
            buzz = 1

        Receiving.insert(i, r_test)
        s_test[0] = 0
        return output_led, error1, error2, error3


    def testing(sending, receiving):
        led = [0] * 5
        btotal=ctotal=dtotal=0
        #error=[[0]*3]*5
        for i in range(0,5):

            # print(sending[i],receiving[i])
            a, b, c, d = (check_connection(sending[i], receiving[i], i))
            # print(a, b, c, d)
            led[i] = a
            ctotal = ctotal+c
            btotal = btotal+b
            dtotal = dtotal+d

        #print(btotal,ctotal,dtotal)

        return led,btotal,ctotal,dtotal

    connected_LED, short_circuit, inter_connected, noconnection = (testing(Sending, Receiving))
    print('properconnection', connected_LED)
    print('Short circuit are', short_circuit)
    print('Inter Connected are', inter_connected)
    print('No connection is ', noconnection)
    print('-')

    return connected_LED, short_circuit, inter_connected, noconnection


