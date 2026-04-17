# DXF Compatibility for Door Schedule Processor

เพื่อให้ Skill นี้ทำงานได้อย่างถูกต้อง ไฟล์ DXF ควรมีลักษณะดังนี้:

## 1. การจัดหน้า (Layouts/Paper Space)
- ข้อมูลควรถูกจัดแบ่งเป็นหน้าๆ ใน Paper Space (Layout)
- ชื่อของ Layout จะถูกนำมาใช้เป็น 'Page Number' ในไฟล์ CSV (เช่น IA7.101, IA7.102)
- หากไม่มี Layout สคริปต์จะระบุเลขหน้าเป็น "Unknown"

## 2. มุมมอง (Viewports)
- ในแต่ละ Layout ควรมี Viewport ที่ส่องไปยัง Model Space ของแบบขยายนั้นๆ
- สคริปต์ใช้การคำนวณตำแหน่งพิกัดจาก Viewport เพื่อจับคู่ข้อความใน Model Space เข้ากับเลขหน้า

## 3. รูปแบบข้อความ (Text Patterns)
- รองรับทั้ง TEXT และ MTEXT
- รองรับการเขียนข้อความใน Blocks (สคริปต์จะทำการ Explode เสมือนเพื่อดึงข้อความออกมา)

## 4. ข้อจำกัด
- สคริปต์ถูกปรับจูน (Calibrated) สำหรับโครงการที่มีการ Shift พิกัดใน Model Space เฉพาะตัว หากนำไปใช้กับโครงการอื่นที่มีการจัดวางต่างกัน อาจต้องมีการปรับค่า SHIFT_X และ OFFSET_Y ในสคริปต์
