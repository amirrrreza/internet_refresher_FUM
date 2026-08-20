# internet_refresher_FUM
این برنامه می‌تونه تا حدی مشکل قطع شدن اینترنت دانشگاه رو برطرف کنه. برنامه در پس‌زمینه‌ی کامپیوتر اجرا می‌شود و هر ۱۰ دقیقه یک‌بار اتصال اینترنت رو بررسی و در صورت نیاز دوباره احراز هویت می‌کند. فاصله‌ی زمانی این بررسی‌ها هم قابل تغییره و می‌تونید بسته به نیازتون تنظیمش کنید.
برنامه با زبان پایتون نوشته شده است و پکیج های مورد نیاز برای اجرای برنامه روی لپتاب یا کامپروتر شما را فراهم خواهد کرد.
# =============================================
This program can help reduce the issue of frequent internet disconnections at the university. It runs in the background of your computer and checks the internet connection every 10 minutes. If needed, it automatically re-authenticates to restore access. The checking interval can also be adjusted depending on your needs.

The program is written in Python, and the required packages needed to run it on your laptop or computer can be installed easily.
# =============================================
نحوه عملکرد برنامه

این برنامه از چند بخش اصلی تشکیل شده است:

1. وارد کردن کتابخانه‌های موردنیاز

در این اسکریپت از کتابخانه‌های زیر استفاده شده است:

* `os` — برای خواندن متغیرهای محیطی مانند نام کاربری و رمز عبور
* `time` — برای کنترل فاصله زمانی بین بررسی‌های اتصال
* `requests` — برای بررسی وضعیت دسترسی به اینترنت
* `selenium` — برای انجام خودکار فرایند ورود به سامانه دانشگاه

 2. تنظیمات اولیه

متغیرهای اصلی تنظیمات برنامه شامل موارد زیر هستند:

```python
CHECK_INTERVAL = 10 * 60
LOGIN_URL = "https://access.um.ac.ir/login"
CHECK_URL = "http://example.com"
```

متغیر `CHECK_INTERVAL` مشخص می‌کند که برنامه هر چند وقت یک‌بار اتصال اینترنت را بررسی کند.

به‌صورت پیش‌فرض، این بررسی هر **۱۰ دقیقه** انجام می‌شود.

 3. بررسی اتصال اینترنت

تابع زیر:

```python
internet_is_available()
```

بررسی می‌کند که آیا دسترسی عادی به اینترنت برقرار است یا خیر.

اگر درخواست به صفحه احراز هویت دانشگاه فردوسی هدایت شود، برنامه تشخیص می‌دهد که نشست اینترنت منقضی شده و نیاز به ورود مجدد وجود دارد.

### 4. اجرای مرورگر در پس‌زمینه

تابع زیر:

```python
create_browser()
```

مرورگر Chrome را با استفاده از Selenium ایجاد می‌کند.

کروم میتواند در حالت پنهان **headless** اجرا شود. 
```python
options.add_argument("--headless=new")
```

 5. ورود خودکار به سامانه دانشگاه

تابع:

```python
login(driver)
```

فرایند احراز هویت را به‌صورت خودکار انجام می‌دهد:

1. صفحه ورود دانشگاه را باز می‌کند.
2. فیلد نام کاربری را پیدا می‌کند.
3. فیلد رمز عبور را پیدا می‌کند.
4. اطلاعات ورود را وارد می‌کند.
5. فرم ورود را ارسال می‌کند.
6. بررسی می‌کند که اتصال اینترنت دوباره برقرار شده باشد.

 6. حلقه اصلی بررسی اتصال

تابع اصلی برنامه به‌صورت مداوم وضعیت اینترنت را بررسی می‌کند.

```text
شروع
  │
  ▼
بررسی اتصال اینترنت
  │
  ▼
آیا اینترنت در دسترس است؟
  │
  ├── بله
  │    │
  │    ▼
  │  ۱۰ دقیقه صبر
  │    │
  │    └──────────────► بررسی مجدد
  │
  └── خیر
       │
       ▼
باز کردن صفحه ورود دانشگاه
       │
       ▼
وارد کردن نام کاربری و رمز عبور
       │
       ▼
احراز هویت
       │
       ▼
بررسی مجدد اینترنت
       │
       ▼
۱۰ دقیقه صبر
       │
       └──────────────► بررسی مجدد
```

 7. متوقف کردن برنامه

برنامه به‌صورت مداوم اجرا می‌شود تا زمانی که کاربر آن را متوقف کند.

برای متوقف کردن برنامه در Terminal یا VS Code می‌توانید از کلیدهای زیر استفاده کنید:

```bash
Ctrl + C
```

پس از توقف، نشست Selenium و مرورگر نیز به‌صورت خودکار بسته می‌شود.

---

 🔄 تغییر فاصله زمانی بررسی

برای تغییر فاصله زمانی بررسی اتصال، کافی است مقدار زیر را تغییر دهید:

```python
CHECK_INTERVAL = 10 * 60
```

برای مثال:

```python
CHECK_INTERVAL = 5 * 60
```

باعث می‌شود برنامه هر **۵ دقیقه** یک‌بار وضعیت اتصال اینترنت را بررسی کند.

**تنظیم نام کاربری و رمز عبور**

برای امنیت بیشتر، نام کاربری و رمز عبور مستقیماً داخل فایل Python نوشته نمی‌شوند. برنامه آن‌ها را از **Environment Variables** دریافت می‌کند.

macOS / Linux

در Terminal این دستورات را وارد کنید:

```bash id="hsplp7"
export UM_USERNAME="your_username"
export UM_PASSWORD="your_password"
```

مثال:

