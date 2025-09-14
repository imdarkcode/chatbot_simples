# Projeto Simples de Chatbot com IA

Este é um projeto de backend em Python que demonstra como construir um chatbot simples. Ele utiliza a poderosa biblioteca LangChain para orquestrar o fluxo de conversação e a API GroqCloud para acessar a LLM do Llama, oferecendo respostas rápidas e eficientes.

### Instalação e execução

Siga os passos abaixo para clonar o projeto e executá-lo em sua máquina local.

**1. Clonar o repositório**

Abra o seu terminal ou prompt de comando e execute.

```Bash
git clone https://github.com/imdarkcode/chatbot_langchain
```

**2. Configurar o ambiente**

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```Bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
.venv\Scripts\activate
```

**3. Baixar bibliotecas**

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`.

```Bash
pip install -r requirements.txt
```

**4. Configurar a Chave da API do Groq**

- Acesse o [GroqCloud](https://console.groq.com/home) e crie sua chave de API.
- Na raiz do projeto, crie um arquivo chamado `.env`.
- Adicione sua chave no arquivo.

```Python
GROQ_API_KEY = "SUA_CHAVE_AQUI"
```

**5. Execute o programa**

Com todas as configurações prontas, execute o script principal.

```Bash
python main.py
```

### Tecnologias utilizadas

- **Python:** Linguagem de programação.
- **LangChain:** Framework para desenvolvimento de aplicações com LLMs.
- **GroqCloud:** Plataforma que fornece LLMs de alto desempenho.
- **Llama:** Modelo de linguagem (LLM).