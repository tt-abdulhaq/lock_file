# 🔐 Encryptor - File Encryption & Decryption CLI Tool

A cross-platform **command-line tool** for **encrypting and decrypting files** using a password-based key. Works on **Windows and Linux** as a standalone executable.


---

## 📥 Installation

### 🔹 Linux (Ubuntu, macOS)

1. **Download & Save the Script**
   ```sh
   wget https://raw.githubusercontent.com/tt-abdulhaq/lock_file/main/main.py -O encryptor
   chmod +x encryptor
   ```

2. **Move to a Global Path**
   ```sh
   sudo mv encryptor /usr/local/bin/
   ```

3. **Run from Any Terminal**

   To encript a file
   ```sh
   encryptor encrypt --input credentials --key "MySecretKey"
   ```
   To descryp and file 
   ```sh
      encryptor decrypt --input credentials.encrypted --key "MySecretKey"
      ```

---

### 🔹 Windows (Standalone EXE)

1. **Install Dependencies**
   Install `pyinstaller` using pip:
   ```sh
   pip install pyinstaller
   ```

2. **Build Executable**
   Run the following command to create the `.exe` file:
   ```sh
   pyinstaller --onefile encryptor.py
   ```

3. **Move Executable to System Path (Optional)**
   Add the `dist` folder to your system environment variable:
   ```sh
   setx PATH "%PATH%;C:\path\to\dist"
   ```

4. **Run from CMD or PowerShell**
   ```sh
   encryptor.exe encrypt --input myfile.txt --key "MySecretKey"
   ```

---

## 🛠 Usage

### 🔹 Encrypt a File
```sh
encryptor encrypt --input myfile.txt --key "MySecretKey"
```
✅ **Creates** `myfile.txt.encrypted`.

### 🔹 Decrypt a File
```sh
encryptor decrypt --input myfile.txt.encrypted --key "MySecretKey"
```
✅ **Restores** `myfile.txt`.

---

## 🔄 Troubleshooting

- **File Not Found?**
  > Ensure the file exists in the same directory or provide a full path.

- **Incorrect Key on Decryption?**
  > The same key used for encryption must be used for decryption.

- **Permission Denied?**
  > Run the command with `sudo` (Linux) or **Administrator Mode** (Windows).

---


