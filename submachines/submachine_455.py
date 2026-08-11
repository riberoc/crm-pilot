import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 633) - 480
    _mask = _data(75, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'Sevt[XfAV+b%)fw4 5Wx8c@+5X,`r5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
