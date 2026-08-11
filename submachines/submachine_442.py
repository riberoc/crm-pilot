import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 151) - 188
    _mask = _data(399, None)
    _enc = 78
    return _mask, _enc

def run():
    matrix = '/Zv*1W!YEN]|2XLBkLi;{/l%3s;QSu'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
