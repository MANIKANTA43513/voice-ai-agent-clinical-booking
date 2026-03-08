import json
import time

from agent.agent import agent_reasoning
from agent.tools import execute_tool
from services.language_detection import detect_language


def process_text(user_text):

    start_time = time.time()

    # STEP 1 — Detect language
    language = detect_language(user_text)

    # STEP 2 — Agent reasoning
    agent_output = agent_reasoning(user_text)

    # If agent_output is string convert to dict
    if isinstance(agent_output, str):
        try:
            agent_output = json.loads(agent_output)
        except:
            agent_output = {"intent": "unknown"}

    # STEP 3 — Tool execution
    tool_result = execute_tool(agent_output)

    # Latency calculation
    latency = (time.time() - start_time) * 1000

    response = {
        "language": language,
        "agent_output": agent_output,
        "tool_result": tool_result,

        # reasoning trace for evaluation
        "reasoning_trace": {
            "step1": "language_detection",
            "step2": "agent_reasoning",
            "step3": "tool_execution"
        },

        "latency_ms": round(latency, 2)
    }

    return response
    