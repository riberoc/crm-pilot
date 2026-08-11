import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 177) - 305
    _mask = _data(284, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'GCtm/?HJX -84E?4=@(FS`(iiDT94z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
