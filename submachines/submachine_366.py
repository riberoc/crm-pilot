import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 353) - 247
    _mask = _data(106, None)
    _enc = 6
    return _mask, _enc

def run():
    matrix = '=mvq[%}1LhZvv5w2Gt PKA7{_I6ZNc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
