import sys
import json
from data_files.login import login
from data_files.orders import orders
from config_files import setup
import pytest


from request_models.request_methods import REQ

print(sys.path)

@pytest.mark.usefixtures('oneTimeSetUp')
class TestTC():

    #Set Up
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.req = REQ()
        self.token = self.req.get_token(login.login, login.password, setup.login_endpoint)
        self.my_token = self.token[1]['token']
        self.empty_token = None

    # Verify token
    @pytest.mark.run(order=1)
    def test_verify_valid_token(self):
        verify_token = self.req.get(self.base_url, setup.check_valid_token_endpoint, self.my_token)
        assert verify_token[0]== 200
        success = verify_token[1]['status']
        assert success == 'success'

    # Verify valid token endpoint missing token in header
    @pytest.mark.run(order=2)
    def test_verify_valid_token_no_token(self):
        verify_token = self.req.get(self.base_url, setup.check_valid_token_endpoint, self.empty_token)
        assert verify_token[0] == 401
        success = verify_token[1]['errorDetails']
        assert success == 'token not valid'

    # Request a quote
    @pytest.mark.run(order=3)
    def test_request_a_quote(self):
        request_quote = self.req.post(self.base_url, setup.orders_quote_endpoint, orders.orders_quote_payload, self.my_token )
        assert request_quote[0] == 200
        message = request_quote[1]['status']
        assert message == "success"

    # Request a quote with no token in header
    @pytest.mark.run(order=4)
    def test_request_a_quote_no_token(self):
        request_quote = self.req.post(self.base_url, setup.orders_quote_endpoint, orders.orders_quote_payload,
                                     self.empty_token)
        assert request_quote[0] == 403
        message = request_quote[1]['errorDetails']
        assert message == "Unauthorized. Invalid token"

    # Request a quote with missing required currency field in json
    @pytest.mark.run(order=5)
    def test_request_a_quote_missing_currency(self):
        request_quote = self.req.post(self.base_url, setup.orders_quote_endpoint, orders.missing_required_field,
                                     self.my_token)
        assert request_quote[0] == 403
        message = request_quote[1]['errorDetails']
        assert message == "currency: Currency is required"

    # Create a order no token in header
    @pytest.mark.run(order=6)
    def test_create_a_order_no_token(self):
        global order_reference
        create_quote = self.req.post(self.base_url, setup.create_orders_endpoint, orders.create_order_payload,
                                     self.empty_token)
        assert create_quote[0] == 403
        message = create_quote[1]['errorDetails']
        assert message == "Unauthorized. Invalid token"

    # Create an order
    @pytest.mark.run(order=7)
    def test_create_a_quote(self):
        global order_reference
        create_quote = self.req.post(self.base_url, setup.create_orders_endpoint, orders.create_order_payload,
                                     self.my_token)
        assert create_quote[0] == 200
        message = create_quote[1]['status']
        assert message == "success"
        order_reference = create_quote[1]['kantoxOrderRef']
        assert order_reference != None

    # Get order with reference
    @pytest.mark.run(order=8)
    def test_get_order_reference(self):
        payload = {"orderRef":order_reference}
        get_company_orders = self.req.get_body(self.base_url, setup.company_orders_index_endpoint, payload, self.my_token)
        assert get_company_orders[0] == 200
        success = get_company_orders[1][0]['status']
        assert success == 'success'

    # Get Company orders index
    @pytest.mark.run(order=9)
    def test_get_company_oreders_index(self):
        get_company_orders = self.req.get(self.base_url, setup.company_orders_index_endpoint, self.my_token)
        assert get_company_orders[0] == 200
        success = get_company_orders[1][0]['status']
        assert success == 'success'

    # Get Company orders index missing token in header
    @pytest.mark.run(order=10)
    def test_get_company_oreders_index_no_token(self):
        get_company_orders = self.req.get(self.base_url, setup.company_orders_index_endpoint, self.empty_token)
        assert get_company_orders[0] == 403
        message = get_company_orders[1]['errorDetails']
        assert message == "Unauthorized. Invalid token"

    #Get Company orders with body
    @pytest.mark.run(order=11)
    def test_get_company_oreders_index_body(self):
        get_company_orders = self.req.get_body(self.base_url, setup.company_orders_index_endpoint,
                                               orders.get_company_orders_body, self.my_token)
        assert get_company_orders[0] == 200
        success = get_company_orders[1][0]['status']
        assert success == 'success'


