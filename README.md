<div align="center">

# 💱 Live Currency Converter
### 🌍 Real-Time Exchange Rates for 160+ Countries | ⚡ Built with Python

<p>
  <b>A fast, zero-config command-line tool that converts money between 160+ countries using live market rates!</b>
</p>

<!-- Static Badges (Never Break — Even on Private Repos!) -->
<p>
  <img src="https://shields.io" alt="Python 3.8+" />
  <img src="https://shields.io" alt="160+ Currencies" />
  <img src="https://shields.io" alt="No API Key Needed" />
  <img src="https://shields.io" alt="Cross Platform" />
</p>

<!-- Clickable Quick Navigation -->
<p>
  <a href="#-what-does-this-project-do-for-everyone">📌 Overview</a> •
  <a href="#-how-it-looks-when-you-run-it">💻 Demo</a> •
  <a href="#-how-to-run-this-even-if-you-are-non-tech">🚀 Quick Start</a> •
  <a href="#-20-popular-currency-codes-you-can-use">🌐 Currencies</a> •
  <a href="#-how-it-works-behind-the-scenes">⚙️ Architecture</a> •
  <a href="#-project-structure">📁 Structure</a> •
  <a href="#-troubleshooting--faq">🛠️ FAQ</a>
</p>

</div>

---

## 🤔 What Does This Project Do? (For Everyone!)

Ever wondered how much **100 USD** is in **Pakistani Rupees (PKR)** or **Indian Rupees (INR)** right now?  
Instead of searching on Google every single time, this tool connects directly to a live financial server on the internet, grabs today's exact exchange rate, and calculates your converted amount in less than a second!

