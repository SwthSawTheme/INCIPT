class Victim(object):

    def __init__(self, name: str, occupation: str, college: str, trauma_history: str, friends: list):
        
        self.name = name  # Nome da vítima
        self.occupation = occupation  # Emprego da vítima
        self.college = college  # Faculdade onde a vítima estuda
        self.trauma_history = trauma_history  # Histórico de traumas
        self.friends = friends  # Lista de amigos da vítima
        self.current_activity = None  # Armazena a última atividade realizada

    def work(self):
        """
        Simula o trabalho da vítima. A vítima está ocupada em seus empregos.
        """
        jobs = ["Trabalhando como garçonete", "Atendendo no café"]
        self.current_activity = jobs[0] if self.occupation == "garçonete" else jobs[1]
        print(f"{self.name} está {self.current_activity}.")
        return self.current_activity

    def study(self):
        """
        Simula a vítima estudando para a faculdade de medicina.
        """
        self.current_activity = f"Estudando para as aulas de medicina na {self.college}"
        print(f"{self.name} está {self.current_activity}.")
        return self.current_activity

    def contact_friend(self):
        """
        Simula o contato da vítima com sua amiga.
        A vítima pode entrar em contato com um amigo para conversar ou pedir ajuda.
        """
        if self.friends:
            friend_contacted = self.friends[0]  # Assume que ela vai contatar o primeiro amigo da lista
            self.current_activity = f"Conversando com a amiga {friend_contacted}"
            print(f"{self.name} está {self.current_activity}.")
            return friend_contacted
        else:
            print(f"{self.name} não tem amigos disponíveis para contatar.")
            return None

    def perform_daily_routine(self):
        """
        Simula a rotina diária da vítima. Pode incluir trabalho, estudo e contato com amigos.
        """
        routine = []
        routine.append(self.work())  # Ela trabalha
        routine.append(self.study())  # Ela estuda
        routine.append(self.contact_friend())  # Ela entra em contato com amigos
        return routine
