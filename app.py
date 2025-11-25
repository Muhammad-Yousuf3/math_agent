import chainlit as cl
from agent import PythagorasAgent


@cl.on_chat_start
async def start_chat():
    # Initialize the agent
    try:
        agent = PythagorasAgent()
        cl.user_session.set("agent", agent)
        cl.user_session.set("history", []) # Initialize empty history
        print("Math Agent Initialized successfully.")
        
        # Send a welcome message
        await cl.Message(
            content="Hello! I am the **Pythagoras Agent**. 📐\n\nI can help you solve complex math problems, verify calculations, and explain mathematical concepts step-by-step."
        ).send()
        
    except Exception as e:
        await cl.ErrorMessage(content=f"Failed to initialize agent: {e}").send()

@cl.on_message
async def main(message: cl.Message):
    agent = cl.user_session.get("agent")
    history = cl.user_session.get("history")
    
    if not agent:
        await cl.Message(content="Agent not initialized. Please restart the app.").send()
        return

    # Update history with user message
    history.append({"role": "user", "content": message.content})
    
    # Create a placeholder for the response
    msg = cl.Message(content="")
    await msg.send()
    
    # Process with agent (running synchronously for simplicity, wrapped in async in a real app usually)
    # Since our agent uses standard sync OpenAI calls, we run it directly.
    # For better performance in production, async client should be used.
    try:
        response_content = await cl.make_async(agent.process_message)(history)
        
        # Update history with assistant response
        history.append({"role": "assistant", "content": response_content})
        
        # Update the UI
        msg.content = response_content
        await msg.update()
        
    except Exception as e:
        await cl.Message(content=f"An error occurred: {e}").send()
        
    # Save history back to session
    cl.user_session.set("history", history)
