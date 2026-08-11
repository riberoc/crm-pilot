import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 641) - 407
    _mask = _data(232, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = ',uBO*U?_!>3xjk1{JVIC*1J9_ is/Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
