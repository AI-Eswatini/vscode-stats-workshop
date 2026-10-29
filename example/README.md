# Example: A Tiny Python Web Server

This folder has one file, [server.py](server.py), a small web server that uses only Python's standard library. You don't need to install anything extra.

## Part 1: Run it in VS Code

1. In VS Code, go to **File > Open Folder...** and open the `example` folder.
2. Click `server.py` in the Explorer on the left to open it.
3. Open the terminal: **Terminal > New Terminal** (or `` Ctrl + ` ``).
4. Run:

   ```bash
   python server.py
   ```

5. Open http://localhost:8000 in your browser. You should see a greeting.
6. To stop the server, click in the terminal and press `Ctrl + C`.

> Tip: with the Python extension installed, you can also click the ▶ **Run** button in the top-right corner of the editor.

## Part 2: Make a change

1. In `server.py`, find the line:

   ```python
   MESSAGE = "Hello from my first web server!"
   ```

2. Change the text to anything you like, e.g. `"Hello from <your name>!"`.
3. Save with `Ctrl + S`.
4. Stop the server (`Ctrl + C`), start it again (`python server.py`), and refresh your browser.

## Part 3 (Optional): Version control with Git

Git keeps a history of your changes so you can see what changed, go back if you break something, and share your code on GitHub.

### 3.1 One-time setup

Tell Git who you are (use the same email as your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 3.2 Start tracking the project

Copy the `example` folder somewhere of your own (for example, your Desktop) and open that copy in VS Code. Then, in the terminal:

```bash
git init
git add .
git commit -m "First version of my web server"
```

- `git init` creates a new, empty history for this folder.
- `git add .` stages every file, i.e. picks what goes into the next snapshot.
- `git commit` saves the snapshot with a message describing it.

### 3.3 Make a change and see it in VS Code

1. Change `MESSAGE` in `server.py` again and save.
2. Click the **Source Control** icon on the left (or press `Ctrl + Shift + G`). `server.py` shows up under **Changes**.
3. Click the file to see a side-by-side diff of what you changed.
4. Type a message in the box at the top (e.g. "Change greeting") and click **Commit**. If VS Code asks whether to stage all changes, click **Yes**.

You can do the same from the terminal:

```bash
git status                       # what has changed?
git diff                         # show the exact changes
git add server.py
git commit -m "Change greeting"
git log --oneline                # list your commits
```

### 3.4 Push to GitHub

1. On https://github.com, click **New repository**, give it a name (e.g. `my-web-server`), leave it empty (don't add a README), and click **Create repository**.
2. GitHub shows you some commands. Copy the ones under "…or push an existing repository from the command line". They look like this:

   ```bash
   git remote add origin https://github.com/<your-username>/my-web-server.git
   git branch -M main
   git push -u origin main
   ```

3. Run them in the VS Code terminal. The first time, a window will pop up asking you to sign in to GitHub.
4. Refresh the GitHub page to see your code online.

From now on, after each commit you can click **Sync Changes** in VS Code's Source Control panel (or run `git push`) to upload it.

## Challenges

- Change the page colour by editing the `color` in the `<style>` section.
- Add a paragraph under the heading, e.g. `<p>Welcome to the workshop!</p>`.
- Commit each change with a clear message, then look at your history with `git log --oneline`.
