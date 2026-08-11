import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 451) - 782
    _mask = _data(754, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = 'P_D]7*6?Os]T7zg.U [3j7MoMs2>jt'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
