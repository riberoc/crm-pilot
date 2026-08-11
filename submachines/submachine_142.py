import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 437) - 263
    _mask = _data(52, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = 'prpLX4;RTI52fM4G4#1 ),~ci,OUUI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
