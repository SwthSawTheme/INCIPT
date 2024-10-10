from flask import Flask, jsonify,request, render_template
from app.models.devices import Devices
from app.models.player import Player
from app.models.victim import Victim

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

# Simulação do "sistema de arquivos"
fake_filesystem = {
    "~": ["documentos", "fotos", "sistema"],
    "~/documentos": ["segredo.txt", "plano.doc"],
    "~/fotos": ["fotos1.jpg", "fotos2.png"],
    "~/sistema": ["sistema_info.txt"]
}

# Instâncias de exemplo
device = Devices(device_type="Celular", security_level=3, stored_data=["Fotos", "Mensagens"])
player = Player(obsession_level=0, hacking_skill=2, gathered_data=[])

# Página principal
@app.route('/')
def main():
    return render_template('main.html')

# Rota para o terminal
@app.route('/terminal', methods=['POST'])
def terminal():
    data = request.json
    command = data.get("command", "")
    path = data.get("path", "~")

    # Processar os comandos
    if command == "ls":
        if path in fake_filesystem:
            return jsonify({"output": "\n".join(fake_filesystem[path]), "path": path})
        else:
            return jsonify({"output": "Caminho inválido", "path": path})

    elif command.startswith("cd "):
        new_dir = command.split("cd ", 1)[1]
        if new_dir == "..":
            new_path = "/".join(path.split("/")[:-1]) or "~"
        else:
            new_path = f"{path}/{new_dir}".replace("~//", "~/")
        if new_path in fake_filesystem:
            return jsonify({"output": f"Mudando para {new_path}", "path": new_path})
        else:
            return jsonify({"output": "Caminho não encontrado", "path": path})

    elif command == "hack":
        result = player.hack_device(device.security_level)
        return jsonify({"output": "Hack bem-sucedido!" if result else "Falha no hack.", "path": path})

    else:
        return jsonify({"output": f"Comando não reconhecido: {command}", "path": path})

# Rota para retornar o status do jogador
@app.route('/player/status', methods=['GET'])
def player_status():
    return jsonify({
        "obsession_level": player.obsession_level,
        "hacking_skill": player.hacking_skill,
        "gathered_data": player.gathered_data
    })

# Rota para hackear dispositivo
@app.route('/player/hack', methods=['POST'])
def hack_device():
    result = player.hack_device(device.security_level)
    return jsonify({"hack_result": result})

# Rota para extrair fotos
@app.route('/player/extract_photos', methods=['POST'])
def extract_photos():
    player.extract_photos()
    return jsonify({"gathered_data": player.gathered_data})

# Rota para monitorar atividades
@app.route('/player/monitor_activity', methods=['POST'])
def monitor_activity():
    player.monitor_activity()
    return jsonify({"gathered_data": player.gathered_data})

# Rota para aumentar obsessão
@app.route('/player/increase_obsession', methods=['POST'])
def increase_obsession():
    player.increase_obsession()
    return jsonify({"obsession_level": player.obsession_level})

# Rota para melhorar habilidade de hacking
@app.route('/player/improve_hacking', methods=['POST'])
def improve_hacking():
    player.improve_hacking_skill()
    return jsonify({"hacking_skill": player.hacking_skill})

if __name__ == '__main__':
    app.run(debug=True)
