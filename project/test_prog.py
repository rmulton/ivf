import cover_analyser.test_criteria as tests
import program.examples as examples

if __name__=="__main__":
    # Create the program that we are going to test
    pgm = examples.create_test_program1()
    pgm_while = examples.create_test_program2()
    pgm_while_2 = examples.create_test_program3()

    print("=== First program ===")
    # Test the TA criterion
    ta_test_set = [{"x": 0},{"x": -1},{"x": 1}]
    tests.test_ta(ta_test_set, pgm)

    # Test the TD criterion
    td_test_set = [{"x": 0}]
    tests.test_td(td_test_set, pgm)

    # Test the KTC criterium
    ktc_test_set = [{"x": 0}, {"x": 5}]
    tests.test_ktc(ktc_test_set, pgm, 2)

    # Test the TDef criterium
    test_set = [{"x": 0}, {"x": 5}, {"x": -1}]
    tests.test_tdef(test_set, pgm)

    # Test the TC criterium
    tc_test_set = [{"x": 0}, {"x": 5}, {"x": -1}]
    tests.test_tc(tc_test_set, pgm)

    # Test the ITB criterium
    itb_tests_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_itb(itb_tests_set, pgm ,1)

    # Test the TU criterium
    tu_test_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_tu(tu_test_set, pgm)

    # Test the TDU criterium
    tdu_test_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_tdu(tu_test_set, pgm)

    print("=== End for first program ===")
    # Test the ITB criterium
    itb_tests_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_itb(itb_tests_set,pgm_while,1)

    # Test the TU criterium
    tu_test_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_tu(tu_test_set,pgm_while)

    # Test the TDU criterium
    tdu_test_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_tdu(tu_test_set,pgm_while)


