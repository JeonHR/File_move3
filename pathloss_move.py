import os
import shutil
from pathlib import Path

def copy_site_files(site_count=16, base_filename="pathloss_r2_BAZB_site", file_ext=".txt"):
    base_dir = Path.cwd()

    for i in range(1, site_count + 1):
        site_folder = base_dir / f"site{i}"
        site_folder.mkdir(exist_ok=True)

        src_file = base_dir / f"{base_filename}{i}{file_ext}"
        dst_file = site_folder / f"site{i}{file_ext}"

        if src_file.exists():
            shutil.copy2(src_file, dst_file)
            print(f"✅ Copied {src_file.name} → {dst_file}")
        else:
            print(f"⚠️ Source file not found: {src_file}")

if __name__ == "__main__":
    copy_site_files()
