import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 652) - 139
    _mask = _data(991, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = '20QzX1S~GwjnTXZj *W!/FAg[!J[RY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
