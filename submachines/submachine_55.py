import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 319) - 106
    _mask = _data(24, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = 'mG_RW[Enk+h4=Li5|l#UzlC9 D[JOw'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
