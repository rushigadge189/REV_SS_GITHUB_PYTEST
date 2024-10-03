class Test_014_multiplication():

    def test_014_mul2no(self):

        a=100 ;
        b=25 ;
        mul=a*b ;
        if(mul==2500) :
            print("\n-----------MULTIPLICATION IS SUCCESSFUL----------\n") ;
            print("MULTIPLICATION=",mul) ;
            assert True ;
        else:
            print("\n-----------SORRY, INVALID OPERATION----------\n") ;
            assert False ;
