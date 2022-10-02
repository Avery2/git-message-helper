# git-message-helper

Takes the output from `git log --name-only --oneline` (list of commits) and organizes the output by file. Then it styles the output for GitHub, optionally leveraging [`<details>` `<summary>`](https://gist.github.com/scmx/eca72d44afee0113ceb0349dd54a84a2) for expandable content. Works best with [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). It's like a bad [gitlens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).

## How to run

Command to take the last `n=10` commits:

```
git log --name-only --oneline -n 10 | python3 organize.py
```

For me, in other directories: 

```
git log --name-only --oneline -n 10 | python3 /Users/avery.chan/Desktop/organize_pr/organize.py
```

## Example

### Command: 
```
git log --name-only --oneline -n 24 | python3 /Users/avery.chan/Desktop/organize_pr/organize.py
```

### Console output: 
```
<details><summary><code>README.md</code> with <code>12</code> commits</summary>

- a03beaf Update README.md
- cd211b5 docs: update README
- 8465c43 Update README.md
- 665047e Update README.md
- 95797eb Update README.md
- 98b5031 Update README.md
- 394f360 Update README.md
- 851a015 Update README.md
- 28c1fab Update README.md
- cc94819 Update README.md
- 2dd0560 docs: Update README.md
- de3b482 docs: Create README.md

</details>
<details><summary><code>organize.py</code> with <code>10</code> commits</summary>

- 0bb4618 feat: take input from stdin instead of from a file
- 56c4f5e feat: show number of changes and sort
- bb9af5e docs: update comments
- 6c52f66 style: update prints
- f126fd8 fix: work with commit hashes of smaller sizes
- 001f363 feat: strip AMP messages
- 89272ad feat: add code styling
- da30be6 feat: add detail and file shortening options
- 5da75f5 style: refactor into function
- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>.gitignore</code> with <code>1</code> commits</summary>

- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>organize.ipynb</code> with <code>1</code> commits</summary>

- 1ce8a08 initial commit 🚀

</details>
```

### Output in GitHub:
<details><summary><code>README.md</code> with <code>12</code> commits</summary>

- a03beaf Update README.md
- cd211b5 docs: update README
- 8465c43 Update README.md
- 665047e Update README.md
- 95797eb Update README.md
- 98b5031 Update README.md
- 394f360 Update README.md
- 851a015 Update README.md
- 28c1fab Update README.md
- cc94819 Update README.md
- 2dd0560 docs: Update README.md
- de3b482 docs: Create README.md

</details>
<details><summary><code>organize.py</code> with <code>10</code> commits</summary>

- 0bb4618 feat: take input from stdin instead of from a file
- 56c4f5e feat: show number of changes and sort
- bb9af5e docs: update comments
- 6c52f66 style: update prints
- f126fd8 fix: work with commit hashes of smaller sizes
- 001f363 feat: strip AMP messages
- 89272ad feat: add code styling
- da30be6 feat: add detail and file shortening options
- 5da75f5 style: refactor into function
- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>.gitignore</code> with <code>1</code> commits</summary>

- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>organize.ipynb</code> with <code>1</code> commits</summary>

- 1ce8a08 initial commit 🚀

</details>

The commit hashes will be styled in comments: 

<img width="931" alt="image" src="https://user-images.githubusercontent.com/53503018/193481457-3a8dc408-41d7-4c05-8847-72d80e476913.png">

