# Intro to VS Code Workshop

Welcome! This repo has everything you need for the workshop: what to install beforehand, and a small example project we'll use to practise working in VS Code and (optionally) Git.

## 1. Things to install

For each link, open it and select the download for your operating system. Most people use Windows, so these are the steps:

1. **Visual Studio Code** => https://code.visualstudio.com/download
2. **Git** => https://git-scm.com/install/windows (click on where it says 'Click here to download')
3. **Node** => https://nodejs.org/en/download (please click on the green button 'Windows Installer (.msi)')
4. **Python** => https://www.python.org/downloads/ (click the yellow 'Download Python' button). During installation, **tick the box that says "Add python.exe to PATH"** before clicking Install.

Please also create an account on GitHub (https://github.com), if you do not have one already, for project hosting.

> Note: assuming everyone is using Windows. If not, select your operating system on each page and follow those steps.

### Check that everything installed

Open VS Code, then open the terminal with **Terminal > New Terminal** (or `` Ctrl + ` ``) and run:

```bash
code --version
git --version
node --version
python --version
```

Each command should print a version number. If one says "not recognized", close and reopen VS Code (or restart your computer) and try again.

## 2. VS Code extensions

### What is an extension?

On its own, VS Code is a plain text editor. **Extensions** are free add-ons that teach it new skills, like understanding a programming language, running code, or opening new file types. Think of them like apps on your phone: you install only the ones you need.

### How to install one

1. Click the **Extensions** icon on the left sidebar (four small squares), or press `Ctrl + Shift + X`.
2. Type the extension's name in the search box.
3. Check the publisher is **Microsoft** (look for the blue verified tick ✓), then click **Install**.

### What to install for this workshop

| Extension | What it does | Approx. size on disk |
|---|---|---|
| **Python** (Microsoft) | Lets VS Code understand Python: colours your code, spots mistakes with red squiggly lines, suggests completions as you type, and adds the ▶ Run button. It also installs **Pylance**, **Python Debugger** and **Python Environments** automatically. | ~75 MB+ (including helpers) |
| **Jupyter** (Microsoft) | Lets you open and run notebooks (`.ipynb` files), where code runs one cell at a time with the results underneath. It also installs a few small helpers, such as **Jupyter Notebook Renderers** for showing charts and tables. | ~45 MB (including helpers) |

> **Tip:** please install these **before** the workshop. Together they're over 100 MB, which can take a while if everyone downloads them on the same Wi-Fi at once.

When you open this repo's folder in VS Code, a pop-up in the bottom-right corner will suggest these extensions for you. Just click **Install**. (This comes from the [.vscode/extensions.json](.vscode/extensions.json) file.)

### Be careful with extensions

Anyone can publish an extension, so stick to well-known publishers (like Microsoft) and extensions with lots of downloads. Avoid installing random extensions you don't need.

## 3. The example project

The [example/](example/) folder has a simple "Hello, world!" Python program. We'll use it to practise:

- Opening folders and files in VS Code
- Using the built-in terminal
- Running and editing code
- Using a Jupyter notebook
- (Optional) Tracking changes with Git and pushing to GitHub

Follow the steps in [example/README.md](example/README.md).

## Need help?

Feel free to send a WhatsApp message only to (+26878170309).
