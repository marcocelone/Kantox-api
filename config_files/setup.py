base_url = "https://demo.kantox.com/api/"
headers = {'Content-Type': 'application/json'}
ref_number = '8TV212TCY'
company_name = "Demo Company"
suprevisor = 'marcocelone16@gmail.com​'

login_endpoint='/login'
check_valid_token_endpoint = '/token_valid'
logoff_endpoint = '/logoff'
orders_quote_endpoint = '/companies/'+ref_number+'/orders/quote'
create_orders_endpoint = '/companies/'+ref_number+'/orders/create'
company_orders_index_endpoint = '/companies/'+ref_number+'/orders/index'
order_details = '/companies/'+ref_number+'/orders/show'




