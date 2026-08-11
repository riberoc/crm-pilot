import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 554) - 539
    _mask = _data(157, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = 'c/|}x~&6Kqq5f[z]I<y82& vG}^E|u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
