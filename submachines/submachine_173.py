import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 346) - 440
    _mask = _data(184, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = 'q6#*6B6r: %bRPcEEo=#~xvl6i{R!|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
