Here are the **essential Vim navigation shortcuts** — the ones DevOps engineers use daily when editing config files, scripts, YAML, Dockerfiles, Helm charts, etc.

If you master these, you're already dangerous in Vim 💪

---

## 🚶‍♂️ **Basic Movement**

| Action | Shortcut |
| ------ | -------- |
| Left   | `h`      |
| Down   | `j`      |
| Up     | `k`      |
| Right  | `l`      |

> Think **h j k l** = Left Down Up Right

---

## 📄 **Move by Words**

| Action                              | Shortcut |
| ----------------------------------- | -------- |
| Next word                           | `w`      |
| Next WORD (separated by space only) | `W`      |
| Previous word                       | `b`      |
| End of word                         | `e`      |

---

## 🧭 **Move Start/End of Line**

| Action          | Shortcut   |
| --------------- | ---------- |
| Start of line   | `0` (zero) |
| First non-space | `^`        |
| End of line     | `$`        |

---

## 📜 **Move by Lines / Screen**

| Action        | Shortcut   |
| ------------- | ---------- |
| Top of screen | `H`        |
| Middle        | `M`        |
| Bottom        | `L`        |
| Page down     | `Ctrl + f` |
| Page up       | `Ctrl + b` |

---

## 🔢 **Jump to Specific Line**

| Action            | Shortcut       |
| ----------------- | -------------- |
| Go to line number | `:5` (example) |
| First line        | `gg`           |
| Last line         | `G`            |

---

## 🔍 **Search & Jump**

| Action          | Shortcut |
| --------------- | -------- |
| Search word     | `/word`  |
| Search backward | `?word`  |
| Next match      | `n`      |
| Previous match  | `N`      |

---

## 🎯 **Go to matching bracket**

```vim
%
```

Helps in editing YAML, JSON, functions, loops.

---

## 🪄 **Word Jumping Trick**

| Action                  | Keys           |
| ----------------------- | -------------- |
| Jump inside quotes      | `ci'` or `ci"` |
| Jump inside parentheses | `ci(`          |
| Jump inside brackets    | `ci[`          |

---

## 📦 **Buffers / Tabs / Windows (Advanced DevOps Use)**

| Action             | Shortcut           |
| ------------------ | ------------------ |
| Open file in split | `:split filename`  |
| Vertical split     | `:vsplit filename` |
| Switch split       | `Ctrl + w + w`     |
| New tab            | `:tabnew filename` |
| Next tab           | `gt`               |

---

## 🛑 **Exit & Save**

| Action      | Keys  |
| ----------- | ----- |
| Save        | `:w`  |
| Quit        | `:q`  |
| Save & quit | `:wq` |
| Force quit  | `:q!` |

---

## 💣 **Pro Level Navigation Combo**

Want to fly in Vim? Use numbers:

```
5j    # move 5 lines down
3w    # move 3 words forward
2G    # go to 2nd line
```

---

## 🎓 **DevOps Real-World Tasks Where Vim Helps**

✔️ Editing config files (`/etc/nginx/nginx.conf`)
✔️ Editing `.sh` scripts, Dockerfiles
✔️ Updating YAML for Kubernetes
✔️ Editing EC2 server configs
✔️ Debugging Ansible playbooks

---

## 🎁 Bonus: Must-Know Insert Commands

| Action                  | Shortcut |
| ----------------------- | -------- |
| Insert at cursor        | `i`      |
| Insert at start of line | `I`      |
| Append after cursor     | `a`      |
| Append end of line      | `A`      |
| New line below          | `o`      |
| New line above          | `O`      |

---


