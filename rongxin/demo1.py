# -*- coding: UTF-8 -*-
import json
list1 = [1,2,3,9,0,-1,-2]

def get_value(list1):
    zhengshu = 0
    fushu = 0
    for i in list1:
        if i>0:
            zhengshu+=1
            # print("zhengshu %s" %zhengshu)
        elif i<0:
            fushu += 1
            # print("fushu %s" % fushu)
        else:
            print(i)
    print(zhengshu)
    print(fushu)
    return zhengshu,fushu

print(get_value(list1))

str1 = 'axbyczdj'
print(str1[::2])

str2 = 'hello_world_yoyo'
print(str2.split('_'))
a=1
a='000'+str(a)
print(a)

 b=[1,3,5,7]
b[0],b[1],b[2]=b[1],b[2],b[0]

print(b)

c={"name":"json"}
print(json.dumps(c))
print(type(json.dumps(c)))

#requests发送post请求的方式
'''
form requests.post(url,data=data)
json requests,post(url,json=data, headers=header)
mulitpart requests,post(url,files=files)
'''

'''
requests模块发送请求有data、json、params三种携带参数的方法。
params在get请求中使用，data、json在post请求中使用。
'''

'''
json的key只能是字符串，python的dict可以是任何可hash对象（hashtable type）；
json的key可以是有序、重复的；dict的key不可以重复。
json的value只能是字符串、浮点数、布尔值或者null，或者它们构成的数组或者对象。
json的字符串强制双引号，dict字符串可以单引号、双引号；
dict可以嵌套tuple，json里只有数组。
json:true、false、null；python：True、False、None
json的类型是字符串，字典的类型是字典。
'''

'''
元素定位+异常捕获
'''

'''
把登陆的token数据保存至json，利用jsonpath模块进行提取token ,把token作为类属性，其他接口获取
'''

'''
import pymysql
# 插入语句
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="root", database="python",charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 执行sql语句，插入多条数据
cursor.executemany("insert into test(id, name, score) values (%s,%s,%s)", data)
# 提交数据
db.commit()
# 发生错误时回滚
db.rollback()
# 关闭数据库连接
db.close()
'''

'''
创建类，定义一个类属性，定义为空，提取接口的返回值，通过setattar()方法存储到类属性里，下一个接口调用时，通过getattar()方法获取类属性的值'''

'''
1、手机操作系统：
Android较多，Ios较少且不能降级，只能单向升级。
2、多分辨率测试：
Android端有20多种，而Ios较少。
3、按键：Android一般有3个按键，而Ios只有一个home键。
①Android长按home键呼出应用列表和切换应用，然后右滑则终止应用。
Back键在大部分情况下和页面上的返回键功能一样，不过还要看Back键是否被重写，测试Back键的反馈是否正确，可以在应用间切换，还可以返回主屏幕。
②Ios单击home键返回主界面，双击回到单手操作模式。
4、push测试（推送测试）：
①Android：点击home键，程序后台运行时，此时接收到push，点击后唤醒应用，查看此时是否可以正常跳转。
②Ios：点击home键关闭程序；屏幕锁屏时的情况（红点的显示）。
5、安装和卸载测试：
Android的下载、安装的平台和工具，平台比较多。
Ios主要有App store，iTunes，testflight下载。
6、升级测试：
可以被级的必要条件：新旧版本具有相同的签名、具有相同的包名、有一个标识符区分新旧版本（如版本号）。
7、分享跳转：
分享后的文案是否正确、分享后跳转是否正确、显示的消息来源是否正确。
8、触屏测试：
同时触摸不同的位置或同时进行不同的操作，查看客户端的处理情况，比如，是否会crash等。
'''

