# Herói do jogador
heroi = {
    "nome":   "Aran",
    "vida":   100,
    "ataque": 20,
    "defesa": 5,
    "pocoes": 2
}
 
# Lista de monstros do dungeon
monstros = [
    {"nome": "Goblin",    "vida": 30, "ataque": 8,  "ouro": 10},
    {"nome": "Esqueleto", "vida": 50, "ataque": 12, "ouro": 25},
    {"nome": "Dragão",    "vida": 80, "ataque": 20, "ouro": 50},
]
 
ouro_total = 0
 
# Percorrer cada monstro
for monstro in monstros:
    # loop de turnos dentro de cada batalha
    while monstro["vida"] > 0 and heroi["vida"] > 0:
        # ... (implemente aqui a lógica da batalha)
        pass
    