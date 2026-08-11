import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 176) - 493
    _mask = _data(676, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = ',72{z.DQMudB8dFJ_E:c)+u%X!|T1+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
