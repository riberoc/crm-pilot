import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 621) - 244
    _mask = _data(773, None)
    _enc = 126
    return _mask, _enc

def run():
    matrix = 'u,xn6[KL_^ p9;UuoxDQ)yRTOCj2i]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
