import sys
 
n = len(sys.argv)
TEST = True
filename = "example"
if n > 1:
    TEST = False
    filename = "input"

f = open(filename, "r")


def get_cur_dir(cur_line, splitting):
    return cur_line.split(splitting)[1][:-1]


cur_dir_ls = ''
infos = dict()
infos['least_than_100000'] = 0


for line in f.readlines():
    if line.startswith('$ cd'):
        new_dir = get_cur_dir(line, 'cd ')
        if new_dir == '/':
            cur_dir_ls = '/'
        elif new_dir == '..':
            cur_dir_ls = '/'.join(cur_dir_ls.split('/')[:-2]) + '/'
        else:
            cur_dir_ls = cur_dir_ls + new_dir + '/'
        if cur_dir_ls not in infos:
            infos[cur_dir_ls] = []
    elif line.startswith('$ ls'):
        # LS
        pass
    elif line.startswith('dir'):
        dir_name = get_cur_dir(line, 'dir ')
        cur_dir = cur_dir_ls + dir_name
        infos[cur_dir_ls].append(dict(type='dir', filename=dir_name, size=0))
    else:
        size, filename = line.split(' ')
        infos[cur_dir_ls].append(dict(type='file', size=int(size), filename=filename[:-1]))
       

def insert_data(list_of_dir, infos, _file, root):
    size = _file['size']
    if _file['type'] == 'dir':
        new_root = root + _file['filename'] + '/'
        _file['data'] = infos[new_root]
        for subfile in infos[new_root]:
           size += insert_data(list_of_dir, infos, subfile, root=new_root)
        _file['size'] = size
        list_of_dir.append(dict(name=new_root, size=size))
        if size < 100000:
            infos['least_than_100000'] += size
           
    return size


list_of_dir = []
size_root = 0
for _file in infos['/']:
    size_root += insert_data(list_of_dir, infos, _file, root='/')
    
print('TOTAL', infos['least_than_100000'])
