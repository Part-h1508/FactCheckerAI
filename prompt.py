# this function builds the prompt we send to the model

def build_prompt(text):

    prompt = f"""
You are a fact checking system for debates.

The input is a conversation between multiple people.

Your job:

1. Identify each speaker (Speaker A, Speaker B, etc.)
2. Extract only factual claims made by each speaker (ignore opinions)
3. For each claim:
   - classify as TRUE / FALSE / PARTIALLY TRUE / UNVERIFIABLE
   - give a short explanation

4. Assign a score to each speaker between 0 and 1:
   - 1 = all claims are correct
   - 0 = all claims are wrong
   - base this on accuracy of their claims

Return ONLY JSON in this format:

{{
  "speakers": [
    {{
      "name": "Speaker A",
      "score": 0.75,
      "claims": [
        {{
          "claim": "...",
          "verdict": "...",
          "explanation": "..."
        }}
      ]
    }}
  ]
}}

Conversation:
{text}
"""

    return prompt