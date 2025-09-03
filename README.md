# 🔒 Secure Download Link Verifier  

A preventative **cybersecurity tool/plugin** designed to **verify, assess, and authenticate software download sources**. This tool helps users avoid malicious or fraudulent download links by checking domain authenticity, SSL/TLS certificates, reputation, and vendor registry verification in real time.  

---

## 📌 Abstract  

With the growing reliance on internet-based software distribution, users are at high risk of landing on compromised sites through search engines or ads. Attackers exploit this by spreading **malware, spyware, and phishing software** under fake download pages.  

The **Secure Download Link Verifier** provides users with a **trusted way to validate download sources**. It ensures safer software acquisition by automating:  
- Domain & SSL/TLS verification  
- Vendor registry cross-checks  
- Reputation & WHOIS age lookups  
- Optional checksum/signature validation  

The tool is available as both:  
- 🌐 **Web Application**  
- 🧩 **Browser Extension**  

---

## ⚙️ Features  

✅ Real-time URL verification (Safe / ⚠ Caution / ❌ Unsafe)  
✅ Checks against a **trusted vendor registry**  
✅ SSL/TLS certificate validation  
✅ Domain reputation and WHOIS age checks  
✅ Official safe source recommendations  
✅ File checksum/signature validation (if available)  
✅ Lightweight, modular, and extensible architecture  

---

## 🛠️ Workflow  

1. User enters a **software name** (e.g., `VLC Player`) or pastes a **download URL**.  
2. Back-end normalizes the input and checks against the **trusted vendor registry**.  
3. Verification checks are performed:  
   - Domain authenticity (typo-squatting detection)  
   - SSL/TLS certificate validity  
   - Reputation & WHOIS age  
   - File checksum/signature validation  
4. The system assigns a status:  
   - 🟢 **Verified** (Safe & official source)  
   - ⚠ **Caution** (Suspicious, not fully verified)  
   - ❌ **Unsafe** (Malicious or fraudulent detected)  
5. Results are displayed in a simple, user-friendly interface with safe alternatives suggested.  

---

## 🖥️ Example Output  

**Input Software:** VLC Media Player  
**User Input URL:** `https://vlc-download-free.com`  
**Verified Link:** `https://www.videolan.org/vlc/`  

**Verification Results:**  
- SSL Certificate: ❌ Invalid issuer  
- Domain Age: ⚠ 3 months (Suspicious)  
- Trusted Vendor Registry Match: ❌ No  
- Suggested Official Source: ✅ `https://www.videolan.org/vlc/`  

**Issues Found:**  
1. Suspicious domain (typo-squatting)  
2. Invalid SSL certificate  
3. Not in trusted registry  

---

## 🚨 Issues & Remediation  

- **Suspicious/Look-alike domains** → Use exact vendor domains only.  
- **Invalid SSL certificates** → Accept only valid HTTPS-secured links.  
- **Unverified sources/mirror sites** → Block and suggest verified links.  
- **Checksum/signature mismatch** → Require SHA256/PGP verification when available.  

---

## 📚 General Recommendations  

- Download only from **official vendor websites**.  
- Avoid clicking on **ads/sponsored search results**.  
- Verify **domain spelling** before downloading.  
- Always use **HTTPS with valid SSL**.  
- Validate files using **checksums/digital signatures**.  
- Keep the **trusted registry updated**.  
- Educate users on safe download practices.  

---

## 🏗️ Tech Stack  

- **Frontend:** React (User Dashboard)  
- **Backend:** Python (FastAPI / Flask)  
- **APIs/Modules:** Domain reputation checks, WHOIS, SSL validation  
- **Deployment:** Browser Extension + Web App  

---

## 🚀 Future Enhancements  

- 🔄 Automated updates to the trusted vendor registry  
- 🔗 Third-party security service API integration  
- 📦 Integration with browser download managers  
- 🛡️ Advanced phishing/malware detection  

---


This project is released under the **MIT License** – free to use, modify, and distribute.  