'''
1.内存管理错误：可能是可用内存过低，app所需的内存超过设备的限制，app跑步起来导致app crash。或是内存泄漏，程序运行的时间越长，所占用的内存越大，最终用尽全部内存，导致整个系统崩溃。亦或是非授权的内存位置的使用也可能导致app crash
2.程序逻辑错误：数组越界，堆栈溢出，并发操作，逻辑错误。e.g.app新添加一个为经测试的新功能，调用了一个已释放的指针，运行的时候就会crash
3.设备兼容：由于设备多样性，app在不同的设备上可能会有不同的表现
4.网络原因：可能是网速欠佳，无法达到app所需的快速响应时间，导致app crash。或者是不同网络的切换也可能会影响app的稳定性
'''


'''
1.功能方面：
在流程和功能测试上是没有区别的，系统测试和一些细节可能会不一样。那么我们就要先来了解，web和app的区别：
web项目，一般都是b/s架构，基于浏览器的，而app则是c/s的，必须要有客户端。在系统测试的时候就会产生区别了。
首先从系统架构来看的话，web测试只要更新了服务器端，客户端就会同步会更新。而且客户端是可以保证每一个用户的客户端完全一致的。但是app端是不能够保证完全一致的，除非用户更新客户端。如果是app下修改了服务端，意味着客户端用户所使用的核心版本都需要进行回归测试一遍。
2.性能方面:
web页面可能只会关注响应时间，而app则还需要关心流量、电量、CPU、GPU、Memory这些了。
3.兼容性方面:
web是基于浏览器的，所以更倾向于浏览器和电脑硬件，电脑系统的方向的兼容，不过一般还是以浏览器的为主。而浏览器的兼容则是一般是选择不同的浏览器内核进行测试（IE、chrome、Firefox）。app的测试则必须依赖phone或者是pad，不仅要看分辨率，屏幕尺寸，还要看设备系统。系统总的来说也就分为Android和iOS，不过国内的Android的定制系统太多，也是比较容易出现问题的。
4.相比较web测试，app更是多了一些专项测试：
　　一些异常场景的考虑以及弱网络测试。这里的异常场景就是中断，来电，短信，关机，重启等。
　　而弱网测试是app测试中必须执行的一项测试。包含弱网和网络切换测试。需要测试弱网所造成的用户体验，重点要考虑回退和刷新是否会造成二次提交。需要测试丢包，延时的处理机制。避免用户的流失。这些在前面的弱网测试那篇已经讲过，这里不再讲了。
5.安装、卸载、更新：
　　web测试是基于浏览器的所以不必考虑这些。而app是客户端的，则必须测试安装、更新、卸载。除了常规的安装、更新、卸载还要考虑到异常场景。包括安装时的中断、弱网、安装后删除安装文件，更新的强制更新与非强制更新、增量包更新、断点续传、弱网，卸载后删除app相关的文件等等。这里讲起来的话太多了，如果有疑问的同学可以评论或者给我留言。
6.界面操作：
　　app产品的用户都是使用的触摸屏手机，所以测试的时候还要注意手势，横竖屏切换，多点触控，事件触发区域等测试。
'''


# def get_max_same_string(a):
#     for i in a:
#         if

def commonChars(A):
# “”"
# 该函数主要识别list中各元素相同的字符
# :param A: 给定的list
# :return: common_chars:相同字符的列表
# “”"
    lenth_li = len(A)
    lenth_li0 = len(A[0])
    common_li = []
##方式一：通过遍历list中第一个元素每一个字符的方式
# 遍历第一个列表元素得每一个元素
    for x in range(0,lenth_li0):
        element = A[0][x]
        i = 1
# #将列表中每一元素与列表中没有元素进行比对
    for y in range(1,lenth_li):
# #具体比对列表中每一个元素中每一个字符
        for y1 in range(0,len(A[y])):
            if element == A[y][y1]:
                i += 1
            if i == lenth_li:
                common_li.append(A[y][y1])
                A[y] = A[y][:y1] + A[y][y1 + 1:]
                break
            else:
                continue
    return common_li

A=['hello','hehe']
print(commonChars(A))
