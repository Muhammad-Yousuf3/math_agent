# 🤖 Pythagoras Agent: Your Ultimate Math Solver

Welcome to the Pythagoras Agent, a sophisticated AI designed to tackle your math problems with precision and clarity! Built with the OpenAI Agent SDK (compatible with Gemini) and Chainlit, this agent is engineered to provide step-by-step solutions and verify calculations using powerful tools.

## ✨ Features

-   **Intelligent Problem Solving**: Breaks down complex math problems into manageable steps.
-   **Accurate Calculations**: Leverages a Python-based calculator tool for verifiable results.
-   **Interactive Interface**: A user-friendly chat interface powered by Chainlit.



## 💡 How it Works

The Pythagoras Agent uses the following components:

-   **Backend**: `openai` library configured to interact with the Gemini API (via an OpenAI-compatible endpoint).
-   **Tools**: A custom `calculate` function in `tools.py` for executing mathematical expressions.
-   **Frontend**: Chainlit provides the interactive chat interface.

The agent intelligently decides when to use its internal reasoning and when to invoke the `calculate` tool for precise computations.

---

### Example Questions

-   "What is the square root of 144 multiplied by 5?"
-   "Solve for x: 2x + 5 = 15"
-   "Calculate the area of a circle with radius 7. Use π as 3.14159."
-   "What is (123 + 456) * (789 - 123)?"