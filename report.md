# 🔐 Password Security & Attack Simulation Report

## 1. 🧾 Introduction

Passwords are the first line of defense in most systems. Weak or predictable passwords can be easily exploited using techniques such as **brute-force attacks** and **wordlist attacks**.

This project demonstrates both:
- Password strength evaluation
- Simulation of password attacks in a controlled environment

---

## 2. 🎯 Objectives

- To analyze password strength using multiple parameters  
- To understand entropy and its role in password security  
- To simulate brute-force and wordlist attacks  
- To demonstrate risks of weak passwords  

---

## 3. 🛠️ Tools & Technologies

- Python  
- Standard Libraries: `re`, `math`, `itertools`, `string`, `time`  

---

## 4. ⚙️ Project Components

### 4.1 Password Strength Checker

The system evaluates password strength based on:

- Length of password  
- Use of uppercase and lowercase letters  
- Inclusion of numbers and special characters  
- Detection of common patterns (e.g., "123", "abc")  
- Comparison with common password list  

#### 🔢 Entropy Calculation

Password entropy is calculated using:
