import ezdxf
import csv
import sys
import os
import re

# Blacklist of keywords to filter out
BLACKLIST = ['TYPE', 'ADDITIONAL EQUIPMENT', 'AREA:', 'โล่ง', '200X200', '200X300', 'FD.', 'REF.', '-']

def is_blacklisted(text):
    clean_text = text.strip().upper()
    if not clean_text or clean_text == '-':
        return True
    return any(item.upper() in clean_text for item in BLACKLIST if item != '-')

def process_door_schedule(dxf_path, output_path):
    print(f"--- Processing: {os.path.basename(dxf_path)} ---")
    
    try:
        doc = ezdxf.readfile(dxf_path)
    except Exception as e:
        print(f"ERROR: Could not read DXF file. {e}")
        return False

    # 1. Validation: Check if there are Layouts (Pages)
    layouts = [l.name for l in doc.layouts if l.name.lower() != 'model']
    if not layouts:
        print("VALIDATION WARNING: No Layouts found. Text will not be associated with page numbers.")
    else:
        print(f"VALIDATION SUCCESS: Found {len(layouts)} layouts (pages).")

    # 2. Map Viewports to Layouts (for Model Space text association)
    # Note: Using the specific shift found for this project. 
    # In a general skill, we might need to adjust this or make it a parameter.
    # For now, we'll use the proven logic for this project's structure.
    layout_viewports = []
    SHIFT_X = 15970
    OFFSET_Y = -15551

    for l in doc.layouts:
        if l.name.lower() == 'model': continue
        for vp in l.query('VIEWPORT'):
            if vp.dxf.id == 1: continue 
            vc = vp.dxf.view_center_point
            vh = vp.dxf.view_height
            aspect = vp.dxf.width / vp.dxf.height
            vw = vh * aspect
            
            actual_vc_x = vc.x + SHIFT_X
            actual_vc_y = vc.y + OFFSET_Y

            layout_viewports.append({
                'layout': l.name,
                'min_x': actual_vc_x - vw/2, 'max_x': actual_vc_x + vw/2,
                'min_y': actual_vc_y - vh/2, 'max_y': actual_vc_y + vh/2
            })

    # 3. Extract Text from Model Space (Recursive for blocks)
    msp = doc.modelspace()
    all_msp_text = []

    def process_entities(entities):
        for e in entities:
            if e.dxftype() in ['TEXT', 'MTEXT']:
                text = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
                if not text or is_blacklisted(text): continue
                pos = getattr(e.dxf, 'insert', getattr(e.dxf, 'align_point', None))
                if pos:
                    all_msp_text.append({'text': text, 'pos': (pos.x, pos.y)})
            elif e.dxftype() == 'INSERT':
                try:
                    process_entities(e.virtual_entities())
                except: pass

    print("Extracting and filtering Model Space text...")
    process_entities(msp)

    # 4. Extract Text from Paper Space (directly on layouts)
    paper_text = []
    for l in doc.layouts:
        if l.name.lower() == 'model': continue
        for e in l.query('TEXT MTEXT'):
            t = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
            if t and not is_blacklisted(t):
                paper_text.append({'Text': t, 'Page Number': l.name})

    # 5. Combine and Associate
    final_results = []
    for item in all_msp_text:
        px, py = item['pos']
        page = "Unknown"
        for vp in layout_viewports:
            if vp['min_x'] <= px <= vp['max_x'] and vp['min_y'] <= py <= vp['max_y']:
                page = vp['layout']
                break
        final_results.append({'Text': item['text'], 'Page Number': page})
    
    final_results.extend(paper_text)

    # 6. Save to CSV
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['Text', 'Page Number'])
        writer.writeheader()
        writer.writerows(final_results)

    print(f"SUCCESS: Saved {len(final_results)} cleaned entries to {output_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_door_schedule.py <input.dxf> <output.csv>")
    else:
        process_door_schedule(sys.argv[1], sys.argv[2])
