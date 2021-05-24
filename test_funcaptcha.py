from python_anticaptcha import AnticaptchaClient, FunCaptchaTask, Proxy
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 ' \
     '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

api_key = '174faff8fbc769e94a5862391ecfd010'
site_key = 'DE0B0BB7-1EE4-4D70-1853-31B835D4506B'  # grab from site
url = 'https://www.google.com/recaptcha/api2/demo'
proxy = Proxy.parse_url("socks5://login:password@123.123.123.123")

client = AnticaptchaClient(api_key)
task = FunCaptchaTask(url, site_key, proxy=proxy, user_agent=user_agent)
job = client.createTask(task)
job.join()
print job.get_token_response()