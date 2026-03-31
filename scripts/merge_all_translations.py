#!/usr/bin/env python3
"""
Merge all translation batches into the main script
"""

# Load existing translations from main script
exec_globals = {}
with open('add_kagga_translations.py', 'r', encoding='utf-8') as f:
    exec(f.read(), exec_globals)

all_translations = exec_globals['translations'].copy()
print(f"Starting with {len(all_translations)} translations from add_kagga_translations.py")

# Load batch 3
try:
    exec_globals_b3 = {}
    with open('add_kagga_translations_batch3.py', 'r', encoding='utf-8') as f:
        exec(f.read(), exec_globals_b3)
    batch3 = exec_globals_b3.get('additional_translations', {})
    all_translations.update(batch3)
    print(f"Added {len(batch3)} from batch 3, total now: {len(all_translations)}")
except Exception as e:
    print(f"Batch 3 error: {e}")

# Load batch 4
try:
    exec_globals_b4 = {}
    with open('add_more_translations_batch4.py', 'r', encoding='utf-8') as f:
        exec(f.read(), exec_globals_b4)
    batch4 = exec_globals_b4.get('batch4_translations', {})
    all_translations.update(batch4)
    print(f"Added {len(batch4)} from batch 4, total now: {len(all_translations)}")
except Exception as e:
    print(f"Batch 4 error: {e}")

# Load final batch
try:
    exec_globals_final = {}
    with open('final_batch_translations.py', 'r', encoding='utf-8') as f:
        exec(f.read(), exec_globals_final)
    final_batch = exec_globals_final.get('final_translations', {})
    all_translations.update(final_batch)
    print(f"Added {len(final_batch)} from final batch, total now: {len(all_translations)}")
except Exception as e:
    print(f"Final batch error: {e}")

print(f"\n=== FINAL COUNT: {len(all_translations)} translations ===")
print(f"Target: 216 stanzas")
print(f"Coverage: {len(all_translations)/216*100:.1f}%")

# Write the complete merged script
with open('add_kagga_translations.py', 'w', encoding='utf-8') as f:
    f.write('''#!/usr/bin/env python3
"""
Script to add English translations to Mankuthimmana Kagga
Creates a two-column layout with Kannada on left, English on right
"""

# Translations dictionary
translations = {
''')

    for k in sorted(all_translations.keys()):
        v = all_translations[k]
        f.write(f'    {k}: """{v}""",\n')

    f.write('''}\n
def read_file_in_chunks(filepath, chunk_size=1000):
    """Read large file in chunks"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def extract_stanza_number(text):
    """Extract stanza number from Kannada text like ॥ ೧ ॥"""
    import re
    match = re.search(r'॥\\s*(\\d+)\\s*॥', text)
    if match:
        # Convert Kannada numerals to regular numbers
        kannada_nums = {'೧': '1', '೨': '2', '೩': '3', '೪': '4', '೫': '5',
                       '೬': '6', '೭': '7', '೮': '8', '೯': '9', '೦': '0'}
        num_str = match.group(1)
        for k, v in kannada_nums.items():
            num_str = num_str.replace(k, v)
        try:
            return int(num_str)
        except:
            return None
    return None

def process_kagga_file(input_file, output_file):
    """Process the Kagga file and add English translations"""
    lines = read_file_in_chunks(input_file)

    output_lines = []
    current_stanza = []
    stanza_num = None

    # Copy header
    output_lines.append(lines[0])  # Title
    output_lines.append(lines[1])  # Slug
    output_lines.append(lines[2])  # Template
    output_lines.append(lines[3])  # Blank line
    output_lines.append(lines[4])  # ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ title
    output_lines.append('\\n')

    for i, line in enumerate(lines[5:], start=5):
        # Skip blank lines between stanzas
        if line.strip() == '':
            if current_stanza:
                # Process the completed stanza
                stanza_text = ''.join(current_stanza)
                num = extract_stanza_number(stanza_text)

                if num and num in translations:
                    # Create two-column HTML structure
                    output_lines.append('<div class="poetry-stanza">\\n')
                    output_lines.append('<div class="poetry-kannada">\\n')
                    output_lines.append(stanza_text)
                    output_lines.append('</div>\\n')
                    output_lines.append('<div class="poetry-english">\\n')
                    output_lines.append(translations[num] + '\\n')
                    output_lines.append('</div>\\n')
                    output_lines.append('</div>\\n\\n')
                else:
                    # No translation available yet, keep original format
                    output_lines.append(stanza_text)
                    output_lines.append('\\n')

                current_stanza = []
            continue

        current_stanza.append(line)

    # Don't forget last stanza
    if current_stanza:
        stanza_text = ''.join(current_stanza)
        num = extract_stanza_number(stanza_text)
        if num and num in translations:
            output_lines.append('<div class="poetry-stanza">\\n')
            output_lines.append('<div class="poetry-kannada">\\n')
            output_lines.append(stanza_text)
            output_lines.append('</div>\\n')
            output_lines.append('<div class="poetry-english">\\n')
            output_lines.append(translations[num] + '\\n')
            output_lines.append('</div>\\n')
            output_lines.append('</div>\\n\\n')
        else:
            output_lines.append(stanza_text)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"Processed {len(translations)} stanzas with English translations")
    print(f"Output written to {output_file}")

if __name__ == '__main__':
    input_file = 'content/pages/about/ಕಗ್ಗ.md'
    output_file = 'content/pages/about/ಕಗ್ಗ_new.md'

    process_kagga_file(input_file, output_file)
    print("\\nNext steps:")
    print("1. Review the output file")
    print("2. If satisfied, replace the original:")
    print(f"   mv {output_file} {input_file}")
    print("3. Run: pelican content")
''')

print("\n✓ Successfully wrote merged add_kagga_translations.py")
print(f"  Total translations: {len(all_translations)}")
