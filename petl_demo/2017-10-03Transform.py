# coding:utf8

import petl as etl

table1 = [('foo', 'bar', 'baz'),
          ('apple', 1, 2.5), ('orange', 3, 4.5), ('pears', 5, 6.5),
          ('bananer', 7, 8.5), ('cat', 9, 10.5)]
# head 4
table_head = etl.head(table1, 4)
print(table_head)

# tail 4
table_tail = etl.tail(table1, 4)
print(table_tail)

# rowslice
rowsliceTb = etl.rowslice(table1, 2)
print(rowsliceTb)

rowsliceTb_2_4 = etl.rowslice(table1, 2, 4)
print(rowsliceTb_2_4)

# 从1开始，2作为第一个，步长为2，
rowsliceTb_1_2_5 = etl.rowslice(table1, 1, 5, 2)
print(rowsliceTb_1_2_5)

# cut
cutTb = etl.cut(table1, 'foo', 'bar')
print(cutTb)

# index starts from 0
cutTb_0_2 = etl.cut(table1, 0, 2)
print(cutTb_0_2)

# filename and index used mixed
cutTb_name_index = etl.cut(table1, 'foo', 0)
print(cutTb_name_index)

# select a range of fields
# 区间选择针对列上的索引 0 =< index <2
cutTb_select_range = etl.cut(table1, *range(0, 2))
print(cutTb_select_range)


