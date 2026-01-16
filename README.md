<p align="center">
  <img src="https://j.top4top.io/p_3668bwcl20.png" width="220" alt="AYYUBI Logo">
</p>

<h1 align="center">🔐 AYYUBI SIMPLE RANSOMWARE </h1>

<p align="center">
  <b>Simple • Permanent Key </b><br>
  by <b>ayyubi</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue">
  <img src="https://img.shields.io/badge/crypto-fernet-green">
  <img src="https://img.shields.io/badge/status-stable-success">
</p>

---
---

## 🧠 Tentang Project
**AYYUBI Simple Ransomware** adalah tools Python sederhana untuk **enkripsi & dekripsi semua file**  
menggunakan **key permanen berbasis passphrase**.

✔ Tidak tergantung session  
✔ Aman untuk testing & edukasi
✔ Binary‑safe (rb / wb)  
✔ Struktur simpel & mudah dipahami  

---

## 🔑 Sistem Key
- **Passphrase:** `212121`
- Passphrase diubah menjadi **Fernet key valid (SHA‑256)**
- **Key tidak berubah** walau program ditutup / dibuka ulang
- Enkripsi & dekripsi **SELALU KONSISTEN**

---

## 📁 Format File yang Didukung
Karena membaca file sebagai **binary**, semua format didukung:

### 📄 Dokumen
- pdf, docx, xlsx, txt, csv

### 🖼️ Media
- png, jpg, jpeg, gif
- mp3, wav, mp4, mkv

### 📦 Arsip
- zip, rar, 7z, tar, gz

### ⚙️ Binary
- exe, apk, so, bin, dll

➡️ **SEMUA FILE bisa dienkripsi & didekripsi**

---

## ▶️ Cara Penggunaan
Pastikan Python 3 dan library `cryptography` sudah terpasang.

### 🔐 Cara enkripsi dan dekripsi 
```bash

python3 main.py encrypt
python3 main.py decrypt
