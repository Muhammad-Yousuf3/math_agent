import math

def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression.
    Safe to use for standard math operations.
    """
    try:
        # We limit the scope of eval for safety, though for a local math agent 
        # full python power is often desired. Here we keep it simple.
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Tool definition for the OpenAI SDK
CALCULATOR_TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluates a mathematical expression using Python's math library. Use this for any precise calculation.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate (e.g., 'math.sqrt(16) * 12', '2 + 2').",
                }
            },
            "required": ["expression"],
        },
    }
}
