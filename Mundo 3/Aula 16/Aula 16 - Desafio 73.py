Brasileiro = ("Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo",
              "Bragantino", "Fluminense", "Athletico-PR", "Internacional", "Fortaleza",
              "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco",
              "Bahia", "Santos", "Goiás", "Coritiba", "América-MG")

print("***"*20)
print(f"Os times do Brasileirão são : {Brasileiro}")
print("***"*20)
print(f"\nOs 4 primeiros colocados do campeonato Brasileiro são : {Brasileiro[0:4]}")
print(f"\nOs 4 Rebaixados  do campeonato Brasileiro são : {Brasileiro[-4:]}")
print(f"\nTimes em ordem alfábética: {sorted(Brasileiro)}")
print(f"\nO Botafogo está em {Brasileiro.index("Botafogo")+1} colocado")