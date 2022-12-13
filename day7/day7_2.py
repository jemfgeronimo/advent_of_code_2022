class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0

    def add_size(self, num):
        self.size += num
        if self.parent != None:
            self.parent.add_size(num)

    def delete_size(self, num):
        self.size -= num
        if self.parent != None:
            self.parent.delete_size(num)

def get_size(dir):
    return dir.size

f = open("input.txt")
index = 0
dirs_list = [] # list of objects
#obj_dirs_list = []
for line in f:
    line_split = line.split()
    print("line_split: ", line_split)

    if line_split[0] == "$":
        if line_split[1] == "cd":
            if line_split[2] == "..": # $ cd ..
                curr_dir = curr_dir.parent
            else: # $ cd dir_name
                if line_split[2] == "/":
                    curr_dir = Directory("/", None)
                else:
                    curr_dir = Directory(line_split[2], curr_dir)
                dirs_list.append(curr_dir)
            print("curr_dir: ", curr_dir.name)
        else: # ls
            pass
    elif line_split[0] != "dir":    # size
        print("line_split[0]: ", line_split[0])
        curr_dir.add_size(int(line_split[0]))
    else:
        pass

f.close()
#sum = 0
dirs_list.sort(key=get_size)
for dir in dirs_list:
    #if dir.size <= 100000:
    #    sum += dir.size
    if dir.name != "/":
        print("dir.name: ", dir.name, " \tsize: ", dir.size, " \tparent_dir: ", dir.parent.name)
    else:
        print("dir.name: ", dir.name, " \tsize: ", dir.size, " \tparent_dir: ", None)
    temp_size = dir.size
    dir.delete_size(temp_size)
    if dirs_list[-1].size <= 40000000:
        break
    else:
        dir.add_size(temp_size)
#print("dirs_list: ", dirs_list)
# sort muna todo
#print("sum: ", sum)
main_dir = dirs_list[-1]
print("main_dir: ", main_dir.name, " \tsize: ", main_dir.size)