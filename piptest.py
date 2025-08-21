from server import Server, DatabaseServer

StandartServer = Server("Procution", "122.56.77.10")
DBServer = DatabaseServer("Users", "122.56.77.11", "MsSQL")


StandartServer.start()
DBServer.start()

StandartServer.status_info()
DBServer.status_info()

DBServer.backup()

StandartServer.stop()
DBServer.stop()