import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 328) - 763
    _mask = _data(615, None)
    _enc = 55
    return _mask, _enc

def run():
    matrix = '_1Tc!F[J(D81VG.0Y<8T*K<p0D?}G8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
