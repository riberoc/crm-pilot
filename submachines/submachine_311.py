import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 841) - 544
    _mask = _data(380, None)
    _enc = 25
    return _mask, _enc

def run():
    matrix = '?w%9S/7Vj,$JETx3>.FI=cWgAh7}#p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
