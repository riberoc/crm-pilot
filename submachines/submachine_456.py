import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 405) - 928
    _mask = _data(1533, None)
    _enc = 205
    return _mask, _enc

def run():
    matrix = '{}(j` L<=*wmT/Gl?l*It|tw(ksJ4='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
