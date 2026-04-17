---
name: dxf-data-extractor
version: 1.0.0
description: สกัดข้อมูลจากไฟล์ DXF จำนวนมาก (Text, Blocks, Polylines) ลงไฟล์ CSV
author: takon
tags: [cad, dxf, engineering, automation]
---

# DXF Data Extractor Skill

Skill นี้ช่วยให้ Agent สามารถอ่านและสกัดข้อมูลจากไฟล์ AutoCAD DXF หลายไฟล์พร้อมกัน และสรุปผลออกมาเป็นไฟล์ CSV ที่นำไปใช้งานต่อใน Excel ได้ทันที

## ความสามารถ
- **Batch Processing**: ทำงานกับไฟล์ DXF หลายไฟล์ในโฟลเดอร์เดียว
- **Entity Support**:
    - TEXT, MTEXT: ดึงเนื้อหาข้อความ
    - INSERT: ดึงชื่อ Block และพิกัด
    - LWPOLYLINE, POLYLINE: ดึงข้อมูลเส้นและจุดพิกัด
- **Tracking**: ระบุชื่อไฟล์ต้นทาง (Filename) ในทุกแถวของข้อมูล

## วิธีใช้งาน
สั่งงานกับ Agent เช่น:
- "ช่วยสกัดข้อมูล Text และ Block จากไฟล์ DXF ทั้งหมดในโฟลเดอร์ drawings/ แล้วสรุปเป็น CSV ให้หน่อย"
