# 🚀 Projeto: Monitoramento de Container Python

Este projeto simula a execução de um container em Python, imprimindo periodicamente no terminal o tempo de execução.
---
## 📁 Estrutura do Projeto

- **main.py** — Script principal com a lógica de execução contínua.
- **.github/workflows/** — Workflows de CI/CD com GitHub Actions.
- **README.md** — Este arquivo de documentação.
---
## ⚙️ Tecnologias Utilizadas

- Python 3.x
- GitHub Actions
- Flake8 (verificação de estilo)
- Pylint e CodeQL (análise de qualidade e segurança)
- CI/CD automatizado com etapas de build e deploy simulados
- **discord.py** (para integração com o Discord)
- **pytest** (para testes automatizados)
- **capsys** (para capturar a saída do terminal em testes)
---
## ✅ Qualidade do Código

Este repositório conta com validações automáticas para garantir a padronização e boas práticas:

- ✅ Verificação de estilo com Flake8
- ✅ Análise de código com Pylint
- ✅ Análise de segurança com CodeQL
- ✅ Correção automática de espaços em branco e quebras de linha
- ✅ Integração contínua via GitHub Actions
---
## 📦 Como Executar

Clone o repositório e rode o script diretamente:

```bash
python main.py
O terminal exibirá mensagens a cada 5 segundos enquanto o script estiver em execução. Para interromper, basta pressionar Ctrl+C.

🚢 Executando Docker
No terminal, utilize os seguintes comandos para rodar o container:

docker build -t meu-container-python .  # para criar o container
docker run -it meu-container-python     # para rodar o container
```
---

## 🔗 Integração com Discord
O projeto inclui uma integração com o Discord para notificações sobre o status do container. Quando o container for executado, o script envia uma mensagem ao canal do Discord configurado.

---
## 📂 CI/CD
A pipeline automatizada inclui os seguintes passos:

Instalação de dependências

Correção de espaços finais e quebras de linha

Verificações com Flake8, Pylint e CodeQL

Simulação de build e deploy

Upload e download de artefatos (opcional)

---

## 🧪 Testes Unitários
Com capsys os testes unitários são realizados utilizando o framework pytest. Para testar a execução do script, usamos o capsys para capturar a saída do terminal e garantir que o comportamento esperado aconteça.

Exemplo de teste:
Crie um arquivo de teste test_main.py:
```
import pytest
from main import executar_container

def test_execucao_container(capsys):
    executar_container()      
    captured = capsys.readouterr()
    assert "Tempo de execução" in captured.out
```
