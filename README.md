# 📚 The Guide Vault

A curated, beautifully styled static library for developer references, algorithms, and technical tutorials.

🔗 **Live Site**: [https://devnode.pw/](https://devnode.pw/)

## ✨ Features
- **Premium Interface**: Dark mode, glassmorphism, and responsive layouts.
- **Instant Search**: Filter guides instantly by keyword or auto-generated tags.
- **Zero-Config Authoring**: Built on GitHub Pages with an automated indexing workflow.
- **Markdown-to-HTML Generator**: Write guides in plain Markdown — compile to styled HTML with one command.

## 🚀 How to Add a New Guide
This repository is designed for "Vibe Coding" content generation. You do not need to update any JSON files or the home page manually.

1. Write your new guide as a `.md` file. (Refer to the [`GUIDE_AUTHORING_REFERENCE.md`](./GUIDE_AUTHORING_REFERENCE.md) for layout rules, colors, and structure).
2. Compile it: `python scripts/build_guide.py guides/my-guide.md guides/my-guide.html`
3. Rebuild the index: `python scripts/build_index.py`
4. Commit and push to `main`.

That's it! A GitHub Action will automatically:
- Run `scripts/build_index.py`
- Parse the title and auto-generate tags (like `linux`, `docker`, `js`, `cpp`) based on the content.
- Update the `guides.js` index.
- Deploy the new guide to the live site.

## 🛠️ Local Development
If you want to preview the site or test your tags locally:
1. Run `python scripts/build_index.py` to generate the `guides.js` file manually.
2. Open `index.html` in your browser. (Because we use a JS file instead of JSON, you can simply double-click the file to view it without CORS errors!).
