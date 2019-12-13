import foo
import spam

foo.func2()
spam.func1()


'''
打包成 zip 运行。
bash % ls
spam.py bar.py grok.py __main__.py
bash % zip -r myapp.zip *.py    # 注意这里，要在目录里面执行。如果直接打包目录，会造成路径错误。
bash % python3 myapp.zip        # 而采用 .pyz 方案相对更合理。


官方方案：
目录结构和 zip 一致，也是要写好 __main__.py

$ python -m zipapp myapp    # 把 myapp 目录打包成 .pyz
$ python myapp.pyz          # 直接运行即可。
<output from myapp>    

$ python -m zipapp myapp -p "/usr/bin/env python"
# 这样打包后。可以直接运行，不用加 python
$ ./myaqpp.pyz 

'''