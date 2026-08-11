import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 911) - 156
    _mask = _data(832, None)
    _enc = 57
    return _mask, _enc

def run():
    matrix = '/TMHE?oU?f lRCJhAq$t6.iOIZKW6l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
