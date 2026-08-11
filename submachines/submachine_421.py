import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 575) - 631
    _mask = _data(136, None)
    _enc = 70
    return _mask, _enc

def run():
    matrix = 'rv[]{z ags9~`A-BCb;i*dSA3u>LB%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
