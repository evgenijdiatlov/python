import cowsay

cowsay.turtle('HI')
methods = dir(cowsay)
for method in methods:
    try:
        function_to_run = getattr(cowsay, method)
        function_to_run('Hello, word')
        except:
            print('error')
            