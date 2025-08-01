from flask import Flask, request, jsonify
from veredito import analisar_jogo
import csv

app = Flask(__name__)

@app.route('/analisar', methods=['POST'])
def analisar():
    dados = request.json
    odds_t1 = float(dados.get("odds_time1", 0))
    odds_empate = float(dados.get("odds_empate", 0))
    odds_t2 = float(dados.get("odds_time2", 0))
    placar = dados.get("placar", "0x0")
    tempo = dados.get("tempo", "0")

    resultado = analisar_jogo(odds_t1, odds_empate, odds_t2, placar, tempo)

    with open("historico.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Odds_T1", "Odds_Empate", "Odds_T2", "Placar", "Tempo", "Veredito"])
        writer.writerow([odds_t1, odds_empate, odds_t2, placar, tempo, resultado])

    return jsonify({"veredito": resultado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
