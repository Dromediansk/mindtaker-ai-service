# Mindtaker: AI Service

## Overview

Mindtaker is an AI-powered service that processes and enhances user ideas through various actions. Built with FastAPI and integrated with OpenAI's API, Mindtaker offers a simple interface for transforming raw ideas into more refined outputs based on specific actions.

## API Endpoints

### Public Endpoints

- `GET /`: Health check endpoint that returns a simple greeting message

### Protected Endpoints

- `POST /idea-action`: Processes user ideas with AI assistance
  - Required body parameters:
    - `action`: The type of processing to apply to the idea
    - `idea_text`: The content of the idea to be processed
  - Authentication: JWT token required in Authorization header

## Security Implementation

### Authentication

Mindtaker implements JWT-based authentication using Supabase:

- All protected endpoints require a valid JWT token
- Tokens are verified against Supabase JWT secret
- Token validation checks for expiration and integrity
- User identity is extracted from the JWT claims

### CORS Configuration

The API includes Cross-Origin Resource Sharing (CORS) configuration to control access:

- Currently configured to allow requests from all origins during development
- Supports credential-based requests
- Permits standard HTTP methods (GET, POST, PUT, DELETE)
- Allows all headers in requests

## Development

The service can operate in two modes:

- Using real OpenAI API calls (default)
- Using mock responses for testing (configured via environment variables)

## Environment Configuration

Key environment variables:

- `SUPABASE_JWT_SECRET`: Secret for JWT validation
- `OPENAI_API_KEY`: API key for OpenAI integration
- `USE_MOCK`: Flag to toggle mock response mode
