import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 647) - 802
    _mask = _data(271, None)
    _enc = 100
    return _mask, _enc

def run():
    matrix = 'aK ujNl7%R!8?CpFn@&<0+pJqz(y_n'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
