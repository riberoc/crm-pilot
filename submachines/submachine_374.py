import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 978) - 412
    _mask = _data(527, None)
    _enc = 71
    return _mask, _enc

def run():
    matrix = 'tRms_# ll.cHz>.zK*^y##5ZS=Ef}q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
