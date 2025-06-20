from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.dalle import DalleTools

image_agent = Agent(
    model=Ollama(id="mistral:latest"),
    tools=[DalleTools()],
    description="You are an AI agent that can generate images using DALL-E.",
    instructions="When the user asks you to create an image, use the `create_image` tool to create the image.",
    markdown=True,
    show_tool_calls=True,
)

image_agent.print_response("Generate an image of a white siamese cat")

images = image_agent.get_images()
if images and isinstance(images, list):
    for image_response in images:
        image_url = image_response.url
        print(image_url)
