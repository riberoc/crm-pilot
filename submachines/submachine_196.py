import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 775) - 529
    _mask = _data(357, None)
    _enc = 70
    return _mask, _enc

def run():
    matrix = '-|,VJ,yA!CD`Uj8sY)Y~]YOiCap[gq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
