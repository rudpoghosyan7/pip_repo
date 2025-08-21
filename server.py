class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.status = "stopped"

    def start(self):
        self.status = "running"
        print(f"Server {self.name} started")

    def stop(self):
        self.status = "stopped"
        print(f"Server {self.name} stopped")

    def status_info(self):
        print(f"Server {self.name} is {self.status}") 

    def restart(self):
        self.stop()
        self.start()
        print(f"Server {self.name} is restarted!")



class DatabaseServer(Server):
    def __init__(self, name, ip, db_type):
        super().__init__(name, ip)
        self.db_type = db_type

    def backup(self):
        print(f"Backing up {self.db_type} database on {self.name}")