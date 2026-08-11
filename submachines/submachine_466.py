import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 270) - 326
    _mask = _data(791, None)
    _enc = 200
    return _mask, _enc

def run():
    matrix = '9>s}Q*i[mO#^,Y.&fuOhgZ8:Zv. a@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
