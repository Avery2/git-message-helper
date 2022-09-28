# git-message-helper

## Example

### Command

`rm output.txt; git log --name-only --oneline -n 10 >> python3 organize.py >> output.txt`

### `log.txt`

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

### `output.txt`

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

### Output for GitHub

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
