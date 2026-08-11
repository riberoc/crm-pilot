import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 198) - 806
    _mask = _data(851, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = 'ia.pcG-kNd47_iIHT+JUVBn}`[l/Bu'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
