import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 616) - 821
    _mask = _data(477, None)
    _enc = 130
    return _mask, _enc

def run():
    matrix = '0PhL4=o#]Zs@&X,:rrn=Ef}&#ePlDs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
