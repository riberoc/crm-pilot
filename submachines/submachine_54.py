import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 190) - 608
    _mask = _data(945, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = '0qp3>@<0[L jX=vH/1C@XgI<|6kRy8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
