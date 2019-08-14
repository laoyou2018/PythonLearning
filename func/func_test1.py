# 上下文

fd = open('name.tex')

try:
    for line in fd:
        print(line)
finally:
    fd.close()

# 在这种情况下如果失败会自动执行 finally的关闭操作 这就是所谓的上下文吧
# 在类 完成后 在详细介绍
with open('name.tex') as f:
    for line in f:
        print(line)