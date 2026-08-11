import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 745) - 698
    _mask = _data(344, None)
    _enc = 244
    return _mask, _enc

def run():
    matrix = '-TEUoVKp.ZV|Ygo|jgODJ#KITt0oI;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
