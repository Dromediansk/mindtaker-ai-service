"""
Mock responses for API endpoints to use during development.
"""

MOCK_RESPONSES = {
    "idea-action": {
        "expand": """Here's an expanded version of your idea with more details and suggestions:

1. Core Concept: Your initial idea has potential but could benefit from clearer definition.
2. Implementation Strategy: Consider starting with a minimal viable product that demonstrates the core value.
3. Target Audience: Think about who would benefit most from this idea and how to reach them.
4. Differentiators: What makes your idea unique compared to existing solutions?
5. Next Steps: I recommend creating a simple prototype to test the basic functionality.

Would you like me to elaborate on any specific aspect of this idea?""",
        
        "summarize": """Here's a concise summary of your idea:

Your concept focuses on [key point] which addresses [problem/opportunity]. 
The main value proposition is [benefit], targeting [audience].
The most distinctive aspect is [unique element].

This idea could be developed further by focusing on [suggestion].
""",

        "improve": """Here are suggestions to improve your idea:

1. Strengthen the core value proposition by [specific suggestion]
2. Consider addressing [potential issue or gap]
3. Differentiate from similar solutions by [unique approach]
4. Enhance scalability by [growth strategy]
5. Test assumptions with [validation method]

The most promising aspect to develop further is [key opportunity].
"""
    }
}

def get_mock_response(action: str, content: str = None) -> str:
    """
    Return a mock response for the given action and content.
    
    Args:
        action: The action to perform (expand, summarize, improve)
        content: The content of the request (if applicable)
        
    Returns:
        A string response simulating what the real API would return
    """
    if "idea-action" not in MOCK_RESPONSES:
        return "Mock response not available for this endpoint"
    
    responses = MOCK_RESPONSES["idea-action"]
    
    # Return the response based on the requested action
    return responses.get(action, "Unknown action requested")
