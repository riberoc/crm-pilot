import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 229) - 905
    _mask = _data(1159, None)
    _enc = 200
    return _mask, _enc

def run():
    matrix = 'E6]VZr]6tpI9JQg_R uZD!|niv}86S'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
