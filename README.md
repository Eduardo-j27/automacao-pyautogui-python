# 🚀 Automação de Cadastro de Produtos com Python

Este projeto automatiza o processo de login e cadastro de produtos em um sistema web, utilizando dados de um arquivo CSV. Ideal para substituir tarefas manuais repetitivas e reduzir erros humanos.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **Pandas:** Para manipulação e leitura da base de dados.
* **PyAutoGUI:** Para automação de interface gráfica (cliques, digitação e comandos de teclado).
* **Time:** Para gerenciamento de intervalos entre ações.

## 📋 Como funciona
1. O script inicia o navegador (Opera).
2. Acessa a URL do sistema de gerenciamento.
3. Realiza o login automaticamente.
4. Percorre cada linha do arquivo `produtos.csv` e preenche os campos (Código, Marca, Tipo, Categoria, etc.).

## 🚀 Como executar
1. Instale as dependências: `pip install pyautogui pandas`
2. Certifique-se de que o arquivo `produtos.csv` está na mesma pasta.
3. Execute o script: `python automacao.py`
