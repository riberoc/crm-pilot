import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 314) - 714
    _mask = _data(584, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = 'gEI5Q?dqO-3(@hF&k|Z5ISgB /nU!L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
