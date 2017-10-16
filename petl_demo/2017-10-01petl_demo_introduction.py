# coding:utf8
# introduction
example_data = """foo,bar,baz
a,1,2.3
b,4,5.6
c,7,8.9
"""
with open('example.csv', 'w') as f:
    f.write(example_data)

import petl as etl

table1 = etl.fromcsv('example.csv')
print(table1)
table2 = etl.convert(table1, 'foo', 'upper')
print(table2)
table3 = etl.convert(table2, {'bar': int, 'baz': float})
print(table3)
table4 = etl.addfield(table3, 'bar*baz', lambda row: row.baz * row.bar)
print(table4.look())

# 管道操作
table=(
    etl
    .fromcsv('example.csv')
    .convert({'foo':'upper','bar':int,'baz':float})
    .addfield('bar*bar_new',lambda r:r.baz* r.bar)
    .convert('baz', lambda v, row: v * float(row.bar),pass_row=True)
)
print(table.look())

