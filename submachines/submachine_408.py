import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 878) - 204
    _mask = _data(909, None)
    _enc = 22
    return _mask, _enc

def run():
    matrix = '|nM9@6;Sv]/.lp!b$/zs(mHrsty:5K'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
