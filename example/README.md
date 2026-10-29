# Example: Hello, World!

This folder has two ways of writing the same tiny Python program:

- [hello.py](hello.py): a regular Python **script**. You run the whole file at once.
- [hello.ipynb](hello.ipynb): a Jupyter **notebook**. You run it one cell at a time and see each result straight away. Notebooks are popular for data work.

We'll use them to get comfortable with VS Code before diving into Python itself.

## Part 1: Run it in VS Code

1. In VS Code, go to **File > Open Folder...** and open the `example` folder.
2. Click `hello.py` in the Explorer on the left to open it.
3. Open the terminal: **Terminal > New Terminal** (or `` Ctrl + ` ``).
4. Run:

   ```bash
   python hello.py
   ```

5. You should see this in the terminal:

   ```
   Hello, world!
   Welcome to the VS Code workshop.
   ```

> Tip: with the Python extension installed, you can also click the ▶ **Run** button in the top-right corner of the editor.

## Part 2: Make a change

1. In `hello.py`, change the text inside the quotes, e.g. `print("Hello, <your name>!")`.
2. Save with `Ctrl + S`. (A white dot on the file's tab means it has unsaved changes.)
3. Run it again with `python hello.py`. Press the **Up arrow** in the terminal to bring back the last command instead of retyping it.

## Part 3: Try the notebook

1. Click `hello.ipynb` in the Explorer to open it.
2. Click **Select Kernel** in the top-right corner, choose **Python Environments**, then pick the Python you installed. (The *kernel* is the Python that runs your cells.)
3. Click the first code cell and press **Shift + Enter**. If VS Code asks to install `ipykernel`, click **Install** and wait for it to finish.
4. The output appears under the cell. Run the next cell the same way.
5. Add your own cell: hover between cells, click **+ Code**, type `print("Hello, <your name>!")`, and run it.

### If running a cell fails: set up an environment

If you see an error like *"Running cells with ... requires the ipykernel package"* and **Install** doesn't fix it, give the project its own **virtual environment**. This is a private copy of Python just for this folder, where you can install packages without affecting anything else.

**The easy way (inside VS Code):**

1. Press `Ctrl + Shift + P` and run **Python: Create Environment**.
2. Choose **Venv**, then pick the Python you installed.
3. Wait for it to finish. A `.venv` folder appears in the Explorer.
4. In the notebook, click the kernel name in the top-right, then **Select Another Kernel... > Python Environments > .venv**.
5. Run a cell. If VS Code asks to install `ipykernel`, click **Install**.

**Or from the terminal** (in the project folder):

```bash
python -m venv .venv
.venv\Scripts\python -m pip install ipykernel
```

Then select the `.venv` kernel as in step 4 above. (On Mac/Linux use `.venv/bin/python` instead.)

> **Script or notebook?** Use a notebook when you're exploring, e.g. loading data and checking it step by step. Use a script when you want to run the whole thing in one go.

## Part 4 (Optional): Version control with Git

Git keeps a history of your changes so you can see what changed, go back if you break something, and share your code on GitHub.

### 4.1 One-time setup

Tell Git who you are (use the same email as your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 4.2 Start tracking the project

Copy the `example` folder somewhere of your own (for example, your Desktop) and open that copy in VS Code. Then, in the terminal:

```bash
git init
git add .
git commit -m "My first Python program"
```

- `git init` creates a new, empty history for this folder.
- `git add .` stages every file, i.e. picks what goes into the next snapshot.
- `git commit` saves the snapshot with a message describing it.

### 4.3 Make a change and see it in VS Code

1. Change one of the messages in `hello.py` again and save.
2. Click the **Source Control** icon on the left (or press `Ctrl + Shift + G`). `hello.py` shows up under **Changes**.
3. Click the file to see a side-by-side diff of what you changed.
4. Type a message in the box at the top (e.g. "Change greeting") and click **Commit**. If VS Code asks whether to stage all changes, click **Yes**.

You can do the same from the terminal:

```bash
git status                       # what has changed?
git diff                         # show the exact changes
git add hello.py
git commit -m "Change greeting"
git log --oneline                # list your commits
```

### 4.4 Push to GitHub

1. On https://github.com, click **New repository**, give it a name (e.g. `my-first-project`), leave it empty (don't add a README), and click **Create repository**.
2. GitHub shows you some commands. Copy the ones under "…or push an existing repository from the command line". They look like this:

   ```bash
   git remote add origin https://github.com/<your-username>/my-first-project.git
   git branch -M main
   git push -u origin main
   ```

3. Run them in the VS Code terminal. The first time, a window will pop up asking you to sign in to GitHub.
4. Refresh the GitHub page to see your code online.

From now on, after each commit you can click **Sync Changes** in VS Code's Source Control panel (or run `git push`) to upload it.

## Challenges

- Add a third `print` line with your favourite food.
- Break it on purpose: delete a closing `"` and run it. Read the error message, then fix it. Notice the red squiggly line VS Code shows you.
- Commit each change with a clear message, then look at your history with `git log --oneline`.
