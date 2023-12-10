import re

def detect_xss(input_text):
    xss_pattern = re.compile(r'<script[\s\S]*?>|<\/script[\s\S]*?>', re.IGNORECASE)

    if xss_pattern.search(input_text):
        print(f'Potential XSS attack detected: {input_text}')
    else:
        print("No Potential XSS attack detected")
     
#Example for XSS attack
user_input = '<p><script>alert("Hello, XSS!");</script></p>'
detect_xss(user_input)
