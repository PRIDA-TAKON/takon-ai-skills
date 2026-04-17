# Excel Template Requirement 📊

สคริปต์ generate_report.py ต้องการไฟล์ Excel Template เพื่อนำข้อมูลไปกรอกและแทรกรูปภาพ
The generate_report.py script requires an Excel template to populate data and insert images.

### การตั้งค่าไฟล์ (File Setup):
- **ชื่อไฟล์ที่แนะนำ (Default Name):** REPORT_template.xlsx (หรือระบุผ่าน Argument ในสคริปต์)
- **ตำแหน่งที่วาง (Location):** วางไว้ในโฟลเดอร์ construction-doc/templates/

### เซลล์ที่ใช้งาน (Target Cells):
สคริปต์จะพยายามแทรกข้อมูลลงในตำแหน่งต่อไปนี้:
- **Images (รูปภาพ):** E66, Z66, E69, Z69, E72, Z72
- **Captions (คำบรรยาย):** E67, Z67, E70, Z70, E73, Z73

*หมายเหตุ: โปรดเตรียมไฟล์ Template ที่มีหัวกระดาษและโลโก้บริษัทของคุณไว้ในตำแหน่งที่ถูกต้องก่อนรันสคริปต์*
