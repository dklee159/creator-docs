import os
import re
from collections import defaultdict
from pathlib import Path

def extract_tags_from_block(lines, start_idx):
    """Extract tags from a tags: block starting at start_idx"""
    tags = []
    if start_idx >= len(lines):
        return tags
    
    line = lines[start_idx]
    stripped = line.strip()
    
    # Check for inline format: tags: [Tag1, Tag2]
    inline_match = re.search(r'tags:\s*\[([^\]]+)\]', line)
    if inline_match:
        tags_str = inline_match.group(1)
        tag_items = [t.strip().strip('"\'') for t in tags_str.split(',') if t.strip()]
        return tag_items
    
    # Check for empty: tags: []
    if '[]' in stripped:
        return []
    
    # Multi-line format: extract tags from following lines
    base_indent = len(line) - len(line.lstrip())
    i = start_idx + 1
    
    while i < len(lines):
        next_line = lines[i]
        next_stripped = next_line.strip()
        next_indent = len(next_line) - len(next_line.lstrip())
        
        # Stop if we hit a line with same or less indent (not part of tags block)
        if next_stripped and next_indent <= base_indent:
            break
        
        # Extract tag from list item
        if next_stripped.startswith('-'):
            tag_match = re.search(r'-\s*(\w+)', next_line)
            if tag_match:
                tag = tag_match.group(1).strip()
                if tag:
                    tags.append(tag)
        elif next_stripped and not next_stripped.startswith('#'):
            # Non-empty line that's not a tag item
            if next_indent <= base_indent:
                break
        
        i += 1
    
    return tags

def extract_tags_with_apis_from_yaml(file_path):
    """Extract all tags with their associated APIs from a YAML file"""
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
        
        # Extract class name
        for line in lines:
            if line.startswith('name:') and not class_name:
                class_name = line.split('name:')[1].strip()
                break
        
        if not class_name:
            return None, results
        
        # Find class-level tags
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('tags:') and 'properties:' not in ''.join(lines[:i]):
                tags = extract_tags_from_block(lines, i)
                if tags:
                    for tag in tags:
                        results['class'].append({
                            'tag': tag,
                            'api': class_name,
                            'type': 'class'
                        })
                break
        
        # Process properties, methods, events, callbacks
        current_section = None
        item_name = None
        item_start = -1
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            indent = len(line) - len(line.lstrip())
            
            # Detect section headers
            if stripped == 'properties:':
                current_section = 'properties'
                item_name = None
            elif stripped == 'methods:':
                current_section = 'methods'
                item_name = None
            elif stripped == 'events:':
                current_section = 'events'
                item_name = None
            elif stripped == 'callbacks:':
                current_section = 'callbacks'
                item_name = None
            
            # Find item name
            if current_section and stripped.startswith('name:'):
                item_name = stripped.split('name:')[1].strip()
                item_start = i
            
            # Find tags for current item
            if current_section and item_name and 'tags:' in stripped:
                # Check if this tags: belongs to the current item
                # It should be at the same or greater indent level as the item
                if item_start >= 0:
                    item_indent = len(lines[item_start]) - len(lines[item_start].lstrip())
                    # Tags should be at same indent level (part of same item)
                    if indent >= item_indent:
                        tags = extract_tags_from_block(lines, i)
                        if tags:
                            api_type = current_section[:-1] if current_section.endswith('s') else current_section
                            for tag in tags:
                                results[current_section].append({
                                    'tag': tag,
                                    'api': item_name,
                                    'type': api_type
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
    
    # Structure: tag -> type -> list of APIs
    tag_apis = defaultdict(lambda: defaultdict(list))
    
    files_processed = 0
    
    # Process all YAML files
    for yaml_file in sorted(classes_dir.glob('*.yaml')):
        files_processed += 1
        class_name, results = extract_tags_with_apis_from_yaml(yaml_file)
        
        if class_name:
            # Process class-level tags
            for item in results['class']:
                tag_apis[item['tag']][item['type']].append(item['api'])
            
            # Process property tags
            for item in results['properties']:
                tag_apis[item['tag']][item['type']].append(item['api'])
            
            # Process method tags
            for item in results['methods']:
                tag_apis[item['tag']][item['type']].append(item['api'])
            
            # Process event tags
            for item in results['events']:
                tag_apis[item['tag']][item['type']].append(item['api'])
            
            # Process callback tags
            for item in results['callbacks']:
                tag_apis[item['tag']][item['type']].append(item['api'])
    
    # Print results
    print(f"Total files processed: {files_processed}\n")
    print("=" * 80)
    print("Tags별 API 정리")
    print("=" * 80)
    
    # Save to file
    with open('tags_with_apis.txt', 'w', encoding='utf-8') as f:
        f.write("Tags별 API 정리\n")
        f.write("=" * 80 + "\n\n")
        
        for tag in sorted(tag_apis.keys()):
            print(f"\n[{tag}]")
            print("-" * 80)
            f.write(f"\n[{tag}]\n")
            f.write("-" * 80 + "\n")
            
            total_count = 0
            for api_type in ['class', 'property', 'method', 'event', 'callback']:
                if api_type in tag_apis[tag]:
                    apis = sorted(set(tag_apis[tag][api_type]))
                    count = len(apis)
                    total_count += count
                    
                    print(f"\n  {api_type.upper()} ({count}개):")
                    f.write(f"\n  {api_type.upper()} ({count}개):\n")
                    
                    for api in apis:
                        print(f"    - {api}")
                        f.write(f"    - {api}\n")
            
            if total_count > 0:
                print(f"\n  총 {total_count}개 API")
                f.write(f"\n  총 {total_count}개 API\n")
            else:
                print(f"\n  (태그가 발견되지 않음)")
                f.write(f"\n  (태그가 발견되지 않음)\n")
    
    print(f"\n\n결과가 tags_with_apis.txt 파일에 저장되었습니다.")

if __name__ == '__main__':
    main()
