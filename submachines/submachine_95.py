import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 878) - 646
    _mask = _data(59, None)
    _enc = 214
    return _mask, _enc

def run():
    matrix = 'G,c}CE[hK%#ZbREJ(Lr6tHKGw nyJv'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
