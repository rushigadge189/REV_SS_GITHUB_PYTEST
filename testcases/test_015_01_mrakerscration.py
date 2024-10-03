import pytest


class Test_015_mkcreation():

    @pytest.mark.skip
    def test_01_addition(self):
        a= 10 ;
        b=5 ;
        add=a+b ;
        if(add==15) :
            print("\n----------ADDITION IS SUCCESSFUL----------\n") ;
            print("ADDITION=",add) ;
            assert True ;
        else:
            print("------------SORRY, INVALID OPERATION----------") ;
            assert False ;

    @pytest.mark.xfail
    def test_02_substraction(self):
        a=10;
        b=5 ;
        sub=a-b ;
        if(sub==5) :
            print("\n----------SUBSTRACTION IS SUCCESSFUL-----------") ;
            print("SUBSTRACTION=",sub) ;
            assert True ;
        else:
            print("\n------------SORRY,INVALID OPERATION------------") ;
            assert False ;

    @pytest.mark.skipif
    def test_03_multiplication(self):
        a=10 ;
        b=5 ;
        mul=a*b ;
        if(mul==50) :
            print("\n-----------MULTIPLICATION IS SUCCESSFUL----------\n") ;
            print("MULTIPLICATION=",mul) ;
            assert True ;
        else:
            print("\n----------SORRY, INVALID OPERATION-----------") ;
            assert False ;


    def test_04_division(self):
        a=10 ;
        b=5 ;
        div=a/b ;
        if int((div==2)) :
            print("\n---------DIVISION IS SUCCESSFUL----------\n") ;
            print("DIVISION", div) ;
            assert True ;
        else:
            print("\n\-----------SORRY, INVALID OPEARTION----------n") ;
            assert False ;