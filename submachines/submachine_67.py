import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 220) - 816
    _mask = _data(882, None)
    _enc = 100
    return _mask, _enc

def run():
    matrix = ',GlnrI]lj-AA]whZH~mTt.ydN<DDSn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
