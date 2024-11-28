#Client Program
import xmlrpc.client
# Create an object to connect to the server
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    # Test addition
    print("Addition: 5 + 3 =", proxy.add(5, 3))
    # Test subtraction
    print("Subtraction: 10 - 3 =", proxy.subtract(10, 3))
    # Test multiplication
    print("Multiplication: 2 * 2 =", proxy.multiply(2, 2))
    # Test division
    print("Division: 2 / 2 =", proxy.divide(2, 2))
