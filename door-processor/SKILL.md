---
name: door-schedule-processor
version: 1.0.0
description: สกัดและทำความสะอาดข้อมูลแบบขยายประตูจากไฟล์ DXF (Extract and clean door schedules)
author: takon
tags: [architecture, doors, dxf, automation]
---

# Door Schedule Processor

Skill นี้สำหรับสกัดข้อมูลสเปคประตูและเลขหน้าอ้างอิงจากแบบขยายประตู (Door Schedule) ในไฟล์ DXF พร้อมระบบการทำความสะอาดข้อมูล (Cleaning) อัตโนมัติ

## ความสามารถ
- **Extract Specifications**: ดึงข้อมูลสเปคของบานประตูแต่ละแบบ
- **Viewport Tracking**: คัดกรองข้อมูลตามพิกัดหน้ากระดาษ (Layouts)
- **Blacklist Filter**: กรองคำที่ไม่จำเป็นออกโดยอัตโนมัติ (เช่น "TYPE", "AREA", "ADDITIONAL EQUIPMENT")

## วิธีใช้งาน
สั่งงานกับ Agent เช่น:
- "ช่วยสกัดสเปคประตูจากไฟล์ door_schedules.dxf และลบคำที่ไม่จำเป็นออกให้หมด"
