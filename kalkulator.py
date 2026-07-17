import sys

def analyze_diff(diff_content):
    if not diff_content.strip():
        return "Error: No diff content provided."
    
    lines = diff_content.split('\n')
    added_lines = 0
    removed_lines = 0
    files_changed = 0
    
    for line in lines:
        if line.startswith('+++ b/'):
            files_changed += 1
        elif line.startswith('+') and not line.startswith('+++'):
            added_lines += 1
        elif line.startswith('-') and not line.startswith('---'):
            removed_lines += 1
            
    return {
        "files_changed": files_changed,
        "added_lines": added_lines,
        "removed_lines": removed_lines
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"File {sys.argv[1]} tidak ditemukan.")
            sys.exit(1)
    else:
        print("Masukkan text diff Anda (tekan Ctrl+D/Ctrl+Z setelah selesai):")
        content = sys.stdin.read()
        
    result = analyze_diff(content)
    if isinstance(result, dict):
        print(f"\nHasil Analisis Diff:\n- File diubah: {result['files_changed']}\n- Baris ditambah: {result['added_lines']}\n- Baris dihapus: {result['removed_lines']}")
    else:
        print(result)