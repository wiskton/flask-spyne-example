from suds.client import Client

c = Client('http://localhost:8000/soap?wsdl')
print c.service.say_hello("Willem", 10)