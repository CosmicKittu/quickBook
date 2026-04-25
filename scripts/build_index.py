import os
import json
import re

GUIDES_DIR = "guides"
OUTPUT_FILE = "guides.js"

def extract_title(html_content):
    match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Untitled Guide"

def generate_tags(filename, title):
    tags = set()
    text = (filename + " " + title).lower()
    
    # Tag logic based on keywords
    if "cpp" in text or "c++" in text:
        tags.add("cpp")
    if "stl" in text:
        tags.add("stl")
    if "js" in text or "javascript" in text:
        tags.add("js")
    if "dsa" in text or "algorithm" in text:
        tags.add("dsa")
    if "react" in text:
        tags.add("react")
    if "python" in text:
        tags.add("python")
        
    return list(tags)

def main():
    guides = []
    
    if not os.path.exists(GUIDES_DIR):
        print(f"Directory {GUIDES_DIR} not found.")
        return
        
    for filename in os.listdir(GUIDES_DIR):
        if filename.endswith(".html"):
            file_path = os.path.join(GUIDES_DIR, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            title = extract_title(content)
            # Use only filename and title for tag generation to avoid matching CSS class names inside content
            tags = generate_tags(filename, title)
            
            guides.append({
                "title": title,
                "url": f"guides/{filename}",
                "tags": tags
            })
            
    # Sort alphabetically by title
    guides.sort(key=lambda x: x["title"])
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Export as a JavaScript global variable to avoid CORS issues locally
        f.write("window.guidesData = ")
        json.dump(guides, f, indent=2)
        f.write(";")
        
    print(f"Successfully generated {OUTPUT_FILE} with {len(guides)} guides.")

if __name__ == "__main__":
    main()
