
class Devices(object):

    def __init__(self,device_type:str,security_level:int,stored_data:list):
        self.device_type = device_type # Tipo de dispositivo (celular, computador, etc.).
        self.security_level = security_level # Nível de segurança do dispositivo.
        self.stored_data = stored_data #Dados armazenados no dispositivo.

    def send_data(self):
        # Envia dados para a mulher ou para o hacker.
        pass

    def receive_data(self):
        # Recebe novos dados.
        pass

    def detect_intrusion(self):
        # Detecta uma possível invasão.
        pass