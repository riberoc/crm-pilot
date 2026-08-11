import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 625) - 687
    _mask = _data(164, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = ',=mAsPocla2ayleU.8L)o9NSh.Mh51'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
