"""
Mock responses for API endpoints to use during development.
"""

MOCK_RESPONSES = {
    "expand-idea": {
        "default": """Here's an expanded version of your idea with more details and suggestions:

1. Core Concept: Your initial idea has potential but could benefit from clearer definition.
2. Implementation Strategy: Consider starting with a minimal viable product that demonstrates the core value.
3. Target Audience: Think about who would benefit most from this idea and how to reach them.
4. Differentiators: What makes your idea unique compared to existing solutions?
5. Next Steps: I recommend creating a simple prototype to test the basic functionality.

Would you like me to elaborate on any specific aspect of this idea?"""
    }
}

def get_mock_response(endpoint: str, content: str = None) -> str:
    """
    Return a mock response for the given endpoint and content.
    
    Args:
        endpoint: The API endpoint being called
        content: The content of the request (if applicable)
        
    Returns:
        A string response simulating what the real API would return
    """
    if endpoint not in MOCK_RESPONSES:
        return "Mock response not available for this endpoint"
    
    responses = MOCK_RESPONSES[endpoint]
    
    # For now just return the default response, but could be expanded
    # to provide different responses based on the content
    return responses.get("default")
