from pathlib import Path
import shutil
import types_files as tf

from pathlib import Path
import shutil

def replaceFile(_function, _folder_in, _folder_out, _type_file, _expansion_file):
    folder_in_path = Path(_folder_in)
    folder_out_path = Path(_folder_out)

    folder_out_path.mkdir(parents=True, exist_ok=True)

    for file in folder_in_path.iterdir():
        if not file.is_file():
            continue

        if file.suffix in _expansion_file:
            try:
                shutil.move(str(file), str(folder_out_path / file.name))
                _function(f"✅ Перемещён: {file.name}")
            except PermissionError:
                _function(f"⚠️ Не перемещено (занят другим процессом): {file.name}")
            except OSError as e:
                _function(f"⚠️ Системная ошибка: {e}")

    _function("\n✅ Готово!")