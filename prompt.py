# this function builds the prompt we send to the model

def build_prompt(text):

    prompt = f"""
You are a fact checker.

From the text below:
- pick only factual statements (ignore opinions)
- check if they are TRUE / FALSE / PARTIALLY TRUE / UNVERIFIABLE
- give a short explanation

Return ONLY JSON like this:
[
  {{
    "claim": "...",
    "verdict": "...",
    "explanation": "..."
  }}
]

Text:
{text}
"""

    return prompt