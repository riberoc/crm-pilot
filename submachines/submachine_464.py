import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 503) - 874
    _mask = _data(543, None)
    _enc = 126
    return _mask, _enc

def run():
    matrix = 'o))cA<Fp.vV;Iyh=A4}yc?)zch7ZkR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
