<div align="center">

# 🔢 Binary Encoder
### 💻 Convert Plain Text into Clean 8-Bit Binary | ⚡ Built with Pure Python

<p>
  <b>A fast, lightweight, zero-dependency command-line tool that converts any text into clean, space-separated 8-bit binary blocks!</b>
</p>

<!-- Static Badges (Never Break — Even on Private Repos!) -->
<p>
  <img src="https://shields.io" alt="Python 3.8+" />
  <img src="https://shields.io" alt="Zero Dependencies" />
  <img src="https://shields.io" alt="8-Bit ASCII" />
  <img src="https://shields.io" alt="Cross Platform" />
</p>

<!-- Clickable Quick Navigation -->
<p>
  <a href="#-what-does-this-project-do">📌 Overview</a> •
  <a href="#-how-it-looks-when-you-run-it">💻 Demo</a> •
  <a href="#-how-to-run-this">🚀 Quick Start</a> •
  <a href="#-ascii-to-binary-cheat-sheet">📊 Cheat Sheet</a> •
  <a href="#-how-it-works-behind-the-scenes">⚙️ Architecture</a> •
  <a href="#-project-structure">📁 Structure</a> •
  <a href="#-troubleshooting--faq">🛠️ FAQ</a>
</p>

</div>

---

## 🤔 What Does This Project Do?

Computers don't understand letters like `A`, `B`, or `C`—they only speak in **1s and 0s** (binary).  
**Binary Encoder** takes any normal text you type and instantly translates each character into its exact **8-bit binary representation** (`0`s and `1`s), cleanly separated by spaces so it's easy to read, copy, or study!

### ✨ Why Use This?
- ⚡ **Zero Dependencies:** Uses only Python's built-in standard library—no `pip install` needed!
- 🧱 **Clean 8-Bit Formatting:** Automatically pads every character to a full 8-bit byte (`01001000` instead of `1001000`).
- 🛡️ **Built-in Input Validation:** Prevents empty submissions and handles whitespace cleanly.
- 🧩 **Modular Codebase:** Written with type hints (`text: str -> str`) and a clean `main()` entry point so you can easily import `text_to_binary()` into other projects.

---

## 💻 How It Looks When You Run It

```text
Enter your text: Hi
Binary: 01001000 01101001
```

```text
Enter your text: Sufyan
Binary: 01010011 01110101 01100110 01111001 01100001 01101110
```

```text
Enter your text: 
Error: Please enter some valid text!
```

---

## 🚀 How to Run This

No third-party packages required! Just make sure **Python 3.8+** is installed on your system:

### Step 1: Clone or Download
* **Easy Way (No Coding):** Click the green **`<> Code`** button at the top of this page ➔ click **`Download ZIP`** ➔ extract the folder.
* **Developer Way (Git):**
  ```bash
  git clone https://github.com
  cd BinaryEncoder
  ```

### Step 2: Run the Script
Open your terminal inside the project folder and run:
```bash
python main.py
```
Type any word, sentence, or symbol and press **Enter**! 🎉

---

## 📊 ASCII to Binary Cheat Sheet

Here is how `BinaryEncoder` translates common characters under the hood:

| Character | Decimal (ASCII) | 8-Bit Binary Output | Character | Decimal (ASCII) | 8-Bit Binary Output |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `A` | `65` | `01000001` | `a` | `97` | `01100001` |
| `B` | `66` | `01000010` | `b` | `98` | `01100010` |
| `C` | `67` | `01000011` | `c` | `99` | `01100011` |
| `0` | `48` | `00110000` | `1` | `49` | `00110001` |
| `@` | `64` | `01000000` | `!` | `33` | `00100001` |
| *(Space)* | `32` | `00100000` | `?` | `63` | `00111111` |

---

## ⚙️ How It Works Behind the Scenes

```text
┌───────────────────┐     ord(letter)      ┌──────────────────────────┐
│   Input Text      │ ───────────────────► │   Unicode / ASCII Code   │
│      ("Hi")       │                      │   'H' = 72, 'i' = 105    │
└───────────────────┘                      └──────────────────────────┘
                                                        │
                                                        │ format(..., '08b')
                                                        ▼
┌───────────────────┐    " ".join(...)     ┌──────────────────────────┐
│  Formatted Output │ ◄─────────────────── │   8-Bit Binary Blocks    │
│ 01001000 01101001 │                      │ ['01001000', '01101001'] │
└───────────────────┘                      └──────────────────────────┘
```

1. **Input & Validation:** Reads user text via `input().strip()` and checks that it isn't empty.
2. **Character-to-Number (`ord`):** Loops through every character and gets its integer Unicode/ASCII code point.
3. **8-Bit Formatting (`format`):** Converts the integer into an 8-digit binary string (`'08b'`), automatically stripping the `0b` prefix and padding leading zeros.
4. **Output Joining:** Joins all 8-bit blocks with spaces (`" ".join()`) for clean readability.

<details>
<summary><b>🧩 Using <code>text_to_binary()</code> in Your Own Python Code</b></summary>
<br/>

Because `main.py` uses `if __name__ == "__main__":`, you can import the converter function directly into another script:

```python
from main import text_to_binary

encoded = text_to_binary("Hello")
print(encoded)
# Output: 01001000 01100101 01101100 01101100 01101111
```
</details>

---

## 📁 Project Structure

```text
BinaryEncoder/
├── main.py          # Core text-to-binary encoder script
└── README.md        # Project documentation
```

---

## 🛠️ Troubleshooting & FAQ

<details>
<summary><b>❓ Do I need to install any libraries using <code>pip</code>?</b></summary>
<br/>
No! This project uses 100% built-in Python functions (<code>ord()</code> and <code>format()</code>), so it works right out of the box.
</details>

<details>
<summary><b>❓ Why does every letter have 8 digits instead of 7?</b></summary>
<br/>
Standard computing stores data in <b>bytes</b> (8 bits per byte). Padding with leading zeros (e.g., <code>01000001</code> instead of <code>1000001</code>) ensures every character aligns cleanly into a full 1-byte block.
</details>

<details>
<summary><b>❓ Does it work with numbers, spaces, and symbols?</b></summary>
<br/>
Yes! Spaces, punctuation marks (<code>!</code>, <code>@</code>, <code>#</code>), and digits (<code>0-9</code>) all have ASCII/Unicode values and are converted automatically.
</details>

---

## 🔮 Roadmap & Future Improvements
- [ ] Add a **Binary Decoder** mode (`01001000 01101001` ➔ `Hi`)
- [ ] Add an interactive menu (`[1] Encode Text` / `[2] Decode Binary` / `[3] Exit`)
- [ ] Add support for encoding/decoding `.txt` files directly
- [ ] Build a clean desktop GUI using `CustomTkinter`

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. **Fork** the repository
2. Create your feature branch (`git checkout -b feature/BinaryDecoder`)
3. Commit your changes (`git commit -m 'Add binary decoder mode'`)
4. Push to the branch (`git push origin feature/BinaryDecoder`)
5. Open a **Pull Request**

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com"><b>Sufyan-m</b></a></p>
  <p>⭐ <i>Like this project? Give it a star on GitHub!</i></p>
</div>
