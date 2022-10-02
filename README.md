# git-message-helper

Takes the output from `git log --name-only --oneline` (list of commits) and organizes the output by file. Then it styles the output for GitHub, optionally leveraging [`<details>` `<summary>`](https://gist.github.com/scmx/eca72d44afee0113ceb0349dd54a84a2) for expandable content. Works best with [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).

This is like a bad [gitlens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).

## Example

Command to take the last `n=10` commits:

```
rm output.txt; rm log.txt; git log --name-only --oneline -n 10 >> log.txt; python3 organize.py >> output.txt
```

For me: 

```
rm output.txt; rm log.txt; git log --name-only --oneline -n 10 >> log.txt; python3 /Users/avery.chan/Desktop/organize_pr/organize.py >> output.txt; cat output.txt; rm log.txt; rm output.txt;
```

`log.txt`:

```
6c52f66 style: update prints
organize.py
f126fd8 fix: work with commit hashes of smaller sizes
organize.py
001f363 feat: strip AMP messages
organize.py
89272ad feat: add code styling
organize.py
da30be6 feat: add detail and file shortening options
organize.py
5da75f5 style: refactor into function
organize.py
1ce8a08 initial commit 🚀
organize.py
```

`output.txt`:

```
<details><summary><code>organize.py</code></summary>

- 6c52f66 style: update prints
- f126fd8 fix: work with commit hashes of smaller sizes
- 001f363 feat: strip AMP messages
- 89272ad feat: add code styling
- da30be6 feat: add detail and file shortening options
- 5da75f5 style: refactor into function
- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>README.md</code></summary>

- de3b482 docs: Create README.md

</details>
<details><summary><code>.gitignore</code></summary>

- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>organize.ipynb</code></summary>

- 1ce8a08 initial commit 🚀

</details>
```

Output in GitHub:

<details><summary><code>organize.py</code></summary>

- 6c52f66 style: update prints
- f126fd8 fix: work with commit hashes of smaller sizes
- 001f363 feat: strip AMP messages
- 89272ad feat: add code styling
- da30be6 feat: add detail and file shortening options
- 5da75f5 style: refactor into function
- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>README.md</code></summary>

- de3b482 docs: Create README.md

</details>
<details><summary><code>.gitignore</code></summary>

- 1ce8a08 initial commit 🚀

</details>
<details><summary><code>organize.ipynb</code></summary>

- 1ce8a08 initial commit 🚀

</details>
