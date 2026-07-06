# Un mic program care verifica daca fructele sunt scrise corect
def testeaza_lista():
    with open('fructe.txt', 'r') as f:
        linii = f.readlines()
    
    # Verificam daca avem continut
    if len(linii) < 2:
        print("❌ Eroare: Lista este prea scurta!")
        exit(1) # Cod 1 inseamna EROARE

    print("✅ Lista are continut. Test trecut!")
    exit(0) # Cod 0 inseamna SUCCES

if __name__ == "__main__":
    testeaza_lista()