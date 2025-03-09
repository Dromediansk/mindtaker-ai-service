from app.utils import IdeaAction

MOCK_RESPONSE_BY_ACTION: dict[IdeaAction, str] = {
    IdeaAction.expand: """Here's an expanded version of your idea with more details and suggestions:

        1. Core Concept: Your initial idea has potential but could benefit from clearer definition.
        2. Implementation Strategy: Consider starting with a minimal viable product that demonstrates the core value.
        3. Target Audience: Think about who would benefit most from this idea and how to reach them.
        4. Differentiators: What makes your idea unique compared to existing solutions?
        5. Next Steps: I recommend creating a simple prototype to test the basic functionality.
        Would you like me to elaborate on any specific aspect of this idea?""",
            
    IdeaAction.summarize: """Here's a concise summary of your idea:

        Your concept focuses on [key point] which addresses [problem/opportunity]. 
        The main value proposition is [benefit], targeting [audience].
        The most distinctive aspect is [unique element].

        This idea could be developed further by focusing on [suggestion].
        """,
        }


def get_mock_response(action: IdeaAction) -> str:  
    responses = MOCK_RESPONSE_BY_ACTION

    return responses.get(action, "Unknown action requested")
