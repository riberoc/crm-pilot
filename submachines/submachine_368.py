import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 572) - 111
    _mask = _data(681, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = 'lGcEF4nV;y _mE%1K--i]w55UoLp;g'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
