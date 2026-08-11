import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 786) - 654
    _mask = _data(121, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = '8Ul>axkT^H5I& gNnyROmOe,EDNZ[u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
