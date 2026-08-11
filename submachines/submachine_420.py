import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 244) - 765
    _mask = _data(811, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = 'FS.hhyJL{k_CH8:k1)Xv}JMaPyruZg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
