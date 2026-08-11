import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 520) - 591
    _mask = _data(303, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'U(W5tDQ3 T:!Q[.v-X#q]|8OE!}M3M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