### ✨ Why Use This?
- 🌍 **Live Market Rates:** Always fetches fresh, real-time rates from [ExchangeRate-API](https://www.exchangerate-api.com) (no outdated numbers!).
- 💱 **160+ Currencies Supported:** Works with almost every country in the world.
- 🔑 **No Sign-Up or API Key Needed:** Works instantly out of the box—no accounts or tokens required.
- ⚡ **Lightweight & Fast:** Uses only Python and `requests` with zero bloatware.
- 🧠 **Beginner & User Friendly:** Clean, fast, and super easy to use for both coders and non-tech users.

---

## 💻 How It Looks When You Run It

```text
Convert from  : PKR
Convert to    : INR
Enter amount  : 100
Converted amount: 33.76 INR
```

```text
Convert from  : USD
Convert to    : EUR
Enter amount  : 100
Converted amount: 91.07 EUR
```

---

## 🧑‍💻 How to Run This (Even If You Are Non-Tech!)

You don't need to be a programmer to use this tool. Just follow these **3 simple steps**:

### Step 1: Install Python *(One-Time Setup)*
1. Go to [python.org/downloads](https://python.org) and download **Python 3.8 or higher**.
2. Open the installer and **IMPORTANT:** Check the box that says **"Add Python to PATH"** at the bottom, then click **Install Now**.

### Step 2: Download This Project
* **Easy Way (No Coding):** Click the green **`<> Code`** button at the top of this page ➔ click **`Download ZIP`** ➔ extract the folder on your PC.
* **Developer Way (Git):**
  ```bash
  git clone https://github.com
  cd Currency-Converter
  ```

### Step 3: Run the Converter
1. Open the extracted folder, click the top address bar, type **`cmd`**, and press **Enter**.
2. Type these two commands one by one:
   ```bash
   pip install requests
   python main.py
   ```
3. Type your currency code (like `PKR`), target currency (like `USD`), and amount—done! 🎉

---

## 🌐 20 Popular Currency Codes You Can Use

Type any of these **3-letter codes** when the program asks `Convert from` or `Convert to`:

| Country / Region | Currency Code | Country / Region | Currency Code |
| :--- | :---: | :--- | :---: |
| 🇵🇰 **Pakistan** | `PKR` | 🇨🇦 **Canada** | `CAD` |
| 🇮🇳 **India** | `INR` | 🇦🇺 **Australia** | `AUD` |
| 🇺🇸 **USA** | `USD` | 🇹🇷 **Turkey** | `TRY` |
| 🇬🇧 **UK** | `GBP` | 🇧🇩 **Bangladesh** | `BDT` |
| 🇪🇺 **Europe** | `EUR` | 🇱🇰 **Sri Lanka** | `LKR` |
| 🇦🇪 **UAE** | `AED` | 🇲🇾 **Malaysia** | `MYR` |
| 🇸🇦 **Saudi Arabia** | `SAR` | 🇸🇬 **Singapore** | `SGD` |
| 🇯🇵 **Japan** | `JPY` | 🇰🇷 **South Korea** | `KRW` |
| 🇨🇳 **China** | `CNY` | 🇨🇭 **Switzerland** | `CHF` |
| 🇿🇦 **South Africa** | `ZAR` | 🇳🇵 **Nepal** | `NPR` |

<details>
<summary><b>➕ Click to expand more supported currency codes (Gulf, Europe & More)</b></summary>
<br/>

- 🇶🇦 **Qatar:** `QAR` (Qatari Riyal)
- 🇴🇲 **Oman:** `OMR` (Omani Rial)
- 🇰🇼 **Kuwait:** `KWD` (Kuwaiti Dinar)
- 🇧🇭 **Bahrain:** `BHD` (Bahraini Dinar)
- 🇷🇺 **Russia:** `RUB` (Russian Ruble)
- 🇸🇪 **Sweden:** `SEK` (Swedish Krona)
- 🇳🇴 **Norway:** `NOK` (Norwegian Krone)
- 🇳🇿 **New Zealand:** `NZD` (New Zealand Dollar)

> 💡 **Note:** Over **140+ additional ISO 4217 currency codes** also work automatically!

</details>

---

## ⚙️ How It Works Behind the Scenes

```text
┌───────────────────┐      HTTP GET Request       ┌──────────────────────────┐
│   User Terminal   │ ──────────────────────────► │   ExchangeRate-API       │
│ (PKR ➔ INR, 100)  │                             │   (v6/latest/PKR)        │
└───────────────────┘                             └──────────────────────────┘
         ▲                                                      │
         │                                                      │ Live JSON Data
         │                                                      ▼
┌───────────────────┐     Calculate & Round       ┌──────────────────────────┐
│  Formatted Output │ ◄────────────────────────── │   Python JSON Parser     │
│   (33.76 INR)     │       (amount * rate)       │   data["rates"]["INR"]   │
└───────────────────┘                             └──────────────────────────┘
```

1. **User Input:** Captures `from_currency`, `to_currency`, and `amount` (automatically converting text to uppercase).
2. **API Request:** Sends a live HTTP `GET` request to [ExchangeRate-API](https://www.exchangerate-api.com).
3. **JSON Parsing:** Converts the server response into a Python dictionary and extracts the exact exchange rate.
4. **Calculation:** Multiplies the entered amount by the live rate and formats the output to 2 decimal places.

<details>
<summary><b>🔍 View Sample Live JSON Response</b></summary>
<br/>

```json
{
  "result": "success",
  "base_code": "USD",
  "rates": {
    "USD": 1,
    "PKR": 278.45,
    "INR": 84.12,
    "EUR": 0.91
  }
}
```
</details>

---

## 📁 Project Structure

```text
Currency-Converter/
├── main.py          # Core CLI currency conversion script
├── .gitignore       # Ignores Python cache and virtual environment files
└── README.md        # Project documentation
```

---

## 🛠️ Troubleshooting & FAQ

<details>
<summary><b>❓ Error: <code>ModuleNotFoundError: No module named 'requests'</code></b></summary>
<br/>
Your Python environment doesn't have the <code>requests</code> library installed yet. Run <code>pip install requests</code> in your terminal first, then run <code>python main.py</code> again.
</details>

<details>
<summary><b>❓ Error: <code>KeyError</code> after entering a currency code</b></summary>
<br/>
Make sure you enter a valid <b>3-letter currency code</b> (such as <code>USD</code>, <code>PKR</code>, or <code>EUR</code>) without extra spaces, and check that you are connected to the internet.
</details>

<details>
<summary><b>❓ Do I need to pay or create an account for the API?</b></summary>
<br/>
No! This project uses the open-access endpoint of ExchangeRate-API, which requires zero sign-ups or API keys.
</details>

---

## 🔮 Roadmap & Future Improvements
- [ ] Add `try-except` error handling for invalid currency codes, non-numeric amounts, or offline mode
- [ ] Add a `while True` loop so users can convert multiple amounts without restarting
- [ ] Show historical rate comparisons or last-updated timestamp from the API
- [ ] Build a modern graphical desktop version (GUI) using `CustomTkinter`

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. **Fork** the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com"><b>Sufyan-m</b></a></p>
  <p>⭐ <i>Like this project? Give it a star on GitHub!</i></p>
</div>
