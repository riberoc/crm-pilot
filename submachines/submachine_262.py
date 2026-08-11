import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 241) - 519
    _mask = _data(570, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = '-sMQ4E+sj>SlETR}(0b <k<=^S$j:<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
