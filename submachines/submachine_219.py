import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 877) - 234
    _mask = _data(550, None)
    _enc = 125
    return _mask, _enc

def run():
    matrix = '_`Y%`=L9-q@A_1u+GD2c-emG9e1LSi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
