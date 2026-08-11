import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 174) - 390
    _mask = _data(357, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = '}SUJ@z-EjI2Cx8%9(;H3he8wm uUVl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
