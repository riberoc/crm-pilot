import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 749) - 502
    _mask = _data(67, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = '0K;hZLN8s2|=/z 3.$*s!v)93(3]55'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
