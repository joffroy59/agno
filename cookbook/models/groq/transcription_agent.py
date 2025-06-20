# groq transcription agent

import asyncio
import os
from pathlib import Path

from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.ollama import Ollama
from agno.tools.models.groq import GroqTools

url = "https://agno-public.s3.amazonaws.com/demo_data/sample_conversation.wav"

agent = Agent(
    name="Groq Transcription Agent",
    model=Ollama(id="mistral:latest"),
    tools=[GroqTools(exclude_tools=["generate_speech"])],
    debug_mode=True,
)

agent.print_response(f"Please transcribe the audio file located at '{url}' to English")
