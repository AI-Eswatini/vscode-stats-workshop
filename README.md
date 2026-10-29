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

## 2. Recommended VS Code extensions

Open the Extensions panel (`Ctrl + Shift + X`) and install:

- **Python** (by Microsoft)

When you open this folder in VS Code, it will also suggest these for you (see [.vscode/extensions.json](.vscode/extensions.json)).

## 3. The example project

The [example/](example/) folder has a tiny Python web server. We'll use it to practise:

- Opening folders and files in VS Code
- Using the built-in terminal
- Running and editing code
- (Optional) Tracking changes with Git and pushing to GitHub
- (Optional) Deploying it to the internet with Render

Follow the steps in [example/README.md](example/README.md).

## Need help?

Feel free to send a WhatsApp message only to (+26878170309).
