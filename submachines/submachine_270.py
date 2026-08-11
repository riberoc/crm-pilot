import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 106) - 216
    _mask = _data(291, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = 'E& zyV%0k/KuURTHit)8;&,/VC[vFJ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
