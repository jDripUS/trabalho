import pandas as pd
import sys
import os

def main():
    """Função principal simples para teste"""
    print("📊 CSV Analyzer - Funcionando!")
    print("Versão do pandas:", pd.__version__)
    
    # Verifica se foi passado um arquivo
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            print(f"Processando arquivo: {file_path}")
            try:
                df = pd.read_csv(file_path)
                print(f"✅ Arquivo carregado: {df.shape[0]} linhas, {df.shape[1]} colunas")
                print("Colunas:", list(df.columns))
            except Exception as e:
                print(f"❌ Erro ao processar: {e}")
        else:
            print(f"❌ Arquivo não encontrado: {file_path}")
    else:
        print("ℹ️  Uso: python -m csv_analyzer <arquivo.csv>")
        print("ℹ️  Exemplo: python -m csv_analyzer data/example.csv")

if __name__ == "__main__":
    main()
