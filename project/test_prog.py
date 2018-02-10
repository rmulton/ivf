import cover_analyser.test_criteria as tests
import program.examples as examples

def test_program(pgm_name, pgm, test_set, k=5, i=1):
    print("=== Tests for {} ===".format(pgm_name))
    # Test the TA criterion
    tests.test_ta(test_set, pgm)
    # Test the TD criterion
    tests.test_td(test_set, pgm)
    # Test the KTC criterium
    tests.test_ktc(test_set, pgm, k)
    # Test the ITB criterium
    tests.test_itb(test_set, pgm, i)
    # Test the TDef criterium
    tests.test_tdef(test_set, pgm)
    # Test the TU criterium
    tests.test_tu(test_set, pgm)
    # Test the TDU criterium
    tests.test_tdu(test_set, pgm)
    # Test the TC criterium
    tests.test_tc(test_set, pgm)
    print("=== End of the tests for {} ===\n".format(pgm_name))



if __name__=="__main__":
    # Create the program that we are going to test

    # Test program 1
    pgm = examples.create_test_program1()
    pgm_test_set = [ \
        {"x": -2}, \
        {"x": -1}, \
        {"x": 0}, \
        {"x": 1}, \
        {"x": 2}, \
        {"x": 5} \
        ]
    test_program("First program", pgm, pgm_test_set, k=4)

    # Test program While
    pgm_while = examples.create_test_program2()
    pgm_while_test_set = [ \
        {"x": -2}, \
        {"x": -1}, \
        {"x": 0}, \
        {"x": 1}, \
        {"x": 2}, \
        {"x": 5} \
        ]
    test_program("Program while", pgm_while, pgm_while_test_set)
    

    # Test prog with 3 var
    pgm4_test_set = [ \
        {"x": -2, "y":3, "z":5}, \
        {"x": -1, "y":1, "z":0} \
        ]
    pgm4 = examples.create_test_program4()
    test_program("Program 3 variables v1", pgm4, pgm4_test_set)

    # Test prog with 3 var
    pgm5_test_set = [ \
        # Straight to the finale node
        ## Through 2
        {"x": -2, "y":1, "z":2}, \
        {"x": -2, "y":0, "z":-1}, \
        ## Through 3
        {"x": 1, "y":1, "z":2}, \
        {"x": 1, "y":2, "z":-1}, \
        # One loop
        ## Through 2
        {"x": -2, "y":0, "z":2}, \
        {"x": -2, "y":0, "z":5}, \
        ## Through 3
        {"x": 5, "y":2, "z":2}, \
        {"x": 5, "y":2, "z":5}
        ]
    pgm5 = examples.create_test_program5()
    test_program("Program 3 variables v2", pgm5, pgm5_test_set, k=5)
