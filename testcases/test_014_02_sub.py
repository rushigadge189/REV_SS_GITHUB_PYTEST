class Test_014_substraction():

    def test_014_sub2no(self):

        a=100;
        b=25;
        sub=a-b ;
        if(sub==75) :
            print("\n------------SUBSTRATION IS SUCCESSFUL----------\n") ;
            print("SUBSTARCTION=",sub) ;
            assert True ;
        else:
            print("\n----------SORRY,INVALID OPERATION-----------\n") ;
            assert False ;