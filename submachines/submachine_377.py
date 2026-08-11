import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 353) - 293
    _mask = _data(166, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = '0GK,qU kr0f-2;bMc]qN:Z5si6[h]~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
