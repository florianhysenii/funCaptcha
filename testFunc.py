
from anticaptchaofficial.funcaptchaproxyless import *

solver = funcaptchaProxyless()
solver.set_verbose(1)
solver.set_key("b9616b54e7724410f9e8ef752887684f")
solver.set_website_url("https://website.com")
solver.set_website_key("XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX")

# optional funcaptcha API subdomain, see our Funcaptcha documentation for details
# solver.set_js_api_domain("custom-api-subdomain.arkoselabs.com")

# optional data[blob] value, read the docs
# solver.set_data_blob("{\"blob\":\"DATA_BLOB_VALUE_HERE\"}")

token = solver.solve_and_return_solution()
if token != 0:
    print "result token: "+token
else:
    print "task finished with error "+solver.error_code