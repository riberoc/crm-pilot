import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 851) - 180
    _mask = _data(542, None)
    _enc = 148
    return _mask, _enc

def run():
    matrix = 'fBCY/iDxsO>qL Q&:%<wIj.y?]z9J0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
