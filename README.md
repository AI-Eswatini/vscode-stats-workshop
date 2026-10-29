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

Anyone can publish an extension, so stick to well-known publishers and extensions with lots of downloads. Avoid installing random extensions you don't need.

## 3. The example project

The [example/](example/) folder has a simple "Hello, world!" Python program. We'll use it to practise:

- Opening folders and files in VS Code
- Using the built-in terminal
- Running and editing code
- Using a Jupyter notebook
- (Optional) Tracking changes with Git and pushing to GitHub

Follow the steps in [example/README.md](example/README.md).

## 4. Source control (Git in VS Code)

VS Code has Git built in, so you can track changes without typing Git commands. Open it with the **Source Control** icon on the left sidebar (it looks like a branch with three dots), or press `Ctrl + Shift + G`.

### Start tracking a folder

If the folder isn't a Git repo yet, click **Initialize Repository**. If you want it on GitHub straight away, click **Publish to GitHub** instead and sign in when asked.

### What the letters mean

Next to each changed file you'll see a letter:

| Letter | Meaning |
|---|---|
| **U** | Untracked: a new file Git hasn't seen before |
| **M** | Modified: an existing file you've changed |
| **D** | Deleted: a file you've removed |
| **A** | Added: a new file you've staged |

### Save a snapshot (commit)

1. Click a file in the **Changes** list to see exactly what changed (old version on the left, new on the right).
2. Hover over the file and click **+** to **stage** it (choose it for the next snapshot). Click **+** next to **Changes** to stage everything.
3. Type a short message in the box at the top describing what you did, e.g. `Add greeting function`.
4. Click **Commit**.

### Send your work to GitHub

Click **Sync Changes** (or **Publish Branch** the first time). This pushes your commits to GitHub and pulls down any new changes from there.

### Undo a change

Hover over a file under **Changes** and click the curved arrow (**Discard Changes**) to put it back the way it was at the last commit. Be careful: this can't be undone.

## 5. Timeline

The **Timeline** shows the history of the file you have open. Find it at the bottom of the **Explorer** panel (`Ctrl + Shift + E`); if you can't see it, right-click the Explorer header and tick **Timeline**.

It lists two kinds of entries:

- **Git commits** that changed this file, with their message and author.
- **Local history**: VS Code saves a copy every time you save the file, even if you're not using Git.

Click any entry to compare that version with the current one. To go back to an old version, right-click a local history entry and choose **Restore Contents**. This is a lifesaver if you accidentally delete code.

## 6. Configurations and nice-to-haves

### Turn on Auto Save

By default VS Code only saves when you press `Ctrl + S`, and unsaved files show a dot (●) on their tab. To save automatically, click **File > Auto Save**.

To fine-tune it, open Settings (`Ctrl + ,`), search for **auto save**, and pick:

- `afterDelay`: saves a moment after you stop typing (the default when you turn it on)
- `onFocusChange`: saves when you click into another file or panel
- `onWindowChange`: saves when you switch to another app

### Find files fast with `Ctrl + P`

Press `Ctrl + P` and start typing part of a file name, e.g. `hello`. Press `Enter` to open it. This is much quicker than clicking through folders.

You can also type a symbol at the start of the `Ctrl + P` box:

| Type | What it does |
|---|---|
| `>` | Run a command (same as `Ctrl + Shift + P`, the **Command Palette**) |
| `:` | Go to a line number, e.g. `:25` |
| `@` | Jump to a function or class in the current file |

If you only remember one shortcut, make it `Ctrl + Shift + P`: you can type what you want to do (e.g. "change theme", "toggle word wrap") and VS Code will find it.

### Search

- `Ctrl + F`: find text in the current file. `Ctrl + H` finds and replaces.
- `Ctrl + Shift + F`: search across **every file** in the folder. Click a result to jump to it. Use the arrow on the left of the search box to replace across all files.

### Other handy settings

| What | How |
|---|---|
| Format code automatically when saving | Settings (`Ctrl + ,`) > search **format on save** > tick it |
| Wrap long lines so you don't scroll sideways | `Alt + Z` |
| Make the text bigger or smaller | `Ctrl + =` / `Ctrl + -` |
| Change the colour theme | `Ctrl + K` then `Ctrl + T` |
| Show/hide the sidebar | `Ctrl + B` |
| Show/hide the terminal | `` Ctrl + ` `` |
| Comment/uncomment a line | `Ctrl + /` |
| Move a line up or down | `Alt + ↑` / `Alt + ↓` |
| Edit several places at once | Hold `Alt` and click where you want extra cursors |

> **Mac users:** swap `Ctrl` for `Cmd` and `Alt` for `Option` in the shortcuts above.

## Need help?

Feel free to send a WhatsApp message only to (+26878170309).
