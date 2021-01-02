def func():
    print('FUNC() IN ONE.PY')


print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported')


# (base) anhvuong@Anhs-Air python-learning % python3 one.py
# TOP LEVEL IN ONE.PY
# ONE.PY is being run directly!
