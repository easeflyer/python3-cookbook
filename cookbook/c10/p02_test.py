from p02_control_import import *
# from p02_control_import import foo

spam()
grok()
foo()  # 未定义，未包含到 __all__ 中因此通过 * 不会被导入。