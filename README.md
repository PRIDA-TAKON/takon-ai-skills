# 🛠️ Takon AI Skills Repository
### Advanced AI Agent Skills for Engineering, Architecture, and Construction Management
---

[![GitHub CLI](https://img.shields.io/badge/GitHub%20CLI-v2.89.0-blue.svg)](https://cli.github.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()

ชุดเครื่องมือ AI Agent Skills สำหรับเพิ่มประสิทธิภาพการทำงานในสายวิศวกรรมและงานก่อสร้าง 
A collection of professional AI Agent Skills designed to streamline workflows in Engineering and Construction.

---

## 🚀 Available Skills | สกิลที่พร้อมใช้งาน

| Skill Name | Description (TH/EN) | Key Tags |
| :--- | :--- | :--- |
| **DXF Extractor** | สกัดข้อมูล CAD (Text/Block) / Extract CAD Data (Text/Block) | CAD, DXF, CSV |
| **Door Schedule** | จัดการแบบขยายประตู / Door Specifications Automation | Architecture, Door |
| **Construction Doc** | รายงานประจำวันและ Dashboard / Daily Reports & Dashboards | Management, Typhoon AI |

---

## 📦 Installation | การติดตั้ง

ใช้ GitHub CLI เพื่อติดตั้งชุดเครื่องมือทั้งหมด:
Install the entire suite using GitHub CLI:

`bash
gh skill install PRIDA-TAKON/takon-ai-skills
`

---

## 🔍 Skill Details | รายละเอียดเชิงลึก

### 1. 🏗️ DXF Data Extractor (dxf-extractor)
- **TH**: สกัดข้อมูลจากไฟล์ DXF จำนวนมาก (Batch) เช่น Text, Blocks, และ Polylines โดยระบุชื่อไฟล์ต้นทางในผลลัพธ์ CSV อัตโนมัติ
- **EN**: Batch extract entities from multiple DXF files including Text, Blocks, and Polylines, with automatic source filename tracking in CSV output.

### 2. 🚪 Door Schedule Processor (door-processor)
- **TH**: สกัดและทำความสะอาดข้อมูลแบบขยายประตู ดึงสเปคและเลขหน้าอ้างอิง พร้อมกรองคำที่ไม่จำเป็นออกโดยอัตโนมัติ
- **EN**: Extract and clean door schedules from CAD drawings, capturing specs and reference numbers while filtering out redundant noise.

### 3. 📊 Construction Doc Manager (construction-doc)
- **TH**: จัดการรายงานประจำวันและ Dashboard ความคืบหน้า รองรับการแทรกรูปภาพลง Excel และใช้ AI (Typhoon) ช่วยสรุปงาน
- **EN**: Manage daily construction reports and progress dashboards, featuring image insertion into Excel templates and AI-powered (Typhoon) work summaries.

---

## 🛠️ Requirements | ข้อกำหนด
- **GitHub CLI (gh)**: v2.89.0+
- **Compatible AI Agent**: Gemini CLI, GitHub Copilot, or any agent supporting gentskills.io standard.

---

## 🤝 Contribution & Support
- **Author**: Takon (PRIDA-TAKON)
- **License**: MIT
- **Contact**: Feel free to open an Issue for suggestions or feedback!

---
*Created with ❤️ by Takon for the Construction & Engineering Community.*
