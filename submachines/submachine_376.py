import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 733) - 350
    _mask = _data(866, None)
    _enc = 112
    return _mask, _enc

def run():
    matrix = 'n!0ivDM,=!x/wr_`J ab7CQV6SqI]6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
