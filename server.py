class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.status = "stopped"

    def start(self):
        status = "running"
        print(f"Server {self.name} started")

    def stop(self):
        status = "stopped"
        print(f"Server {self.name} stopped")

    def status_info(self):
        print(f"Server {self.name} is {self.status}") 


