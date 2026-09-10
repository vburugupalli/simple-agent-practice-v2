# -------------------------------------------------------------------
# 1. THE TOOL (ADK Pattern)
# A simple function that performs a specific action.
# -------------------------------------------------------------------
def check_item_stock(item_name: str) -> str:
    inventory = {"laptop": "5 units available", "headset": "Out of stock"}
    return inventory.get(item_name.lower(), "Item not found in database")

# -------------------------------------------------------------------
# 2. THE NODES & STATE (LangGraph Pattern)
# State is just a dictionary that flows step-by-step through functions.
# -------------------------------------------------------------------
def node_1_parse_input(state: dict) -> dict:
    """Node 1: Extract the item name from the user query."""
    query = state["user_query"].lower()
    if "laptop" in query:
        state["detected_item"] = "laptop"
    elif "headset" in query:
        state["detected_item"] = "headset"
    else:
        state["detected_item"] = "unknown"
    return state

def node_2_run_tool(state: dict) -> dict:
    """Node 2: Execute the tool using data from the state."""
    item = state["detected_item"]
    result = check_item_stock(item)
    state["agent_response"] = f"Result for '{item}': {result}"
    return state

# -------------------------------------------------------------------
# 3. THE GRAPH EXECUTION
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Initial State
    state = {"user_query": "Do we have any laptop left in stock?"}
    # Pass State through Node 1 -> Node 2
    state = node_1_parse_input(state)
    state = node_2_run_tool(state)
    # Output final state
    print("--- AGENT OUTPUT ---")
    print(state["agent_response"])