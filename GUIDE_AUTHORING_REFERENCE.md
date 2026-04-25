# Guide Authoring Reference (For AI & Humans)

This document serves as the absolute source of truth for creating new guides in this repository. When generating or writing a new guide, follow these rules, layout structures, and color schemas to ensure visual consistency across the library.

## 🎨 Design System & Color Schema

All guides MUST use the exact same CSS root variables and fonts to match the deep dark mode aesthetic.

**Fonts (via Google Fonts):**
- Headings & Body: `'Syne', sans-serif`
- Code & Monospace: `'JetBrains Mono', monospace`

**Core Colors:**
- `--bg: #0d0f14` (Main background)
- `--bg2: #13161e` (Sidebar & secondary bg)
- `--bg3: #1a1e28` (Code block bg)
- `--text: #e8eaf0` (Primary text)
- `--text2: #8b90a8` (Secondary text)
- `--accent: #7c6ef7` (Primary brand color)

**Syntax & Alert Colors:**
- `--green: #3ecf8e` (Success / JS / Tips)
- `--amber: #f5a623` (Warning / C++ / Numbers)
- `--red: #f06565` (Danger / Errors)
- `--blue: #4da6ff` (Info / Functions)
- `--teal: #2ed8c3` (Types)

## 🏗️ Base File Structure
Every new guide must be a single `.html` file placed inside the `guides/` directory.
It MUST contain:
1. **The Global `<style>` block:** Copy the CSS exactly from existing guides (`dsa-js-guide.html` or `stl-cpp-guide.html`). Do not use external stylesheets.
2. **Sidebar Navigation:** A sticky `<nav id="sidebar">` containing `<a class="nav-link" onclick="navTo('section-id')">`.
3. **Hero Header:** A `<div class="hero">` block introducing the guide with a title and description.
4. **Main Sections:** Content divided into `<section class="section" id="section-id">`.

---

## 📖 Guide Type 1: The Code Reference
*Best for: Language overviews, data structures, and syntax references (e.g. C++ STL, JavaScript DSA).*

**Key Components:**
- **Code Compare Blocks**: If comparing two languages (e.g. C++ vs JS), use a grid layout.
  ```html
  <div class="compare">
    <div class="compare-block">
      <div class="compare-header cpp"><span class="dot"></span>C++</div>
      <pre>...</pre>
    </div>
    <div class="compare-block">
      <div class="compare-header js"><span class="dot"></span>JS</div>
      <pre>...</pre>
    </div>
  </div>
  ```
- **Syntax Highlighting**: Use inline spans like `<span class="kw">int</span>`, `<span class="str">"text"</span>`, `<span class="cmt">// comment</span>`.
- **Performance Badges**: Use `.tag-o1`, `.tag-on`, etc. for Big-O notation.

---

## 💻 Guide Type 2: The Command/Tutorial Guide
*Best for: CLI tools, deployment steps, DevOps, and sequential tutorials (e.g. Linux Commands, Docker).*

**Key Components:**
- **Sequential Flow**: Sections should flow logically (e.g., "1. Installation", "2. Basic Commands", "3. Volumes").
- **Terminal Blocks**: Code blocks should clearly represent terminal inputs. 
  ```html
  <pre><code>$ docker run -d -p 80:80 nginx</code></pre>
  ```
- **Tables for Arguments**: Use HTML tables to explain flags and commands clearly.
  ```html
  <table>
    <tr><th>Command</th><th>Description</th></tr>
    <tr><td><code>ls -la</code></td><td>List all files with hidden and details</td></tr>
  </table>
  ```
- **Callout Boxes**: Use callouts heavily to explain gotchas, warnings, or tips.
  ```html
  <div class="callout tip">
    <div class="callout-icon">💡</div>
    <div class="callout-body">
      <div class="callout-title">Pro Tip</div>
      <div class="callout-text">You can use aliases to make navigating directories faster.</div>
    </div>
  </div>
  ```

## 🏷️ Auto-Indexing & Tags
You do NOT need to manually add the guide to the home page. Just ensure:
1. The `<title>` tag inside your HTML `<head>` is descriptive.
2. The file is saved in the `guides/` folder.
3. Relevant keywords (like `docker`, `linux`, `bash`, `react`) are present in the text, as the auto-indexer uses them to generate tags automatically.
