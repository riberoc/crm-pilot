import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 512) - 186
    _mask = _data(909, None)
    _enc = 218
    return _mask, _enc

def run():
    matrix = '26sVuwMJ5,;?ly/O%zG[|y~$@V%V6k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
