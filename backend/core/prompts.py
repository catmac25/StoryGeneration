# STANDARD_STORY_PROMPT = """
# Write a short, engaging story of about 100 words.  

# The story should follow this structure:
# 1. A brief introduction of the main character.  
# 2. A simple setting (time or place).  
# 3. A small challenge, problem, or event.  
# 4. How the character reacts to it.  
# 5. A short resolution with a satisfying or surprising ending.  

# Keep the language simple, descriptive, and imaginative.  
# The tone should be friendly and creative, suitable for readers of all ages.  
# Avoid unnecessary details; focus on keeping the story concise and fun.  

# Return the output strictly in the following JSON format:

# {
#   "title": "A short creative title for the story",
#   "story": "The full story as a single paragraph, around 100 words"
# }
# """
STANDARD_STORY_PROMPT = """
Write a short, engaging story of about 100 words based on the user input.  

The story should follow this structure:
1. A brief introduction of the main character.  
2. A simple setting (time or place).  
3. A small challenge, problem, or event.  
4. How the character reacts to it.  
5. A short resolution with a satisfying or surprising ending.  

Keep the language simple, descriptive, and imaginative.  
The tone should be friendly and creative, suitable for readers of all ages.  
Avoid unnecessary details; focus on keeping the story concise and fun.  

return the output as a string, with the story only
Do NOT return JSON, bullet points, titles, or any code blocks.
Do not include any extra text, explanation, bullet points, or escape characters.  

"""

