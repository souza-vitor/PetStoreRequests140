# PetStoreRequests140

Este projeto consiste em uma suíte de testes automatizados para a API PetStore, utilizando Python. Foram criados testes para os endpoints de pets, usuários e pedidos, organizados em arquivos separados na pasta `__tests__`. Além disso, o projeto utiliza fixtures em formato CSV e JSON para facilitar a criação e remoção de dados durante os testes.

## Estrutura do Projeto
- `__tests__/`: Contém os testes automatizados para cada recurso da API.
- `fixtures/`: Armazena dados de teste em arquivos CSV e JSON.
- `utils/`: Funções utilitárias para auxiliar nos testes.

## Ferramentas Utilizadas
- **Python 3.12**
- **pytest**: Framework de testes utilizado para executar os testes automatizados.
- **requests**: Biblioteca para realizar requisições HTTP à API.

## Como rodar localmente

1. **Clone o repositório:**
   ```powershell
   git clone https://github.com/souza-vitor/PetStoreRequests140.git
   cd PetStoreRequests140
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Instale as dependências:**
   ```powershell
   pip install pytest requests
   ```

4. **Execute os testes:**
   ```powershell
   pytest
   ```

Os resultados dos testes serão exibidos no terminal.