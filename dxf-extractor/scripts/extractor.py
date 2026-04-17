import csv
import os
import glob
import sys

def extract_dxf_data(dxf_path):
    """
    สกัดข้อมูลจากไฟล์ DXF (Text, MText, Block, Polygon/Polyline)
    """
    try:
        with open(dxf_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [line.strip() for line in f.readlines()]
    except Exception as e:
        return []

    results = []
    current_entity = None
    entity_data = {}
    filename = os.path.basename(dxf_path)

    i = 0
    while i < len(lines) - 1:
        code = lines[i]
        value = lines[i+1]
        
        if code == '0':
            # เมื่อเจอ Entity ใหม่ ให้บันทึกข้อมูล Entity เก่า
            if current_entity in ['TEXT', 'MTEXT', 'INSERT', 'LWPOLYLINE', 'POLYLINE']:
                results.append(process_entity(current_entity, entity_data, filename))
            
            current_entity = value
            entity_data = {}
        else:
            # เก็บค่าไว้ตาม Group Code (ถ้า Code ซ้ำ เช่น พิกัด Polyline ให้เก็บเป็น List)
            if code in entity_data:
                if isinstance(entity_data[code], list):
                    entity_data[code].append(value)
                else:
                    entity_data[code] = [entity_data[code], value]
            else:
                entity_data[code] = value
        
        i += 2

    # บันทึก Entity ตัวสุดท้าย
    if current_entity in ['TEXT', 'MTEXT', 'INSERT', 'LWPOLYLINE', 'POLYLINE']:
        results.append(process_entity(current_entity, entity_data, filename))

    return results

def process_entity(etype, data, filename):
    """
    แปลงข้อมูลดิบจาก DXF เป็น Dictionary สำหรับ CSV
    """
    content = ""
    if etype in ['TEXT', 'MTEXT']:
        content = data.get('1', '')
    elif etype == 'INSERT':
        content = f"Block: {data.get('2', '')}"
    elif etype in ['LWPOLYLINE', 'POLYLINE']:
        # สำหรับ Polyline เราจะเก็บจำนวนจุด (Code 90) หรือพิกัด
        content = f"Points: {data.get('90', 'N/A')}"

    return {
        'Filename': filename,
        'Type': etype,
        'Content': content,
        'Layer': data.get('8', ''),
        'X': data.get('10', '') if not isinstance(data.get('10'), list) else data.get('10')[0],
        'Y': data.get('20', '') if not isinstance(data.get('20'), list) else data.get('20')[0]
    }

def run_batch_extraction(input_dir, output_csv):
    """
    รันสกัดข้อมูลทุกไฟล์ในโฟลเดอร์
    """
    dxf_files = glob.glob(os.path.join(input_dir, "*.dxf"))
    if not dxf_files:
        print(f"No DXF files found in {input_dir}")
        return

    all_data = []
    print(f"Found {len(dxf_files)} files. Extracting...")

    for f in dxf_files:
        all_data.extend(extract_dxf_data(f))

    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Filename', 'Type', 'Content', 'Layer', 'X', 'Y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_data:
            writer.writerow(row)
    
    print(f"Done! Extracted {len(all_data)} items from {len(dxf_files)} files to {output_csv}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py extractor.py <target_directory> [output_file.csv]")
        sys.exit(1)
        
    target_dir = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else "master_extraction.csv"
    run_batch_extraction(target_dir, output_name)
