import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 248) - 623
    _mask = _data(595, None)
    _enc = 58
    return _mask, _enc

def run():
    matrix = 'M]{hNi w#l*%V[^L|6;!0@Ykyxme_Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
