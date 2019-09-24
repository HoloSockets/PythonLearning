# -*- coding:utf-8 -*-


def welcome_Python(member_name, hope):
    # 定义带参数的函数
    print('你好，%s，欢迎加入Python实战圈' % member_name)
    print('\t%s' % hope)


def employee(first_name, last_name, **employee_infor):
    '''传递字典：存储员工信息'''
    employee = {}
    employee['first_name'] = first_name
    employee['last_name'] = last_name

    for key, value in employee_infor.items():
        employee[key] = value

    return employee


welcome_Python('kim', '希望你能坚持下去。')
welcome_Python('Grace', '希望你可以找到想要的。')

my_employee = employee('德华', '刘', location='香港', dep='大数据')
print('员工的信息如下：')
for key, value in my_employee.items():
    print('\t' + key + ":" + value + '\n')
