# 🤖 BrasileirãoGPT

Aplicativo de chat com Agente de IA construído com **Streamlit**, **LangChain** e **OpenAI API**. O projeto é modularizado para facilitar manutenção e extensibilidade.

## 📋 Características

- 🤖 Agente conversacional inteligente com memória
- 🛠️ Sistema modular de ferramentas (Tools)
- 📝 Prompts configuráveis via arquivos JSON
- 💬 Interface de chat moderna com Streamlit
- 🔧 Configurações via arquivo `.env`
- 📦 Arquitetura modular e extensível

## 🗂️ Estrutura do Projeto

```
brasileiraogpt/
├── app.py                          # Aplicativo principal Streamlit
├── requirements.txt                # Dependências do projeto
├── .env.example                    # Exemplo de configurações
├── .gitignore                      # Arquivos ignorados pelo Git
├── README.md                       # Documentação
└── src/                           # Código fonte modularizado
    ├── __init__.py
    ├── config/                    # Configurações
    │   ├── __init__.py
    │   └── settings.py            # Carregamento de variáveis .env
    ├── prompts/                   # Prompts em JSON
    │   ├── __init__.py
    │   ├── loader.py              # Carregador de prompts
    │   ├── agent_prompts.json     # Prompts do agente
    │   └── tool_prompts.json      # Prompts das ferramentas
    ├── tools/                     # Ferramentas do agente
    │   ├── __init__.py
    │   └── agent_tools.py         # Implementação das tools
    └── agents/                    # Implementação dos agentes
        ├── __init__.py
        └── conversational_agent.py # Agente conversacional
```

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/brasileiraogpt.git
cd brasileiraogpt
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave da OpenAI:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-4o-mini
TEMPERATURE=0.7
MAX_TOKENS=2000
```

## ▶️ Como Usar

Execute o aplicativo Streamlit:

```bash
streamlit run app.py
```

O aplicativo abrirá automaticamente no navegador em `http://localhost:8501`

## 🛠️ Ferramentas Disponíveis

O agente possui as seguintes ferramentas:

1. **Calculadora**: Realiza cálculos matemáticos
2. **Data e Hora**: Informa data e hora atual

### Adicionando Novas Ferramentas

Para adicionar uma nova ferramenta:

1. Edite `src/tools/agent_tools.py`
2. Crie uma função para a ferramenta
3. Crie uma função `create_[nome]_tool()` que retorna um `Tool`
4. Adicione a ferramenta em `get_all_tools()`
5. Adicione a descrição em `src/prompts/tool_prompts.json`

## 📝 Personalizando Prompts

Os prompts são configurados em arquivos JSON no diretório `src/prompts/`:

- **agent_prompts.json**: Prompts do sistema, mensagens de boas-vindas e erro
- **tool_prompts.json**: Descrições das ferramentas

Edite esses arquivos para personalizar o comportamento do agente.

## 🔧 Configurações Avançadas

### Alterando o Modelo

Edite o arquivo `.env`:

```env
OPENAI_MODEL=gpt-4o        # Para GPT-4 Turbo
OPENAI_MODEL=gpt-3.5-turbo # Para GPT-3.5
```

### Ajustando a Temperatura

```env
TEMPERATURE=0.5  # Mais determinístico
TEMPERATURE=1.0  # Mais criativo
```

## 🏗️ Arquitetura

### Módulos

- **config**: Gerencia configurações e variáveis de ambiente
- **prompts**: Carrega e gerencia prompts de arquivos JSON
- **tools**: Implementa ferramentas que o agente pode usar
- **agents**: Implementa o agente conversacional com LangChain

### Fluxo de Dados

```
Usuário → Streamlit → Agent → LLM (OpenAI)
                        ↓
                      Tools
                        ↓
                    Resposta
```

## 📦 Dependências Principais

- **streamlit**: Interface web
- **langchain**: Framework para agentes de IA
- **langchain-openai**: Integração com OpenAI
- **openai**: API da OpenAI
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🐛 Problemas Conhecidos

- Certifique-se de ter uma chave válida da OpenAI
- O histórico da conversa é mantido apenas durante a sessão

## 📞 Suporte

Para problemas ou dúvidas, abra uma [issue](https://github.com/seu-usuario/brasileiraogpt/issues) no GitHub.

---

Desenvolvido com ❤️ usando Streamlit, LangChain e OpenAI
An AI expert focused on Brazil’s national football league (Brasileirão)
