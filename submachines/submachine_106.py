import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 548) - 650
    _mask = _data(378, None)
    _enc = 204
    return _mask, _enc

def run():
    matrix = 'Us|2P[9kVH4{`~bS3o/ZRA,c fvLDU'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
