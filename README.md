# Ransomware Simulator (Educational)

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Safety](https://img.shields.io/badge/security-harmless_educational_tool-red)

A harmless ransomware simulation designed to educate users about how ransomware attacks work and how to protect against them. **NO actual files are encrypted** - this is purely an educational tool.

## 📌 Overview

This Python script creates a safe simulation of a ransomware attack to:
- Demonstrate how ransomware encrypts files and demands payment
- Show the importance of regular backups
- Teach cybersecurity best practices
- Raise awareness about ransomware threats

All operations occur in a temporary directory and no real files are modified.

## 🛡️ Safety Notice

❗ **This is an educational tool only** ❗  
✅ **Safe to run** - No actual encryption occurs  
✅ **No malicious code** - Completely harmless simulation  
✅ **Self-cleaning** - All created files are temporary and automatically removed  

**DO NOT** use this tool maliciously or without proper authorization. This is for **educational purposes only**.

## 🚀 Features

- Simulates ransomware encryption process (harmlessly)
- Creates realistic ransom note with educational information
- Demonstrates two recovery scenarios:
  - Paying the ransom (with warnings about risks)
  - Restoring from backups (recommended approach)
- Provides cybersecurity education resources
- Self-contained temporary environment
- Complete cleanup after execution

## 📋 Prerequisites

- Python 3.6+
- No additional dependencies required

## 🛠️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ransomware-simulator.git
   cd ransomware-simulator
   ```

2. Run the simulator:
   ```bash
   python ransomware_simulator.py
   ```

3. Follow the on-screen instructions to:
   - Create the simulation environment
   - Run the ransomware simulation
   - Explore recovery options
   - Learn about ransomware protection

## 📸 Screenshots

![Simulation in progress](screenshots/simulation.png)  
*Example of the simulation in progress*

![Recovery options](screenshots/recovery.png)  
*Recovery options menu*

## 📚 Educational Resources

The simulator includes links to:
- [CISA Ransomware Guide](https://www.cisa.gov/stopransomware)
- [No More Ransom Project](https://www.nomoreransom.org/)
- [FTC Ransomware Info](https://www.consumer.ftc.gov/articles/how-protect-yourself-ransomware)

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Ethical Use Warning

This tool is for **educational purposes only**. Unauthorized use of ransomware simulation tools against systems you don't own may be illegal. Always obtain proper authorization before performing any security testing.

**The developer assumes no liability and is not responsible for any misuse or damage caused by this tool.**
```

### Recommended Repository Structure:
```
ransomware-simulator/
├── ransomware_simulator.py  # Main Python script
├── README.md                # This file
├── LICENSE                  # MIT License file
└── screenshots/             # Folder for demonstration screenshots
    ├── simulation.png
    └── recovery.png
```

### TODO Notes:
1. Create a `LICENSE` file (MIT recommended for educational projects)
2. Add actual screenshots to the `screenshots` directory
3. Adding a `.gitignore` file for Python
4. For extra credibility:
   - A Code of Conduct
   - Contributing guidelines
   - Security policy
