import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 241) - 345
    _mask = _data(690, None)
    _enc = 253
    return _mask, _enc

def run():
    matrix = ')4F3z<zVsP>RlOgFCR|%U$Q F^Uk2c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
