import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 746) - 989
    _mask = _data(1780, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = 'x-LHOb4zNwbymSjPQ]`V[164Pt4RK&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
