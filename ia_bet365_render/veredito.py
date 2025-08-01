def analisar_jogo(odds_t1, odds_empate, odds_t2, placar, tempo):
    if odds_t1 < odds_t2:
        return f"Time 1 favorito com odds {odds_t1}"
    elif odds_t2 < odds_t1:
        return f"Time 2 favorito com odds {odds_t2}"
    else:
        return "Empate provável"
