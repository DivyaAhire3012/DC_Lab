from datetime import datetime, timedelta

def berkeley_algorithm(server_time, client1_time, client2_time):
    print(f"Server Clock   = {server_time}")
    print(f"Client Clock1  = {client1_time}")
    print(f"Client Clock2  = {client2_time}")

    # Convert time strings to datetime objects
    format = "%M:%S"
    server = datetime.strptime(server_time, format)
    client1 = datetime.strptime(client1_time, format)
    client2 = datetime.strptime(client2_time, format)

    # Calculate time differences in seconds
    diff1 = (client1 - server).total_seconds()
    print(f"t1 - s = {diff1} seconds")
    diff2 = (client2 - server).total_seconds()
    print(f"t2 - s = {diff2} seconds")

    # Calculate average adjustment
    avg_diff = (diff1 + diff2) / 2
    print(f"(t1 + t2) / 2 = {avg_diff} seconds")

    # Adjust times
    adjusted_server = server + timedelta(seconds=avg_diff)
    adjusted_client1 = client1 + timedelta(seconds=avg_diff - diff1)
    adjusted_client2 = client2 + timedelta(seconds=avg_diff - diff2)

    # Print synchronized clocks
    print(f"Synchronized Server Clock   = {adjusted_server.strftime(format)}")
    print(f"Synchronized Client1 Clock  = {adjusted_client1.strftime(format)}")
    print(f"Synchronized Client2 Clock  = {adjusted_client2.strftime(format)}")

# Input times
server_time = input("Enter Server Time (MM:SS): ")
client1_time = input("Enter Client 1 Time (MM:SS): ")
client2_time = input("Enter Client 2 Time (MM:SS): ")

# Run Berkeley Algorithm
berkeley_algorithm(server_time, client1_time, client2_time)
