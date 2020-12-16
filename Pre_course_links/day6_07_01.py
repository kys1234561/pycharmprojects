import xml.etree.cElementTree as et
#ElementTree表示元素数


tree = et.parse('movies.xml')#把文件movies.xml传进来，python会自动
# 封装成一棵树，此处赋给tree，
root = tree.getroot()#获取树的根节点
print(root.get('shelf'))#get是获取节点的内容（此时表示的是属性）

for movie in root.findall('movie'):
    title = movie.get('title')

    print(title)

    type = movie.find('type').text
    #获取标签内容，属性的子节点用find或者findall,如果要获取子节点的的内容，再用text