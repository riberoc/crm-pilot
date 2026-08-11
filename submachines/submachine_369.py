import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 480) - 713
    _mask = _data(576, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = 'FArehNJ3%yqJgAl;UCr)%=@i$_evdD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
