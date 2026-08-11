import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 693) - 617
    _mask = _data(76, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = ',Uu0Jht6j;E!lt!ay[DG |cdz4-a=P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
