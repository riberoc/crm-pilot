import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 169) - 518
    _mask = _data(572, None)
    _enc = 150
    return _mask, _enc

def run():
    matrix = '.eZYl`0G?Ca*A_3)]_GPrDeZ= `I,]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
