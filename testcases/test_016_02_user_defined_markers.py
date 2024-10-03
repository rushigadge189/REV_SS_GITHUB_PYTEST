import pytest


class Test_016_02_user_markers():

    @pytest.mark.customer
    def test_add_cust(self):
        print("\nCUSTOMER ADDED SUCCESSFULLY\n") ;

    @pytest.mark.customer
    def test_del_cust(self):
        print("\nCUSTOMER DELETED SUCCESSFULLY\n") ;

    @pytest.mark.product
    def test_add_prod(self):
        print("\nPRODUCT ADDED SUCCESSFULLY\n");

    @pytest.mark.product
    def test_prod_del(self):
        print("\nPRODUCT DELETED SUCCESSFULLY\n") ;

    @pytest.mark.bill
    def test_add_bil(self):
        print("\nBILL ADDED SUCCESSFULLY\n") ;

    @pytest.mark.bill
    def test_del_bill(self):
        print("\nBILL DELETED SUCCESSFULLY\n") ;

    @pytest.mark.regression
    @pytest.mark.patient
    def test_add_patient(self):


        print("\nPATIENT ADDED SUCCESSFULLY\n") ;

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.patient
    def test_del_patient(self):
        print("\nPATIENT DELETED SUCCESFULLY\n") ;