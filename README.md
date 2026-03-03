# 🚀 Automação de Tarefas e Bots com Python

Este projeto automatiza o processo de login e cadastro em massa de produtos em um sistema web. Ele substitui tarefas manuais repetitivas por um processo autônomo, garantindo velocidade e eliminando erros humanos de digitação.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**: Linguagem principal.
* **Pandas**: Para manipulação inteligente de bases de dados.
* **PyAutoGUI**: Para automação de interface gráfica (cliques, digitação e comandos de teclado).
* **Time/OS**: Para gerenciamento de intervalos e leitura de diretórios.

## 📋 Diferenciais do Projeto
* **Versatilidade de Dados**: O script foi desenvolvido para ser flexível. Ele identifica automaticamente e processa dados tanto de arquivos **CSV** quanto de planilhas **Excel (.xlsx)**.
* **Segurança de Execução**: Utiliza pausas estratégicas (`pyautogui.PAUSE`) para garantir que o sistema acompanhe a velocidade dos comandos.
* **Escalabilidade**: Pronto para cadastrar centenas de itens em poucos minutos.

## ⚙️ Como funciona
1. **Abertura**: O bot inicia o navegador (configurado para Opera/Chrome).
2. **Navegação**: Acessa automaticamente a URL do sistema de gerenciamento.
3. **Autenticação**: Realiza o login com as credenciais fornecidas.
4. **Loop de Cadastro**: 
    * Lê a base de dados (CSV ou Excel) via Pandas.
    * Percorre cada linha da tabela.
    * Preenche os campos (Código, Marca, Tipo, Categoria, Preço, etc.) usando comandos de teclado e mouse.
    * Envia os dados e repete o processo até o fim da lista.

## 🚀 Como executar
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Eduardo-j27/automacao-pyautogui-python.git

   
---

# 👍 Dica rápida

Depois de clonar, você pode entrar na pasta e rodar:

```bash
cd automacao-pyautogui-python
pip install pyautogui pandas
python automacao.py
