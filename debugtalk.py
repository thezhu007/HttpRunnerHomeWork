import faker,pymysql
def setup_hook_testcase(casename):
    print("----------%s测试用例执行开始----------"%casename)

def teardown_hook_testcase(casename):
    print("----------%s测试用例执行结束----------"%casename)

def creat_tags():
    return ["new_04","new_05","new_06"]

def get_faker_name(count):
    name_obj = faker.Faker(locale='zh_CN')
    name_list = []
    for i in range(count):
        name_list.append(name_obj.name())
    return name_list

# 3、使用pymysql把mysqk数据库的数据进行查询读取出去
def get_mysql_data():
    mysql_obj = pymysql.connect(host='172.102.16.33',port= 3306,user='root',password='0018$0018bB',database='ysld',charset='utf8')
    cursor_obj = mysql_obj.cursor()
    cursor_obj.execute('select * from bscorganization limit 10')
    data = cursor_obj.fetchall()
    cursor_obj.close()
    mysql_obj.close()
    return data

if __name__ == '__main__':
    print(get_mysql_data())

