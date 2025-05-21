import os
import dotenv
from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_ollama import ChatOllama

dotenv.load_dotenv()


def connect(
    host: Literal["azure", "openai", "ollama"], model="gpt-4o-mini"
) -> BaseChatModel:
    """Connect to specified host_type LLM

    Args:
        host (Literal["azure", "openai", "ollama"]): host type

    Returns:
        BaseChatModel: AzureChatOpenAI or ChatOpenAI or ChatOllama (local)
    """
    # connect with LLM
    if host == "azure":
        print(
            f"[INFO]: Using {host}/{os.getenv('AZURE_OPENAI_LLM_DEPLOYMENT_ID')} model..."
        )
        llm = AzureChatOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.7,
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_LLM_DEPLOYMENT_ID"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )
    elif host == "openai":
        print(f"[INFO]: Using {host}/{model} model...")
        llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.7,
            model=model,
        )
    elif host == "ollama":
        print(f"[INFO]: Using {host}/{model} model...")
        llm = ChatOllama(
            temperature=0.7,
            model=model,
        )
    else:
        llm = None
    return llm


def make_prompt_template(
    system_prompt: str = "", user_prompt: str = ""
) -> ChatPromptTemplate:
    """prepare ChatPromptTemplate from strings

    Args:
        system_prompt (str, optional): system/persona message. Defaults to "".
        user_prompts (str, optional): user supplied message. Defaults to "".

    Returns:
        ChatPromptTemplate: the prompt template
    """
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", user_prompt),
        ]
    )
    return prompt_template
