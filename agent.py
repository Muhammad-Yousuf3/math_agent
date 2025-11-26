import json
from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL_NAME, SYSTEM_PROMPT
from tools import calculate, CALCULATOR_TOOL_DEFINITION

class PythagorasAgent:
    def __init__(self):
        if not API_KEY:
            raise ValueError("GEMINI_API_KEY not found. Please set it in the Space Settings > Secrets.")

        # Initialize the client to point to Google's Gemini via OpenAI compatibility
        self.client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )
        self.model = MODEL_NAME
        self.tools = [CALCULATOR_TOOL_DEFINITION]
        
        # Available functions mapping
        self.available_functions = {
            "calculate": calculate
        }

    def process_message(self, message_history):
        """
        Processes the message history and returns the final response.
        Handles tool calls automatically.
        """
        # Add system prompt if not present or just rely on the history passed
        # We ensure the system prompt is the first message if possible, 
        # but typically the calling app manages history.
        # Here we create a copy to avoid modifying the original list in place unexpectedly
        messages = list(message_history)
        
        if not messages or messages[0]["role"] != "system":
             messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})

        # First call to the model
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=self.tools,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message

        # Check if the model wants to call a function
        tool_calls = response_message.tool_calls
        
        if tool_calls:
            # Add the model's response (with tool calls) to history
            messages.append(response_message)
            
            # Execute each tool call
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                if function_name in self.available_functions:
                    function_to_call = self.available_functions[function_name]
                    print(f"Calling tool: {function_name} with {function_args}") # Debug log
                    
                    function_response = function_to_call(**function_args)
                    
                    # Add tool response to history
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    })
            
            # Second call to the model to get the final answer based on tool outputs
            second_response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return second_response.choices[0].message.content
            
        else:
            # No tool calls, just return the response
            return response_message.content
