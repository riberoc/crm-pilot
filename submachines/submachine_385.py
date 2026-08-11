import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 218) - 498
    _mask = _data(597, None)
    _enc = 139
    return _mask, _enc

def run():
    matrix = 'eRWXfWjWjb3ax{kpaeGi1=efCp,fm8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
