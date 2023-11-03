import os
import shutil


allowed_formats = ['.jpg', '.mp4']
sources = ['', '']
destination = ''
date_from = 2023091900000
date_to = 2023100100000


def _move_entry(entry: os.DirEntry[str], dest_dir: str, sfx: str) -> int:
    f_ext = entry.name[-4:].lower()
    if f_ext not in allowed_formats:
        print("{} is not a media file {} extension is not in the {}".format(
            entry.name, 
            f_ext, 
            allowed_formats))
        return 0
    
    entry_idx = entry.name[4:12] + entry.name[14:19]
    if not entry_idx.isnumeric():
        print("{} is not a numeric value".format(entry_idx))
        return 0
    
    if  date_from < int(entry_idx) < date_to:
        to_pth = dest_dir + entry_idx + sfx + f_ext
        print(to_pth)
        shutil.copyfile(entry.path, to_pth)
        return 1
    
    return 0


def _move_files(src: str, sfx: str):
    global destination
    with os.scandir(path=src) as dir_entries:
        counter = 0
        for entry in dir_entries:
            counter += _move_entry(entry, destination, sfx)

    print("{} files were moved".format(counter))


def main():
    global sources
    for i, filepath in enumerate(sources):
        _move_files(filepath, str(i))


if __name__ == "__main__":
    main()