```bash id="pvml0t"
export UM_USERNAME="401234567"
export UM_PASSWORD="MyPassword123"
```

سپس برنامه را اجرا کنید:

```bash id="9d5xjq"
python3 ferdowsiuniversitywifi.py
```

> توجه: این متغیرها فقط تا زمانی که همان Terminal باز است باقی می‌مانند.

---

### Windows PowerShell

در PowerShell وارد کنید:

```powershell id="y7a9ni"
$env:UM_USERNAME="your_username"
$env:UM_PASSWORD="your_password"
```

سپس برنامه را اجرا کنید:

```powershell id="lrkj0g"
python ferdowsiuniversitywifi.py
```

---

### Windows CMD

در Command Prompt وارد کنید:

```cmd id="4xgwkp"
set UM_USERNAME=your_username
set UM_PASSWORD=your_password
```

سپس:

```cmd id="l2p3sc"
python ferdowsiuniversitywifi.py
```

---
# =============================================

Features
Automatically checks Internet connectivity
Detects redirection to the university authentication portal
Automatically enters the username and password
Re-authenticates when the Internet session expires
Runs Chrome in headless mode
Works in the background without opening a visible Chrome window
Adjustable connection check interval
Supports macOS, Linux, and Windows
Keeps credentials outside the Python source code using environment variables
Requirements

Make sure you have the following installed:

Python 3
Google Chrome
requests
selenium

Install the required Python packages using:

python3 -m pip install requests selenium

On Windows, you can also use:

python -m pip install requests selenium
Configuration

The main configuration variables are:

CHECK_INTERVAL = 10 * 60

LOGIN_URL = "https://access.um.ac.ir/login"

CHECK_URL = "http://example.com"
Check Interval

The following value means that the Internet connection is checked every 10 minutes:

CHECK_INTERVAL = 10 * 60

For example, to check every 5 minutes:

CHECK_INTERVAL = 5 * 60
Setting Username and Password

For security reasons, the username and password are not stored directly inside the Python file.

Instead, the program reads them from environment variables:

USERNAME = os.environ.get("UM_USERNAME")
PASSWORD = os.environ.get("UM_PASSWORD")
macOS / Linux

Open Terminal and enter:

export UM_USERNAME="your_username"
export UM_PASSWORD="your_password"

Example:

export UM_USERNAME="401234567"
export UM_PASSWORD="MyPassword123"

Then run the program:

python3 ferdowsiuniversitywifi.py

Note: These environment variables remain available only while the current Terminal session is active.

Windows PowerShell

Open PowerShell and enter:

$env:UM_USERNAME="your_username"
$env:UM_PASSWORD="your_password"

Then run:

python ferdowsiuniversitywifi.py
Windows Command Prompt

Open Command Prompt and enter:

set UM_USERNAME=your_username
set UM_PASSWORD=your_password

Then run:

python ferdowsiuniversitywifi.py
How the Program Works

The program consists of several main components.

1. Importing Required Libraries

The script uses the following libraries:

os — reads environment variables such as username and password
time — controls the interval between connection checks
requests — checks whether Internet access is available
selenium — automatically handles authentication through the university login portal
2. Checking the Internet Connection

The function:

internet_is_available()

checks whether normal Internet access is available.

The script sends a request to:

http://example.com

If the request is redirected to:

access.um.ac.ir

the program assumes that the university authentication session has expired.

In that case, automatic authentication is started.

3. Running Chrome in the Background

The function:

create_browser()

creates a Chrome browser using Selenium.

Chrome runs in headless mode:

options.add_argument("--headless=new")

This allows the browser to run completely in the background without opening a visible Chrome window.

Additional options can also be used for better stability:

options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
4. Automatic Authentication

The function:

login(driver)

handles the authentication process automatically.

It:

Opens the Ferdowsi University login page.
Finds the username field.
Finds the password field.
Enters the user's credentials.
Submits the login form.
Waits for authentication.
Checks whether Internet access has been restored.
5. Main Monitoring Loop

The main function continuously checks the Internet connection.

Start
  │
  ▼
Check Internet Connection
  │
  ▼
Is Internet Available?
  │
  ├── Yes
  │    │
  │    ▼
  │  Wait 10 Minutes
  │    │
  │    └──────────────► Check Again
  │
  └── No
       │
       ▼
Open University Login Page
       │
       ▼
Enter Username and Password
       │
       ▼
Authenticate
       │
       ▼
Check Internet Again
       │
       ▼
Wait 10 Minutes
       │
       └──────────────► Check Again
Running the Program

After installing the required packages and setting your username and password, run:

macOS / Linux
python3 ferdowsiuniversitywifi.py
Windows
python ferdowsiuniversitywifi.py

or:

py ferdowsiuniversitywifi.py
Stopping the Program

The program runs continuously until it is manually stopped.

To stop it in Terminal or VS Code, press:

Ctrl + C

The program handles the interruption and closes the Selenium browser session automatically.

Security Notice

Do not store your real university username and password directly inside the Python source code.

Avoid doing this:

USERNAME = "your_username"
PASSWORD = "your_password"

Instead, use environment variables:

export UM_USERNAME="your_username"
export UM_PASSWORD="your_password"

Important Notes
The program does not fix physical Wi-Fi or network infrastructure problems.
It is designed to help with situations where Internet access stops because the university authentication session has expired.
Google Chrome must be installed on the system.
The university login page may change in the future. If its HTML structure changes, the Selenium login logic may also need to be updated.
The default connection check interval is 10 minutes and can be customized.
Disclaimer

This project is an unofficial utility and is not affiliated with or maintained by Ferdowsi University of Mashhad.

Use it responsibly and only with your own university account.

License

This project is provided for educational and personal use.
