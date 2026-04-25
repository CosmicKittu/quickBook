# Guide Authoring Reference (For AI & Humans)

This document serves as the absolute source of truth for creating new guides in this repository. We use a **Markdown-to-HTML Generator Pipeline** to author guides efficiently. Do not write raw HTML files for new guides; always write in Markdown and compile them.

## 🎨 Design System & Color Schema

All generated guides automatically inherit our exact CSS root variables and fonts to match the deep dark mode aesthetic via `templates/guide_template.html`.

**Core Colors:**
- `--bg: #0d0f14` (Main background)
- `--bg2: #13161e` (Sidebar & secondary bg)
- `--bg3: #1a1e28` (Code block bg)
- `--text: #e8eaf0` (Primary text)
- `--text2: #8b90a8` (Secondary text)
- `--accent: #7c6ef7` (Primary brand color)

**Syntax Colors (Handled by Prism.js automatically):**
- `--green: #3ecf8e` (Strings / Tips)
- `--amber: #f5a623` (Numbers / Warnings)
- `--red: #f06565` (Errors / Danger)
- `--blue: #4da6ff` (Functions / Info)
- `--teal: #2ed8c3` (Types)

## 🏗️ Guide Authoring Workflow

Every new guide must be written as a `.md` file and compiled.

### 1. File Structure & Frontmatter
Start your Markdown file with a configuration block at the very top:

```markdown
---
title: Python DSA Reference
logo: Python Guide
sidebartitle: Python Standard Library
sidebarsub: DSA Reference
herotitle: Python <span>Collections</span> DSA
herodesc: This is a quick reference for Python data structures in DSA.
tags: Python, Interview Ready
---
```

### 2. Sections and Sidebar
To create a section (which automatically generates a sticky sidebar link), use an H2 `##` header. You can optionally include a badge string separated by a pipe `|`:

```markdown
## 01 — PYTHON | List

Lists are the primary array type in Python.
```

### 3. Syntax Highlighting
**DO NOT** use manual inline spans like `<span class="kw">`. Use standard Markdown code blocks with the appropriate language identifier. Our custom Prism.js theme will automatically highlight them perfectly matching the UI:

```python
def hello():
    print("Hello, World!")
```

### 4. Code Comparison (If needed)
If you need a two-column comparison block, use raw HTML inside the Markdown:
```html
<div class="compare">
  <div class="compare-block">
    <div class="compare-header cpp"><span class="dot"></span>C++</div>
    <pre><code class="language-cpp">std::cout &lt;&lt; "Hi";</code></pre>
  </div>
  <div class="compare-block">
    <div class="compare-header js"><span class="dot"></span>JS</div>
    <pre><code class="language-javascript">console.log("Hi");</code></pre>
  </div>
</div>
```

### 5. Callouts
Use raw HTML for callout boxes (warn, info, tip, danger):
```html
<div class="callout tip">
  <div class="callout-icon">💡</div>
  <div class="callout-body">
    <div class="callout-title">Pro Tip</div>
    <div class="callout-text">You can use aliases to make navigating directories faster.</div>
  </div>
</div>
```

## 🛠️ Compiling The Guide

Once the Markdown file is complete, run the generator script from the root of the project:
```bash
python scripts/build_guide.py <input.md> guides/<output>.html
```
*Note: Make sure to output the HTML file to the `guides/` directory so the auto-indexer can find it.*

## 🏷️ Auto-Indexing & Tags
You do NOT need to manually add the guide to the home page. Just ensure:
1. The output `.html` file is saved in the `guides/` folder.
2. Run the auto-indexer script (`python scripts/build_index.py`).
