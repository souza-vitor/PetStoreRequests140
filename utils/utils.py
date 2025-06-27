import csv

def ler_csv(arquivo_csv):
    dados_csv = []

    try:
        with open(arquivo_csv, newline='') as massa:
            tabela = csv.reader(massa, delimiter=',')

            next(tabela) # pula para pular a linha de cabeçalho

            for linha in tabela:
                dados_csv.append(linha)
        
        return dados_csv
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_csv}")
    except Exception as fail:
        print(f"Algo deu errado: {fail}")