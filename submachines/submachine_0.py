import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 557) - 953
    _mask = _data(474, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = 'RRt^`IBE;rF],LgLlSHC!7>R(Uo$ :'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
