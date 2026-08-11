import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 564) - 385
    _mask = _data(116, None)
    _enc = 187
    return _mask, _enc

def run():
    matrix = 'O{Q` -@Y_B%tK5T>TuJ[?p}z*}?zQ@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
