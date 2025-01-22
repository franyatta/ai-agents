from phi.agent import Agent
from phi.model.groq import Groq

# Set your API key directly
api_key = "your_api_key_here"

# Initialize the Groq model with the API key
groq_model = Groq(id="llama-3.3-70b-versatile", api_key=api_key)

# Create an agent
agent = Agent(model=groq_model)

# Use the agent
agent.print_response("How many API calls can I make to Groq cloud?")
