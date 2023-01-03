import sys
from task_6_4 import prepare_dataset

if len(sys.argv) > 4:
    raise TypeError (f'prepare_dataset() takes 3 positional arguments but {len(sys.argv[1:])} was given')
elif len(sys.argv) < 4:
    if len(sys.argv) == 1:
        raise TypeError(f"prepare_dataset() missing 3 required positional arguments: 'path_users_file', 'path_hobby_file' and 'path_out_file'")
    elif len(sys.argv) == 2:
        raise TypeError(f"prepare_dataset() missing 2 required positional arguments: 'path_hobby_file' and 'path_out_file'")
    elif len(sys.argv) == 3:
        raise TypeError(f"prepare_dataset() missing 1 required positional arguments: 'path_out_file'")
else:
    users_file, hobbies_file, out_file = sys.argv[1:]
    prepare_dataset(users_file, hobbies_file, out_file)