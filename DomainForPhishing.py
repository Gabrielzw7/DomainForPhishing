import whois # Biblioteca para verificação do domínio

# Define o dicionário para substituição. 
# Podem ser adicionados mais caracteres semelhantes.

def generate_variations(domain):
    variations = set()

    visually_similar = {
    'l': ['1', 'i'],
    'i': ['1', 'l'],
    'o': ['0'],
    'j': ['i'],
    'e': ['3'],
    'w': ['vv'],
    'ae': ['æ'],
    's': ['5'],
    'g': ['9'],
    'z': ['2'],
    't': ['7'],
    'b': ['6', '8'],
    'a': ['4'],
    'n': ['m']
}

# Gera os domínios sem alterar os TLDs

    parts = domain.split(".", 1)
    if len(parts) == 2:
        name, extension = parts
        for char in name:
            similar_chars = visually_similar.get(char, [char])
            for similar_char in similar_chars:
                variation = name.replace(char, similar_char)
                variations.add(f"{variation}.{extension}")
    else:
        print("Nome de domínio inválido")

    return list(variations) # Converte o conjunto para uma lista

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return True
        else:
            return False
    except whois.parser.PywhoisError:
        return True

# Entrada do usuário

def main():
    print("\033[32m    ____                                _              ____                   ____     __      _             __      _                  \033[0m")
    print("\033[32m   / __ \  ____    ____ ___   ____ _   (_)   ____     / __/  ____    _____   / __ \   / /_    (_)   _____   / /_    (_)   ____    ____ _\033[0m")
    print("\033[32m  / / / / / __ \  / __ `__ \ / __ `/  / /   / __ \   / /_   / __ \  / ___/  / /_/ /  / __ \  / /   / ___/  / __ \  / /   / __ \  / __ `/\033[0m")
    print("\033[32m / /_/ / / /_/ / / / / / / // /_/ /  / /   / / / /  / __/  / /_/ / / /     / ____/  / / / / / /   (__  )  / / / / / /   / / / / / /_/ / \033[0m")
    print("\033[32m/_____/  \____/ /_/ /_/ /_/ \__,_/  /_/   /_/ /_/  /_/     \____/ /_/     /_/      /_/ /_/ /_/   /____/  /_/ /_/ /_/   /_/ /_/  \__, /  \033[0m")
    print("\033[32m                                                                                                                               /____/   \033[0m")
    print("")
    print("                                                                            \033[1;31mDomain For Phishing v1 - by Gabriel W.\033[0m")
    print("# Insira o domínio completo, ex: dominio.com")
    print("")
    domain = input("Digite o nome de domínio: ")
    print("")

    variations = generate_variations(domain)

    print("Variações geradas:")
    print("")

# Verifica se o domínio está disponível

    for variation in variations:
        availability = "Disponível para compra" if check_domain_availability(variation) else "Indisponível"
        print(f"{variation} - {availability}")

if __name__ == "__main__":
    main()
