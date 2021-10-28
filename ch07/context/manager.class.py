# context/manager.class.py
class MyContextManager:
    def __init__(self):
        print("MyContextManager init", id(self))

    def __enter__(self):
        print("Entering 'with' context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type=} {exc_val=} {exc_tb=}")
        print("Exiting 'with' context")
        return True


ctx_mgr = MyContextManager()

print("About to enter 'with' context")

with ctx_mgr as mgr:
    print("Inside 'with' context")
    print(id(mgr))
    raise Exception("Exception inside 'with' context")
    print("This line will never be reached")

print("After 'with' context")


"""
$ python context/manager.class.py
MyContextManager init 140340228792272
About to enter 'with' context
Entering 'with' context
Inside 'with' context
140340228792272
exc_type=<class 'Exception'> exc_val=Exception("Exception inside
 'with' context") exc_tb=<traceback object at 0x7fa3817c5340>
Exiting 'with' context
After 'with' context
"""
