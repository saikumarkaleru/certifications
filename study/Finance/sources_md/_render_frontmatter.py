import subprocess, tempfile, os, time

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ROOT = os.path.dirname(os.path.abspath(__file__))
html = os.path.join(ROOT, "_stock_market_roles_frontmatter.html")
out = os.path.join(ROOT, "_frontmatter.pdf")
if os.path.exists(out):
    os.remove(out)
profile = os.path.join(tempfile.gettempdir(), "chrome_pdf_profile_fm")
url = "file:///" + html.replace("\\", "/")
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-first-run",
                 f"--user-data-dir={profile}", "--no-pdf-header-footer",
                 "--virtual-time-budget=30000", f"--print-to-pdf={out}", url],
                check=False, stderr=subprocess.DEVNULL)
for _ in range(30):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        time.sleep(1)
        break
    time.sleep(1)
print("front matter pdf:", os.path.getsize(out) if os.path.exists(out) else "MISSING")
