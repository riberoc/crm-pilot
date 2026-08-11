import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 815) - 713
    _mask = _data(474, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = '~Cn8oo#@zKajJ@AKK:{t:)?<R!Q`.,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
