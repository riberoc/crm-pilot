import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 821) - 593
    _mask = _data(460, None)
    _enc = 191
    return _mask, _enc

def run():
    matrix = 'E{|FtQvo?2hAvP8gItSD80N ==#[q<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
