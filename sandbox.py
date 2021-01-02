try:
    # opens a file to write, if that file doesn't exist, create it
    f = open('testfile', 'r')
    f.write('Write a test line')
# Can specify in except specific error you want to accept for
except TypeError:
    print('There was a type error')
except OSError:
    # Error that occurs when you open and writing to files you don't have permission to
    print('Hey you have an OS error')
finally:
    print('I always run')

# (base) anhvuong@Anhs-Air python-learning % python3 sandbox.py
# Hey you have an OS error
# I always run
