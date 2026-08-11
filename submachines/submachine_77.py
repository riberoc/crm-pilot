import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 652) - 214
    _mask = _data(899, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'D>HltxZq*fa{nNBAB -P9vAc)/8#/Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
