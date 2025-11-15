import  time
# 功能计时
# 定义一个普通通用装饰器
def out_fn(fn):

    def inner_fn(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result
    return inner_fn



# 定义一个带有参数的装饰器
def timeout(ro):
    def out_fn(fn):
        def inner_fn(*args, **kwargs):
            start_time = time.time()
            result = fn(*args, **kwargs)
            end_time = time.time()
            print(round(end_time - start_time,ro))
            return result
        return inner_fn
    return out_fn


@out_fn
# 定义一个普通函数
def add(a, b):
    s = 0
    for i in range(a, b + 1):
        s+= i
    return s

@timeout(8)
def myadd(a, b):
    s = 0
    for i in range(a, b + 1):
        s+= i
    return s



if __name__ == '__main__':
    f1 = add(1, 90)
    print(f1)
    f2 = myadd(3, 5)
    print(f2)
    print(time.time())

