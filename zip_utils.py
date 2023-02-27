import zipfile


def zip_to_binary_file(zip_file: str):
    with zipfile.ZipFile(zip_file, 'r') as zip_file:
        file_data = {}
        for name in zip_file.namelist():
            with zip_file.open(name, 'r') as file:
                data = file.read()
                binary_string = ''.join(['{0:b}'.format(x).zfill(8) for x in data])
                file_data[name] = binary_string

    # Save the binary data to a file
    with open('file.bin', 'w') as file:
        for name, data in file_data.items():
            binary_name = ''.join([format(ord(c), '08b') for c in name])
            constant = ''.join([format(ord(c), '08b') for c in 'ajdlksjdajspdajsdkjsakld@jlkadknlf'])
            file.write(binary_name + constant)
            file.write(data + constant)


def binary_to_zip(restore_zip: str):
    with open("file.bin", 'r') as file:
        file_contents = file.read()
        constant = ''.join([format(ord(c), '08b') for c in 'ajdlksjdajspdajsdkjsakld@jlkadknlf'])
        x = file_contents.split(constant)
        file_dicts = {}
        new_list = [x for x in x if x != '']
        for i in range(0, len(new_list), 2):
            chunks = [new_list[i][z:z + 8] for z in range(0, len(new_list[i]), 8)]
            file_name = ''.join([chr(int(chunk, 2)) for chunk in chunks])
            key = file_name
            value = bytearray([int(new_list[i + 1][x:x + 8], 2) for x in range(0, len(new_list[i + 1]), 8)])
            file_dicts[key] = value

        with zipfile.ZipFile(f'{restore_zip}.zip', 'w') as zip_file:
            for name, data in file_dicts.items():
                zip_file.writestr(name, data)


zip_to_binary_file('/home/akmal/Downloads/Afrin_cv.zip')
# binary_to_zip("file")
