# 🚀 Projeto: Monitoramento de Container Python

Este projeto simula a execução de um container em Python, imprimindo periodicamente no terminal o tempo de execução.

---

## 📁 Estrutura do Projeto

- `main.py` — Script principal com a lógica de execução contínua.
- `.github/workflows/` — Workflows de CI/CD com GitHub Actions.
- `README.md` — Este arquivo de documentação.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **GitHub Actions**
- **Flake8** (verificação de estilo)
- **Pylint** e **CodeQL** (análise de qualidade e segurança)
- **CI/CD automatizado** com etapas de _build_ e _deploy_ simulados

---

## ✅ Qualidade do Código

Este repositório conta com validações automáticas para garantir a padronização e boas práticas:

- ✅ Verificação de estilo com **Flake8**
- ✅ Análise de código com **Pylint**
- ✅ Análise de segurança com **CodeQL**
- ✅ Correção automática de espaços em branco e quebras de linha
- ✅ Integração contínua via **GitHub Actions**


---

## 📦 Como Executar

Clone o repositório e rode o script diretamente:

```bash
python main.py
O terminal exibirá mensagens a cada 5 segundos enquanto o script estiver em execução.
Para interromper, basta pressionar Ctrl+C.

No terminal eu usei os comandos no docker: 
- docker build -t meu-container-python . #para criar o container
- docker run -it meu-container-python # para rodar o container

---

📂 CI/CD
A pipeline automatizada inclui os seguintes passos:

Instalação de dependências

Correção de espaços finais e quebras de linha (W292, W293, W391)

Verificações com Flake8, Pylint e CodeQL

Simulação de build e deploy

Upload e download de artefatos (opcional)

---

👨‍🏫 Instruções para o professor

O código principal está em main.py
A pipeline automatizada está em .github/workflows/pipeline.yml
Todas as verificações passam com sucesso (vide status acima)

O projeto segue boas práticas de formatação e automação via CI/CD



