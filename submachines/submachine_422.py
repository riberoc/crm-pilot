import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 605) - 115
    _mask = _data(759, None)
    _enc = 56
    return _mask, _enc

def run():
    matrix = 'H?^4C#D]Uw4#BqG #EOy(5IvwLxl<D'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
