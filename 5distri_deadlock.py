class Resource:
    def __init__(self, name):
        self.name = name
        self.holder = None

class Process:
    def __init__(self, name):
        self.name = name

    def request_resource(self, resource):
        if resource.holder is None:
            resource.holder = self
            print(f"{self.name} acquired {resource.name}.")
        else:
            print(f"{self.name} is waiting for {resource.name} held by {resource.holder.name}.")

def detect_deadlock(processes):
    # Simulate a simple deadlock detection
    if processes[0].waiting_for == processes[1] and processes[1].waiting_for == processes[0]:
        print("Deadlock detected!")
    else:
        print("No deadlock detected.")

def main():
    r1, r2 = Resource("R1"), Resource("R2")
    p1, p2 = Process("P1"), Process("P2")
    
    # Simulate resource allocation and waiting
    p1.request_resource(r1)  # P1 acquires R1
    p2.request_resource(r2)  # P2 acquires R2
    p1.waiting_for = p2      # P1 waits for P2's resource
    p2.waiting_for = p1      # P2 waits for P1's resource

    detect_deadlock([p1, p2])

if __name__ == "__main__":
    main()
