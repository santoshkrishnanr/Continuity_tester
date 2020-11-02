import tester_test

s_1 = [0]
s_2 = [0]
s_3 = [0]
s_4 = [0]
s_5 = [0]


"""
ARGUMENT: doc
consider s_1, s_2, s_3, s_4, s_5 as connecting wire  and 
(["first slot"],["second slot"] with its respecting position)

the locations of [s_1, s_2, s_3, s_4, s_5] in second slot  can be interchanged 
representing wrong connected wire  
([1, 1, 1, 1, 1], 0, 0, 0) ==> [1, 1, 1, 1, 1] shows the proper wire connection and 0,0,0 represents the errror.py
([1, 1, 1, 1, 1], 0, 0, 0) ==> ([LED1,LED2,LED3,LED4,LED5], Short circuit,Inter connection,No Connection) 

test1.testing_tester([s_1, s_2, s_3, s_4, s_5],
                     [s_1, s_2, s_3, s_4, s_5])==([1, 1, 1, 1, 1], 0, 0, 0)
eg:1 test1.testing_tester([s_1, s_2, s_3, s_4, s_5],
                          [s_2, s_1, s_5, s_4, s_3])==([1, 1, 1, 1, 1], 0, 0, 0)                  
                     
"""

def test_testing_tester():
    assert tester_test.testing_tester([s_1, s_2, s_3, s_4, s_5],
                                [s_1, s_2, s_3, s_4, s_5])==([1, 1, 1, 1, 1], 0, 0, 0)

    assert tester_test.testing_tester([s_1, s_2, s_3, s_4, s_5],
                                [s_2, s_1, s_3, s_5, s_4])==([0, 0, 1, 0, 0], 1, 4, 0)

    assert tester_test.testing_tester([s_1, s_2, s_3, s_4, s_5],
                               [s_1, s_3, s_3, s_4, s_5])==([1, 0, 0, 1, 1], 1, 1, 1)


test_testing_tester()