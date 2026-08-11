import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 394) - 888
    _mask = _data(1421, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = '63{EXf4$28n)V-.z? NPt5g6gb?Ain'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
