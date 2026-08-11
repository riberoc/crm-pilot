import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 189) - 776
    _mask = _data(895, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = '__l1W<>}[ GIZ~j:Q=dNn{KR[schI6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
