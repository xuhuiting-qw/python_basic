import os
import shutil

# 1、os.mkdir(path) : 创建单级目录（如果目录已经存在，则会抛出异常）
# os.mkdir('F:/demo')

# 2、os.makedirs(path) : 创建多级目录(如果路径中的所有目录都已经存在，则会抛出异常)
# os.makedirs('F:/demo/aa/bb')

# 3、os.rmdir(path) : 删除空目录（如果目录不存在，或者目录非空，都会抛出异常）
# os.rmdir('F:/demo/aa/bb')

# 4、os.removedirs(path) : 递归删除空目录，在成功删除末尾一级目录后，会向上尝试把父级目录也删除（直到父级目录不是空目录）
# os.removedirs('F:/demo/aa')

# 5、os.path.exists(path) : 判断路径是否存在(文件/目录都算)
# print(os.path.exists('F:/demo'))

# 6、os.path.isdir(path): 用于判断路径，具体规则如下
#       1、路径不存在                 返回False
#       2、路径存在，但指向的是文件      返回False
#       3、路径存在，并且是目录         返回True
# print(os.path.isdir('F:/demo'))

# 7、os.path.isfile(path): 判断是否为文件
# print(os.path.isfile('F:/demo/hello'))

# 8、os.scandir(path): 扫描指定目录
# result = os.scandir('F:/demo')
# for item in result:
#     print('目录：' if item.is_dir() else '文件：', item.name, item.path)

# 9、os.walk(path): 按层级，递归地遍历指定目录下，所有的子目录和文件
# result = os.walk('F:/demo')
# for item in result:
#     print(item)

# 10、危险操作：删除有内容的目录
shutil.rmtree('F:/demo/cc')