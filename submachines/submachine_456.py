import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 390) - 461
    _mask = _data(1002, None)
    _enc = 141
    return _mask, _enc

def run():
    matrix = 'i]mIHXK<=c.$n;2s7K %)q!a:0xP$u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
