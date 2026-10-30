produto = {
    "codigo": 101, 
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque" : 14
}

print("cadatro do produto:")
print(produto)

print("Nome do produto: ", produto["nome"])
print("Preço do produto: R$", produto["preco"])
print("-"*40)

produto["preco"] = 220.0
produto["estoque"] = produto["estoque"] + 6
produto["categoria"] = "Perifericos"

print(produto)
print(f"novo Estoque Total: {produto['estoque']} Unidades")
print("-"*40)

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}
print("=== USUÁRIO ===")
print("\nChaves do usuário:")
print(usuario.keys())
print("\nValores do usuário:")
print(usuario.values())
print("-"*40)