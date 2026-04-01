#!/usr/bin/env python3
"""
PPT Generator - Creates Steve Jobs style HTML presentations
"""

import json
import os

def generate_ppt_html(content, title="Presentation"):
    """
    Generate HTML presentation from content
    """
    html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            overflow: hidden;
        }}
        .slide {{
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2rem;
            text-align: center;
        }}
        h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
            font-weight: 300;
        }}
        p {{
            font-size: 1.5rem;
            opacity: 0.9;
        }}
    </style>
</head>
<body>
    <div class="slide">
        <h1>{title}</h1>
        <p>{content}</p>
    </div>
</body>
</html>"""
    
    return html_template.format(title=title, content=content)

def save_ppt(content, filename="presentation.html", title="Presentation"):
    """
    Save presentation to file
    """
    html = generate_ppt_html(content, title)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    return filename

if __name__ == "__main__":
    import sys
    content = sys.argv[1] if len(sys.argv) > 1 else "Hello World"
    title = sys.argv[2] if len(sys.argv) > 2 else "My Presentation"
    filename = save_ppt(content, title=title)
    print(f"Presentation saved to: {filename}")