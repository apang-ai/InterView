'''
data = [
    {"id": 4, "name": "name4", "pid": 1},
    {"id": 1, "name": "name1", "pid": 0},
    {"id": 2, "name": "name2", "pid": 0},
    {"id": 3, "name": "name3", "pid": 0},
    {"id": 5, "name": "name4", "pid": 2},
    {"id": 6, "name": "name5", "pid": 2},
    {"id": 7, "name": "name6", "pid": 4},
]
data = [
    (1, 4),
    (0, 1),
    (0, 2),
    (0, 3),
    (2, 5),
    (2, 6),
    (4, 7),
]
                           0
                         / | \
                        1  2  3
                       /  / \
                      4  5   6
                     /
                    7
数据转换：
result = [
    {
        'id': 1, 'pid': 0, 'name': 'name1',
        'children': [
            {'id': 4, 'pid': 1, 'name': 'name4',
             'children': [{'id': 7, 'pid': 4, 'name': 'name6', 'children': []}]
             }
        ]
    },
    {
        'id': 2, 'pid': 0, 'name': 'name2',
        'children': [
            {'id': 5, 'pid': 2, 'name': 'name4', 'children': []},
            {'id': 6, 'pid': 2, 'name': 'name5', 'children': []}
        ]
    },
    {
        'id': 3, 'pid': 0, 'name': 'name3', 'children': []
    }
]

'''

def DB(data):
    # 存放新数据结构的列表
    result = []
    for i in data:
        i['childrent'] = []
        pid = i['pid']
        
        position = 0
        if pid == position:

            result.append(i)

    # 如果result中的 id 和 data中的 pid 相等，就把data中的pid的数据加入result的childrent中
    reslute_len = len(result)
    data_len = len(data)
    for i in range(reslute_len):
        for j in range(data_len):
            
            if result[i]['id'] == data[j]['pid']:
                result[i]['childrent'].append(data[j])

        childrent_len = len(result[i]['childrent'])
        for t in range(childrent_len):

            for x in range(data_len):

                if result[i]['childrent'][t]['id'] == data[x]['pid']:
                    result[i]['childrent'][t]['childrent'].append(data[x])

    return result




data = [
    {"id": 4, "name": "name4", "pid": 1},
    {"id": 1, "name": "name1", "pid": 0},
    {"id": 2, "name": "name2", "pid": 0},
    {"id": 3, "name": "name3", "pid": 0},
    {"id": 5, "name": "name4", "pid": 2},
    {"id": 6, "name": "name5", "pid": 2},
    {"id": 7, "name": "name6", "pid": 4},
]
d = DB(data)

print(d)
