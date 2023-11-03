import os
import shutil
import json
import time


cfg = {}


def _move_entry(entry: os.DirEntry[str], dest_dir: str, sfx: str) -> int:
    f_ext = entry.name[-4:].lower()
    if f_ext not in cfg['allowed_formats']:
        print("{} is not a media file {} extension is not in the {}".format(
            entry.name, 
            f_ext, 
            cfg['allowed_formats']))
        return 0
    
    entry_idx = entry.name[4:12] + entry.name[14:19]
    if not entry_idx.isnumeric():
        print("{} is not a numeric value".format(entry_idx))
        return 0
    
    if  cfg['date_from'] < int(entry_idx) < cfg['date_to']:
        to_pth = dest_dir + entry_idx + sfx + f_ext
        print(to_pth)
        shutil.copyfile(entry.path, to_pth)
        return 1
    
    return 0


def _move_files(src: str, sfx: str):
    with os.scandir(path=src) as dir_entries:
        counter = 0
        for entry in dir_entries:
            counter += _move_entry(entry, cfg['destination'], sfx)

    print("{} files were moved".format(counter))


def _read_cfg(pth: str):
    global cfg
    with open(pth) as cfg_file:
        cfg = json.loads(cfg_file.read())


def main():
    _read_cfg('./data/move_data.json')
    for i, filepath in enumerate(cfg['sources']):
        _move_files(filepath, str(i))



if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Elapsed time: {}".format(time.time() - start_time)) 
