class client_class:
    def __init__(self, websocket, name:str = "Unknown"):
        self.name = name
        self.websocket = websocket

    def changename(self, newname: str):
        self.name = newname