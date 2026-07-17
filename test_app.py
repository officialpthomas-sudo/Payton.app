#!/usr/bin/env python3
import os
import sys
from openai import OpenAI

# Test the API key
try:
    api_key = "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"
    
    client = OpenAI(api_key=api_key)
    
    # Test a simple API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello"}
        ],
        max_tokens=10
    )
    
    print("✅ API Key is valid!")
    print(f"Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    sys.exit(1)
