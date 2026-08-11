import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 374) - 209
    _mask = _data(81, None)
    _enc = 75
    return _mask, _enc

def run():
    matrix = '{Wn=cQ_Mv0^}(Uq4O-u$eB3JcCT$Oi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
