import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 190) - 483
    _mask = _data(763, None)
    _enc = 126
    return _mask, _enc

def run():
    matrix = 'sPr,LDx/x*f]d]Vl678FFAi@P/nc 9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
