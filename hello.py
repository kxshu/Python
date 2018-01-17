#!python
# encoding: utf-8

def hello(name='world'):
    return 'Hello %(name)s' % dict(name=name)

if __name__ == '__main__':
    print(hello())

######  or just:  #############

print('hello world')
