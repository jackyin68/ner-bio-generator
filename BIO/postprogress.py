# bio data correction  for nre, KG

import re

# bio correction config
correct_dict = {
    '方 O\n方 O': '方 B-PER\n方 E-PER',
    '汪 O\n芳 O': '汪 B-PER\n芳 E-PER'
}


def correction_bio(bio_file_path, bio_cor_file_path):
    bio_file = open(bio_file_path, "r")
    lines = bio_file.readlines()
    bio_file.close()

    bio_cor_file = open(bio_cor_file_path, "w")
    lines = "".join(lines)
    for key, value in correct_dict.items():
        lines = re.sub(str(key), str(value), str(lines), count=0, flags=0)
    bio_cor_file.write(lines)
    bio_cor_file.write('\n')
    bio_cor_file.close()
