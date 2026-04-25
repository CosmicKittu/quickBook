import sys
import os
import re
import markdown

def parse_frontmatter(content):
    frontmatter = {}
    md_content = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            meta_raw = parts[1].strip()
            md_content = parts[2].strip()
            for line in meta_raw.split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    frontmatter[key.strip().lower()] = val.strip()
    return frontmatter, md_content

def build_guide(md_file_path, template_path, output_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    meta, md_text = parse_frontmatter(content)
    
    # Defaults
    title = meta.get('title', 'DSA Guide')
    logo = meta.get('logo', 'Guide')
    sidebar_title = meta.get('sidebartitle', 'Reference Guide')
    sidebar_sub = meta.get('sidebarsub', 'DSA Reference')
    hero_title = meta.get('herotitle', 'DSA Guide')
    hero_desc = meta.get('herodesc', '')
    
    tags_html = ''
    if 'tags' in meta:
        tags = [t.strip() for t in meta['tags'].split(',')]
        for i, tag in enumerate(tags):
            if i == 0:
                tags_html += f'<span class="hero-tag tag-blue" style="color: var(--amber); border-color: rgba(245,166,35,0.3); background: rgba(245,166,35,0.08);">{tag}</span>\n'
            else:
                tags_html += f'<span class="hero-tag tag-blue">{tag}</span>\n'
                
    hero_html = f"""<div class="hero" id="intro">
  <div class="hero-eyebrow">Quick Reference</div>
  <h1>{hero_title}</h1>
  <p>{hero_desc}</p>
  <div class="hero-tags">
    {tags_html}
  </div>
</div>"""

    # Process sections: ## Badge | Title
    # We will split the markdown by "## "
    sections = []
    sidebar_links = []
    
    parts = re.split(r'^##\s+', md_text, flags=re.MULTILINE)
    
    # parts[0] might be intro text (if any), which we can process as HTML
    main_content_html = ""
    if parts[0].strip():
        main_content_html += markdown.markdown(parts[0], extensions=['fenced_code', 'tables']) + "\n"
        
    for i, part in enumerate(parts[1:]):
        lines = part.split('\n', 1)
        header = lines[0].strip()
        body = lines[1] if len(lines) > 1 else ""
        
        badge = ""
        sec_title = header
        if '|' in header:
            badge, sec_title = [x.strip() for x in header.split('|', 1)]
            
        sec_id = re.sub(r'[^a-z0-9]+', '-', sec_title.lower()).strip('-')
        
        # Sidebar link
        active = 'active' if i == 0 else ''
        sidebar_links.append(f'<a class="nav-link {active}" onclick="navTo(\'{sec_id}\')"><span class="nav-dot"></span>{sec_title}</a>')
        
        # Parse body to HTML
        body_html = markdown.markdown(body, extensions=['fenced_code', 'tables'])
        
        # Build Section HTML
        badge_html = f'<div class="section-badge">{badge}</div>' if badge else ''
        section_html = f"""<section class="section" id="{sec_id}">
  {badge_html}
  <h2 class="section-title">{sec_title}</h2>
  {body_html}
</section>
<hr class="divider">
"""
        main_content_html += section_html

    sidebar_links_html = '<div class="nav-section-label">Containers</div>\n' + "\n    ".join(sidebar_links)

    # Read Template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
        
    # Inject
    output = template.replace('{{ TITLE }}', title)
    output = output.replace('{{ LOGO_TEXT }}', logo)
    output = output.replace('{{ SIDEBAR_TITLE }}', sidebar_title)
    output = output.replace('{{ SIDEBAR_SUBTITLE }}', sidebar_sub)
    output = output.replace('{{ SIDEBAR_LINKS }}', sidebar_links_html)
    output = output.replace('{{ HERO }}', hero_html)
    output = output.replace('{{ CONTENT }}', main_content_html)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
        
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python build_guide.py <input.md> <output.html>")
        sys.exit(1)
        
    md_file = sys.argv[1]
    out_file = sys.argv[2]
    template_file = os.path.join(os.path.dirname(__file__), '..', 'templates', 'guide_template.html')
    
    build_guide(md_file, template_file, out_file)
