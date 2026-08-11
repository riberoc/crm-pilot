import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 578) - 964
    _mask = _data(1731, None)
    _enc = 191
    return _mask, _enc

def run():
    matrix = 'Ad |L:FVW}u@/92*i>1uZuK@]Vx>B['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
