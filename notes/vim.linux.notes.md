# Vim and Linux Quick Reference

Commonly used Vim commands and a few essential Linux operations.

---

### Compression

```bash
tar -czvf archive.tar.gz my_directory    # Compress
tar -xzvf archive.tar.gz                 # Extract
````

---

### Exiting

| Command | Description         |
| ------- | ------------------- |
| `:q`    | Quit                |
| `:q!`   | Quit without saving |
| `:w`    | Save                |
| `:wq`   | Save and quit       |

---

### Cursor Movement

| Command             | Description                          |
| ------------------- | ------------------------------------ |
| `h` `j` `k` `l`     | Arrow keys (left, down, up, right)   |
| `Ctrl+f` / `Ctrl+b` | Page forward / backward              |
| `Ctrl+d` / `Ctrl+u` | Move down / up half a page           |
| `G`                 | Go to bottom of file                 |
| `gg`                | Go to top of file                    |
| `{` / `}`           | Move forward / backward by paragraph |
| `Ctrl+e` / `Ctrl+y` | Scroll down / up one line            |
| `0`                 | Start of line                        |
| `^`                 | First non-blank character of line    |
| `$`                 | End of line                          |
| `%`                 | Jump between matching `()` or `{}`   |

---

### Editing

| Command   | Description                        |
| --------- | ---------------------------------- |
| `u`       | Undo                               |
| `Ctrl+r`  | Redo                               |
| `i` / `a` | Insert mode before / after cursor  |
| `I` / `A` | Insert mode at start / end of line |

---

### Visual Mode (Selecting Text)

| Command  | Description              |
| -------- | ------------------------ |
| `v`      | Character-wise selection |
| `V`      | Line-wise selection      |
| `Ctrl+v` | Block-wise selection     |

---

### Clipboard

| Command | Description               |
| ------- | ------------------------- |
| `y`     | Yank (copy) selected text |
| `p`     | Paste after cursor        |

---

### Deletion

| Command | Description          |
| ------- | -------------------- |
| `d`     | Delete (cut)         |
| `x`     | Delete one character |

---

### Search and Replace

| Command              | Description                              |
| -------------------- | ---------------------------------------- |
| `:%s/<old>/<new>/g`  | Replace all `<old>` with `<new>` in file |
| `:%s/<old>/<new>/gc` | Replace all with confirmation            |
| `/<text>`            | Search forward for `<text>`              |
| `?<text>`            | Search backward for `<text>`             |

---

### Commenting Out Blocks

1. Press `Esc` to exit insert mode.
2. Press `Ctrl+v` to enter **visual block mode**.
3. Use `j` / `k` to select the lines.
4. Press `Shift+i` (capital `I`).
5. Type your comment prefix (e.g. `% `).
6. Press `Esc` twice.

