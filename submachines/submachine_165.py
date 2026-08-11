import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 897) - 729
    _mask = _data(237, None)
    _enc = 149
    return _mask, _enc

def run():
    matrix = '8kB(Aw iDd?W@fB2GTwVC]/BkV|WZ?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
