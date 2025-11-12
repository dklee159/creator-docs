import os
import re
from collections import defaultdict
from pathlib import Path

def extract_tags_with_apis(file_path):
    """Extract all tags with their associated APIs from a YAML file - complete version"""
    results = {
        'class': [],
        'properties': [],
        'methods': [],
        'events': [],
        'callbacks': []
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        class_name = None
        class_tags_line = None
        
        # Extract class name and find class-level tags
        for i, line in enumerate(lines):
            if line.startswith('name:') and not class_name:
                class_name = line.split('name:')[1].strip()
            elif line.strip().startswith('tags:') and class_name:
                # Check if this is class-level tags (before any section like properties/methods)
                is_class_level = True
                for j in range(i - 1, max(0, i - 100), -1):
                    prev_stripped = lines[j].strip()
                    if prev_stripped in ['properties:', 'methods:', 'events:', 'callbacks:']:
                        is_class_level = False
                        break
                
                if is_class_level:
                    class_tags_line = i
                    # Extract class-level tags
                    tags_list = []
                    inline_match = re.search(r'tags:\s*\[([^\]]+)\]', line)
                    if inline_match:
                        tags_str = inline_match.group(1)
                        tag_items = [t.strip().strip('"\'') for t in tags_str.split(',') if t.strip()]
                        tags_list.extend(tag_items)
                    else:
                        line_indent = len(line) - len(line.lstrip())
                        j = i + 1
                        while j < len(lines):
                            next_line = lines[j]
                            next_stripped = next_line.strip()
                            next_indent = len(next_line) - len(next_line.lstrip())
                            
                            if not next_stripped:
                                k = j + 1
                                while k < len(lines) and not lines[k].strip():
                                    k += 1
                                if k < len(lines):
                                    k_indent = len(lines[k]) - len(lines[k].lstrip())
                                    if not (lines[k].strip().startswith('-') and k_indent > line_indent):
                                        break
                                else:
                                    break
                            elif next_stripped.startswith('-'):
                                if next_indent > line_indent:
                                    tag_match = re.search(r'-\s*(\w+)', next_line)
                                    if tag_match:
                                        tags_list.append(tag_match.group(1).strip())
                                else:
                                    break
                            elif next_stripped and not next_stripped.startswith('#'):
                                if next_indent <= line_indent:
                                    break
                            j += 1
                    
                    for tag in tags_list:
                        results['class'].append({
                            'tag': tag,
                            'api': class_name,
                            'class': class_name
                        })
                    break
        
        if not class_name:
            return None, results
        
        # Build a map of line numbers to item names and sections
        item_map = {}  # line_number -> (item_name, section)
        current_section = None
        
        # First pass: identify all API items (not parameters)
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Skip class-level tags line
            if i == class_tags_line:
                continue
            
            # Detect section
            if stripped == 'properties:':
                current_section = 'properties'
            elif stripped == 'methods:':
                current_section = 'methods'
            elif stripped == 'events:':
                current_section = 'events'
            elif stripped == 'callbacks:':
                current_section = 'callbacks'
            elif stripped.startswith('- name:'):
                item_name = stripped.split('- name:')[1].strip()
                
                # Check if this is an API item or a parameter
                line_indent = len(line) - len(line.lstrip())
                
                # API items: have ":" in name OR are at low indentation (2-4 spaces)
                # Also check: if it's in events/callbacks section, it might not have ":"
                is_api_item = False
                if current_section in ['events', 'callbacks']:
                    # Events and callbacks might not have ":" in name
                    is_api_item = (line_indent <= 4)
                else:
                    # For properties and methods, check for ":" or low indentation
                    is_api_item = (':' in item_name) or (line_indent <= 4)
                
                if current_section and is_api_item:
                    item_map[i] = (item_name, current_section)
        
        # Second pass: find tags and associate with items
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Skip class-level tags line
            if i == class_tags_line:
                continue
            
            if stripped.startswith('tags:'):
                # Found tags line - find the associated item
                tags_list = []
                
                # Check for inline format: tags: [Tag1, Tag2]
                inline_match = re.search(r'tags:\s*\[([^\]]+)\]', line)
                if inline_match:
                    tags_str = inline_match.group(1)
                    tag_items = [t.strip().strip('"\'') for t in tags_str.split(',') if t.strip()]
                    tags_list.extend(tag_items)
                else:
                    # Multi-line format
                    line_indent = len(line) - len(line.lstrip())
                    j = i + 1
                    while j < len(lines):
                        next_line = lines[j]
                        next_stripped = next_line.strip()
                        next_indent = len(next_line) - len(next_line.lstrip())
                        
                        if not next_stripped:
                            k = j + 1
                            while k < len(lines) and not lines[k].strip():
                                k += 1
                            if k < len(lines):
                                k_indent = len(lines[k]) - len(lines[k].lstrip())
                                if not (lines[k].strip().startswith('-') and k_indent > line_indent):
                                    break
                            else:
                                break
                        elif next_stripped.startswith('-'):
                            if next_indent > line_indent:
                                tag_match = re.search(r'-\s*(\w+)', next_line)
                                if tag_match:
                                    tags_list.append(tag_match.group(1).strip())
                            else:
                                break
                        elif next_stripped and not next_stripped.startswith('#'):
                            if next_indent <= line_indent:
                                break
                        j += 1
                
                # Find the associated item by looking backwards
                item_name = None
                item_section = None
                
                # Look backwards to find the most recent API item (not parameter)
                for k in range(i - 1, -1, -1):
                    if k in item_map:
                        item_name, item_section = item_map[k]
                        break
                    # Check if we've hit a section boundary
                    prev_stripped = lines[k].strip()
                    if prev_stripped in ['properties:', 'methods:', 'events:', 'callbacks:']:
                        break
                
                if item_name and item_section:
                    # Store tags with the found item
                    if item_section == 'properties':
                        for tag in tags_list:
                            results['properties'].append({
                                'tag': tag,
                                'api': item_name,
                                'class': class_name
                            })
                    elif item_section == 'methods':
                        for tag in tags_list:
                            results['methods'].append({
                                'tag': tag,
                                'api': item_name,
                                'class': class_name
                            })
                    elif item_section == 'events':
                        for tag in tags_list:
                            results['events'].append({
                                'tag': tag,
                                'api': item_name,
                                'class': class_name
                            })
                    elif item_section == 'callbacks':
                        for tag in tags_list:
                            results['callbacks'].append({
                                'tag': tag,
                                'api': item_name,
                                'class': class_name
                            })
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        import traceback
        traceback.print_exc()
    
    return class_name, results

def main():
    classes_dir = Path('content/en-us/reference/engine/classes')
    
    if not classes_dir.exists():
        print(f"Directory not found: {classes_dir}")
        return
    
    # Organize by tag
    tag_to_apis = defaultdict(lambda: {
        'classes': set(),
        'properties': [],
        'methods': [],
        'events': [],
        'callbacks': []
    })
    
    files_processed = 0
    errors = []
    
    # Process all YAML files
    for yaml_file in sorted(classes_dir.glob('*.yaml')):
        files_processed += 1
        class_name, results = extract_tags_with_apis(yaml_file)
        
        if class_name:
            # Process class-level tags
            for item in results['class']:
                tag = item['tag']
                tag_to_apis[tag]['classes'].add(item['api'])
            
            # Process properties
            for item in results['properties']:
                tag = item['tag']
                tag_to_apis[tag]['properties'].append(f"{item['class']}.{item['api']}")
            
            # Process methods
            for item in results['methods']:
                tag = item['tag']
                tag_to_apis[tag]['methods'].append(item['api'])
            
            # Process events
            for item in results['events']:
                tag = item['tag']
                tag_to_apis[tag]['events'].append(f"{item['class']}.{item['api']}")
            
            # Process callbacks
            for item in results['callbacks']:
                tag = item['tag']
                tag_to_apis[tag]['callbacks'].append(item['api'])
        else:
            errors.append(yaml_file.name)
    
    # Generate report
    output_lines = []
    output_lines.append("=" * 80)
    output_lines.append("태그별 API 목록 (완전 재추출 - 최종 검증)")
    output_lines.append("=" * 80)
    output_lines.append(f"\n총 {files_processed}개 파일 처리 완료")
    if errors:
        output_lines.append(f"오류 발생 파일: {len(errors)}개")
    
    for tag in sorted(tag_to_apis.keys()):
        data = tag_to_apis[tag]
        output_lines.append("\n" + "=" * 80)
        output_lines.append(f"태그: {tag}")
        output_lines.append("=" * 80)
        
        # Classes
        if data['classes']:
            output_lines.append(f"\n[클래스] ({len(data['classes'])}개):")
            for cls in sorted(data['classes']):
                output_lines.append(f"  - {cls}")
        
        # Properties
        if data['properties']:
            output_lines.append(f"\n[프로퍼티] ({len(set(data['properties']))}개):")
            for prop in sorted(set(data['properties'])):
                output_lines.append(f"  - {prop}")
        
        # Methods
        if data['methods']:
            output_lines.append(f"\n[메서드] ({len(set(data['methods']))}개):")
            for method in sorted(set(data['methods'])):
                output_lines.append(f"  - {method}")
        
        # Events
        if data['events']:
            output_lines.append(f"\n[이벤트] ({len(set(data['events']))}개):")
            for event in sorted(set(data['events'])):
                output_lines.append(f"  - {event}")
        
        # Callbacks
        if data['callbacks']:
            output_lines.append(f"\n[콜백] ({len(set(data['callbacks']))}개):")
            for callback in sorted(set(data['callbacks'])):
                output_lines.append(f"  - {callback}")
        
        # Summary
        total = (len(data['classes']) + len(set(data['properties'])) + 
                len(set(data['methods'])) + len(set(data['events'])) + 
                len(set(data['callbacks'])))
        output_lines.append(f"\n총 {total}개 API")
    
    # Write to file
    output_text = '\n'.join(output_lines)
    with open('tags_api_list.txt', 'w', encoding='utf-8') as f:
        f.write(output_text)
    
    print(output_text)
    print(f"\n\n결과가 'tags_api_list.txt' 파일에 저장되었습니다.")
    
    # Verification
    print("\n" + "=" * 80)
    print("검증:")
    print("=" * 80)
    
    # Check Service tag
    service_classes = tag_to_apis['Service']['classes']
    print(f"\nService 태그: {len(service_classes)}개 클래스")
    expected_services = ['AdService', 'CollectionService', 'JointsService', 'FlagStandService']
    for svc in expected_services:
        if svc in service_classes:
            print(f"  [OK] {svc}")
        else:
            print(f"  [MISSING] {svc}")
    
    # Check Yields tag
    yields_methods = set(tag_to_apis['Yields']['methods'])
    print(f"\nYields 태그: {len(yields_methods)}개 메서드")
    expected_yields = ['WrapDeformer:CreateEditableMeshAsync', 'WrapDeformer:GetDeformedCFrameAsync']
    for method in expected_yields:
        if method in yields_methods:
            print(f"  [OK] {method}")
        else:
            print(f"  [MISSING] {method}")
    
    # Check CustomLuaState
    custom_lua_state_methods = set(tag_to_apis['CustomLuaState']['methods'])
    expected_methods = ['AnimationTrack:Play', 'AnimationTrack:AdjustSpeed', 
                       'AnimationTrack:AdjustWeight', 'AnimationTrack:Stop']
    print(f"\nCustomLuaState 태그: {len(custom_lua_state_methods)}개 메서드")
    for method in expected_methods:
        if method in custom_lua_state_methods:
            print(f"  [OK] {method}")
        else:
            print(f"  [MISSING] {method}")
    
    # Check PlayerReplicated
    player_replicated_classes = tag_to_apis['PlayerReplicated']['classes']
    print(f"\nPlayerReplicated 태그: {len(player_replicated_classes)}개 클래스")
    if 'PlayerGui' in player_replicated_classes:
        print(f"  [OK] PlayerGui")
    else:
        print(f"  [MISSING] PlayerGui")
    
    # Check CanYield
    can_yield_methods = set(tag_to_apis['CanYield']['methods'])
    print(f"\nCanYield 태그: {len(can_yield_methods)}개 메서드")
    if 'Instance:WaitForChild' in can_yield_methods:
        print(f"  [OK] Instance:WaitForChild")
    else:
        print(f"  [MISSING] Instance:WaitForChild")
    
    # Show tag counts
    print(f"\n\n태그별 통계:")
    for tag in sorted(tag_to_apis.keys()):
        data = tag_to_apis[tag]
        total = (len(data['classes']) + len(set(data['properties'])) + 
                len(set(data['methods'])) + len(set(data['events'])) + 
                len(set(data['callbacks'])))
        print(f"  {tag}: {total}개 API")

if __name__ == '__main__':
    main()

