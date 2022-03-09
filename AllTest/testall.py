from AllTest.test_all_service import test_All_Service
from AllTest.testdomain import test_domain
from AllTest.testrepository import test_all_repository


def test_all():
    test_domain()
    test_all_repository()
    test_All_Service()
