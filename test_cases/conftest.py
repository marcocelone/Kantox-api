import pytest
from config_files import setup

#from base.enviroment_setting import EnvSettings

@pytest.yield_fixture()
def setUp():
    print("Starting tests")
    yield
    print("\nTest Ended")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, environment):

    if environment == 'local':
        base_url = setup.base_url
    else:
        print("invalid entries")

    if request.cls is not None:
        request.cls.base_url = base_url

    yield base_url
    print("\nEnding Automation")


def pytest_addoption(parser):
    parser.addoption("--env")

@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--env")

