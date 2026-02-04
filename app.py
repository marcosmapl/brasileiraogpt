"""
BrasileirãoGPT - Aplicativo de Chat com Agente de IA
Construído com Streamlit, LangChain e OpenAI
"""
import streamlit as st
from src.agents import create_agent
from src.prompts import prompt_loader
from src.config import settings


# Configuração da página
st.set_page_config(
    page_title="BrasileirãoGPT - Chat com IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


def initialize_session_state():
    """Inicializa as variáveis de estado da sessão"""
    if "agent" not in st.session_state:
        try:
            st.session_state.agent = create_agent()
        except ValueError as e:
            st.error(str(e))
            st.stop()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Adiciona mensagem de boas-vindas
        welcome_msg = prompt_loader.get_welcome_message()
        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome_msg
        })


def display_chat_history():
    """Exibe o histórico de mensagens do chat"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_input(user_input: str):
    """
    Processa a entrada do usuário e obtém resposta do agente
    
    Args:
        user_input: Mensagem do usuário
    """
    # Adiciona mensagem do usuário ao histórico
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Exibe mensagem do usuário
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Obtém resposta do agente
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = st.session_state.agent.chat(user_input)
            st.markdown(response)
    
    # Adiciona resposta ao histórico
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


def sidebar():
    """Cria a barra lateral com configurações e informações"""
    with st.sidebar:
        st.title("⚙️ Configurações")
        
        # Informações do modelo
        st.subheader("Modelo Atual")
        st.info(f"**Modelo:** {settings.OPENAI_MODEL}")
        st.info(f"**Temperatura:** {settings.TEMPERATURE}")
        
        st.divider()
        
        # Botão para limpar histórico
        if st.button("🗑️ Limpar Histórico", use_container_width=True):
            st.session_state.agent.clear_history()
            st.session_state.messages = []
            # Adiciona mensagem de boas-vindas novamente
            welcome_msg = prompt_loader.get_welcome_message()
            st.session_state.messages.append({
                "role": "assistant",
                "content": welcome_msg
            })
            st.rerun()
        
        st.divider()
        
        # Informações sobre ferramentas
        st.subheader("🛠️ Ferramentas Disponíveis")
        tools = st.session_state.agent.tools
        for tool in tools:
            with st.expander(f"**{tool.name}**"):
                st.write(tool.description)
        
        st.divider()
        
        # Informações adicionais
        st.subheader("ℹ️ Sobre")
        st.markdown("""
        **BrasileirãoGPT** é um assistente de IA desenvolvido com:
        - **Streamlit** para interface
        - **LangChain** para orquestração
        - **OpenAI** para o modelo de IA
        
        O agente pode executar diversas tarefas e usar ferramentas para ajudá-lo.
        """)


def main():
    """Função principal do aplicativo"""
    # Inicializa estado da sessão
    initialize_session_state()
    
    # Título principal
    st.title("🤖 BrasileirãoGPT")
    st.caption("Seu assistente de IA inteligente")
    
    # Barra lateral
    sidebar()
    
    # Exibe histórico de mensagens
    display_chat_history()
    
    # Campo de entrada do usuário
    if prompt := st.chat_input("Digite sua mensagem..."):
        handle_user_input(prompt)


if __name__ == "__main__":
    main()
