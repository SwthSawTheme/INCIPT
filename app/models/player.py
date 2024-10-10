import random

class Player(object):

    def __init__(self, obsession_level: int = 0, hacking_skill: int = 1, gathered_data: list = None):
        if gathered_data is None:
            gathered_data = []
        self.obsession_level = obsession_level  # Nível de obsessão inicial
        self.hacking_skill = hacking_skill  # Nível de habilidade de hacking
        self.gathered_data = gathered_data  # Dados coletados, como fotos ou informações pessoais

    def hack_device(self, device_security_level: int):
        """
        Tenta invadir o dispositivo da vítima com base no nível de habilidade de hacking.
        Retorna True se o hack for bem-sucedido, False caso contrário.
        """
        print("Tentando hackear o dispositivo...")
        success_chance = self.hacking_skill / (device_security_level + 1)  # Aumenta a chance de sucesso com mais habilidade
        if random.random() < success_chance:
            print("Hack bem-sucedido! Acesso ao dispositivo garantido.")
            return True
        else:
            print("Falha no hack. O nível de segurança era muito alto.")
            return False

    def extract_photos(self):
        """
        Simula a extração de fotos da vítima.
        As fotos extraídas são adicionadas à lista de dados coletados.
        """
        if self.hack_device(device_security_level=5):  # Supondo que o nível de segurança do dispositivo seja 5
            new_data = "Fotos pessoais da vítima"
            self.gathered_data.append(new_data)
            print(f"Dados coletados: {new_data}")
        else:
            print("Não foi possível extrair fotos, hack falhou.")

    def monitor_activity(self):
        """
        Simula o monitoramento das atividades da vítima, como ler mensagens ou rastrear localização.
        """
        activities = ["Lendo mensagens", "Rastreando localização", "Acessando redes sociais"]
        if self.hack_device(device_security_level=4):  # Supondo que a segurança do dispositivo seja 4
            monitored_activity = random.choice(activities)
            self.gathered_data.append(monitored_activity)
            print(f"Atividade monitorada: {monitored_activity}")
        else:
            print("Falha no monitoramento, hack falhou.")

    def increase_obsession(self):
        """
        Aumenta o nível de obsessão do stalker conforme novas informações são obtidas.
        """
        data_collected = len(self.gathered_data)
        self.obsession_level += data_collected
        print(f"Nível de obsessão aumentado para: {self.obsession_level}")

    def improve_hacking_skill(self):
        """
        Melhora a habilidade de hacking do jogador após hacks bem-sucedidos.
        """
        successful_hacks = random.randint(0, 3)
        self.hacking_skill += successful_hacks
        print(f"Habilidade de hacking aumentada para: {self.hacking_skill}")


