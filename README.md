# 📋 Sistema de Gerenciamento de Tarefas

Um sistema simples e eficiente para gerenciar suas tarefas diárias, desenvolvido em Python.

## 🚀 Funcionalidades

- ✅ Criar, visualizar e gerenciar tarefas
- 📊 Classificação por prioridade (Alta, Média, Baixa)
- 📅 Definição de datas de vencimento
- 📈 Acompanhamento do status de conclusão
- 📁 Persistência de dados em formato JSON
- 📧 Envio automático de relatórios por e-mail

## 📁 Estrutura do Projeto
Sistema-tarefas/
├── README.md # Documentação do projeto
├── .gitignore # Arquivos ignorados pelo Git
├── requirements.txt # Dependências do projeto
├── python.main.py # Arquivo principal de execução
├── Projectpedro.py # Módulo principal do sistema
└── Vendas.xlsx # Base de dados de exemplo

text

## 🛠️ Tecnologias Utilizadas

- **Python 3.14+** - Linguagem de programação
- **JSON** - Formato de persistência de dados
- **pandas** - Manipulação e análise de dados
- **openpyxl** - Leitura de arquivos Excel
- **yagmail** - Envio de e-mails
- **Git** - Controle de versão
- **GitHub** - Hospedagem do código

## 📦 Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/Pedroph185/Sistema-tarefas.git

# Entre na pasta do projeto
cd Sistema-tarefas

# Instale as dependências
pip install -r requirements.txt

# Execute o programa
python python.main.py
📊 Exemplo de Uso
python
# Criando uma nova tarefa
tarefa = Task(
    title="Estudar Python",
    description="Revisar classes e objetos",
    priority="alta",
    due_date="2026-07-20"
)

# Visualizando a tarefa
print(tarefa)
# Saída: ❌ 🔴 Estudar Python
🤝 Contribuição
Sinta-se à vontade para contribuir com o projeto:

Faça um fork do repositório

Crie uma branch para sua feature (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -m 'Adicionando nova feature')

Push para a branch (git push origin feature/nova-feature)

Abra um Pull Request

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

📧 Contato
Pedro Henrique Cavalcanti

GitHub: @Pedroph185

Email: wirelesspedro@gmail.com

⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!
