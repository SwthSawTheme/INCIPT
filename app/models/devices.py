class Devices(object):

    def __init__(self, device_type: str, security_level: int, stored_data: list = None):
        self.device_type = device_type  # Tipo de dispositivo (celular, computador, etc.).
        self.security_level = security_level  # Nível de segurança do dispositivo.
        if stored_data is None:
            stored_data = []
        self.stored_data = stored_data  # Dados armazenados no dispositivo.

    def send_data(self, recipient: str):
        """
        Simula o envio de dados do dispositivo.
        O destinatário pode ser a vítima ou o stalker.
        """
        if self.stored_data:
            data_to_send = self.stored_data[0]  # Envia o primeiro item da lista de dados
            print(f"Enviando '{data_to_send}' para {recipient}.")
            return data_to_send
        else:
            print(f"Não há dados armazenados no {self.device_type} para enviar.")
            return None

    def receive_data(self, new_data: str):
        """
        Simula a recepção de novos dados no dispositivo.
        Os dados recebidos são adicionados à lista `stored_data`.
        """
        self.stored_data.append(new_data)
        print(f"Dados recebidos no {self.device_type}: '{new_data}'")
        return new_data

    def detect_intrusion(self, hacking_skill: int):
        """
        Simula a detecção de uma possível invasão.
        A chance de detectar uma invasão é baseada no nível de segurança do dispositivo e na habilidade de hacking do atacante.
        """
        detection_chance = (self.security_level / (hacking_skill + 1))  # Quanto maior o hacking_skill, menor a chance de detecção
        if detection_chance > 0.5:  # Se a chance de detecção for maior que 50%
            print(f"Intrusão detectada no {self.device_type}!")
            return True
        else:
            print(f"Intrusão não detectada no {self.device_type}.")
            return False

