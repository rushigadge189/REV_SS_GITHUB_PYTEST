class Test_014_addition():

    def test_01_add2no(self):

        a=100;
        b=25 ;
        add=a+b;
        if(add==125) :
            print("\n----------ADDITION IS SUCCESSFUL----------\n") ;
            print("ADDITION=",add) ;
            assert True ;
        else:
            print("\n-----------SORRY, INVALID OPERTAION----------\n") ;
            assert False ;