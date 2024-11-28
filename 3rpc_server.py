#Server Program
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
# Restricting to a specific path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Server setup
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Function to be called by the client
    def add(x, y):
        return x + y
       
    def subtract(x, y):
        return x + y
    
    def multiply(x, y):
        return x + y 
    
    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    # Register the functions to be accessible by the client
    server.register_function(add, 'add')
    server.register_function(subtract, 'subtract')
    server.register_function(multiply, 'multiply')
    server.register_function(divide, 'divide')

    print("Server is running on port 8000...")
    # Run the server's main loop
    server.serve_forever()
