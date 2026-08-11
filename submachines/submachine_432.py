import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 430) - 232
    _mask = _data(152, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = '18zZNxzl`,c3:Au96:fiRq AJurMBX'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
