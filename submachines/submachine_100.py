import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 145) - 448
    _mask = _data(571, None)
    _enc = 253
    return _mask, _enc

def run():
    matrix = 'HMo_<5CM_A~A{^{,+Qt7$My ^c2TS2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
