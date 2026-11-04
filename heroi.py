heroi = [
 ("superman", 500),
 ("batman", 1000),
 ("homem_aranha", 6000),
 ("thor", 9500),
 ("hulk", 7269),
 ("Flash", 9533),
 ("wolverine", 950),
 ("mulher maravilha", 10065)
]

for h in heroi:    
    if h[1] <= 1000:
        nivel = "ferro"
    elif h[1] >= 1001 and h[1] <= 2000:
        nivel = "Bronze"
    elif h[1]  >= 2001 and h[1] <= 5000:
        nivel = "Prata"
    elif h[1]  >= 5001 and h[1] <= 7000:
        nivel = "Ouro"
    elif h[1]  >= 7001 and h[1] <= 8000:
        nivel = "Platina"
    elif h[1]  >= 8001 and h[1] <= 9000:
        nivel = "Ascendente"
    elif h[1] >= 9001 and h[1] <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    print("O Herói de nome", h[0], "está no nível de", nivel)      
        
  
 
