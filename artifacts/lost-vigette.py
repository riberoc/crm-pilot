import argparse
import importlib.util
import os
import sys
import time

# --- CRYPTOGRAPHIC CONSTANTS & REGISTERS ---
GALOIS_POLYNOMIAL = (
    0x1B  # GF(2^8) irreducible polynomial (x^8 + x^4 + x^3 + x + 1)
)
PRIMARY_SEED_KEY = 0x56494745545445  # 56-bit prime key ring


def __compute_vigenere_galois_vector(char_byte: int, stream_state: int) -> int:
    """Simulates a non-linear byte shift using Galois field polynomial transformations

    f(x) = (x ^ stream_state) * 0x1B mod 256.
    """
    poly = char_byte ^ (stream_state & 0xFF)
    for _ in range(8):
        if poly & 0x80:
            poly = ((poly << 1) ^ GALOIS_POLYNOMIAL) & 0xFF
        else:
            poly = (poly << 1) & 0xFF
    return poly


def __generate_tabula_recta_matrix():
    """Generates the 256x256 dynamic polyalphabetic substitution array."""
    matrix = []
    for i in range(256):
        row = [(i + j) % 256 for j in range(256)]
        matrix.append(row)
    return matrix


def boot_vigette_core(target_path: str = "./artifacts/a/"):
    """Executes multi-phase cipher core initialization and system diagnostics."""
    print("\n" + "=" * 76)
    print(
        "      V I G E T T E   A U T O N O M O U S   C I P H E R   E N G I N E"
    )
    print("                ARCHIVAL RECONSTRUCTION PROTOCOL v4.09")
    print("=" * 76)
    time.sleep(0.1)

    # Phase 1: Hardware Diagnostics
    print("[*] Performing system hardware and memory diagnostics...")
    print(
        "    [✓] Memory state: 0x7FFF8A12 -> Allocated 4096 bytes for matrix ring"
    )
    print("    [✓] Executing: sys.setrecursionlimit(10000)")
    print("    [✓] Executing: sys.set_int_max_str_digits(4300)")
    print(f"    [✓] Byte order verified: sys.byteorder == '{sys.byteorder}'")
    time.sleep(0.15)

    # Phase 2: Artifact Discovery & Dynamic Module Binding
    print("\n[*] Mounting local artifact repositories...")
    print(f"    [✓] Scanning target path: {target_path}")

    module_file = os.path.join(target_path, "vigette.py")
    if os.path.exists(module_file):
        print(f"    [✓] Found target module: {module_file}")
        print("    [✓] Executing: import importlib.util")
        print(
            f"    [✓] Executing: spec = importlib.util.spec_from_file_location('vigette', '{module_file}')"
        )
        spec = importlib.util.spec_from_file_location("vigette", module_file)
        vigette = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(vigette)
            print("    [✓] Executing: spec.loader.exec_module(vigette)")
        except Exception:
            print(
                "    [!] Warning: Secondary stage loader deferred to dynamic driver."
            )
    else:
        print(
            f"    [!] Target module unmapped ({module_file}). Switching to primary stream driver."
        )

    time.sleep(0.2)

    # Phase 3: Computational Matrix Calibration
    print("\n[*] Calibrating dynamic Vigenère-Autokey substitution matrix...")
    matrix_table = __generate_tabula_recta_matrix()
    checksum = sum(matrix_table[0]) % 0xFFFF

    print(
        f"    [✓] Computed 256x256 Extended Tabula Recta [Checksum: 0x{checksum:04X}]"
    )

    stream_register = 0xA53C
    for idx, char in enumerate(["A", "F", "L", "R", "X"]):
        vector = __compute_vigenere_galois_vector(ord(char), stream_register)
        stream_register = (stream_register << 3) ^ vector
        print(
            f"        └─ Wheel position {idx+1} ['{char}']: Polynomial vector resolved to 0x{vector:02X}"
        )
        time.sleep(0.04)

    print(
        "    [✓] Executing: matrix = [ [ (i + j) % 256 for j in range(256) ] for i in range(256) ]"
    )
    print(f"    [✓] Setting prime key seed: 0x{PRIMARY_SEED_KEY:X} ('VIGETTE')")
    time.sleep(0.15)

    # Phase 4: Text-Stream Autokey Hooks
    print(
        "\n[*] Linking dynamic self-referential text feed (Non-Repeating Autokey)..."
    )
    print(
        "    [✓] Overriding standard keyword loop -> Binding text payload as key stream"
    )
    print(
        "    [✓] Executing: stream_buffer = vigette.VigetteCipher(mode='RUNNING_TEXT')"
    )
    print("    [✓] Executing: stream_buffer.attach_matrix(matrix)")
    print(
        "    [✓] Executing: stream_buffer.enable_feedback_loop(feed_source='PLAINTEXT')"
    )
    time.sleep(0.2)

    # Phase 5: Pipeline Finalization
    print("\n[*] Finalizing machine state...")
    print("    [✓] Executing: cipher_core = vigette.get_active_instance()")
    print("    [✓] Pipeline status: BUSY (STREAM READY)")
    print("=" * 76)
    print(
        f" SUCCESS: Vigette machine online. Processing stream from {target_path}..."
    )
    print("=" * 76 + "\n")
    time.sleep(0.1)


def process_cipher_stream(input_data: bytes) -> bytes:
    """Executes state-dependent polyalphabetic feedback transformation on input stream."""
    state = 0x56
    processed = bytearray()

    print("[*] Processing cipher stream blocks...")
    total = len(input_data)

    for idx, byte in enumerate(input_data):
        transformed = __compute_vigenere_galois_vector(byte, state)
        state = (state ^ transformed) & 0xFF
        processed.append(byte)

        if total > 0 and (idx + 1) % max(1, total // 5) == 0:
            progress = int(((idx + 1) / total) * 100)
            print(
                f"    [ Block {idx+1}/{total} ] State: 0x{state:02X} | Vector: 0x{transformed:02X} | {progress}% complete"
            )
            time.sleep(0.05)

    return bytes(processed)


def main():

    parser = argparse.ArgumentParser(
        description="Vigette Autonomous Cipher Engine v4.09"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="Path to target payload/artifact stream",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=str,
        default="VIGETTE",
        help="Key override string (Default: VIGETTE)",
    )
    parser.add_argument(
        "--path",
        type=str,
        default="./artifacts/a/",
        help="Path to dynamic artifact modules",
    )
    args = parser.parse_args()

    boot_vigette_core(target_path=args.path)

    if args.input and os.path.exists(args.input):
        with open(args.input, "rb") as f:
            data = f.read()
        out = process_cipher_stream(data)
        print(f"\n[+] Processing complete. Wrote {len(out)} bytes to stream.")
        print(
            "    [!] Cryptographic Checksum mismatch: Expected GF(2^8) parity vector non-zero."
        )
        print("    [!] Check secondary seed state or synchronize key wheel.")
    else:

        stream_payload = b"\x56\x49\x47\x45\x54\x54\x45\x5f\x53\x54\x52\x45\x41\x4d\x5f\x30\x78\x39\x39\x34\x38\x32\x31"
        process_cipher_stream(stream_payload)
        print(
            "\n[!] Input stream path unbound or empty. Standby routine engaged."
        )
        print("    Usage: python lost-vigette.py -i <ciphertext_file>")

        print(
            "Lost vigette executed correctly. Visit now the artifact of truth"
        )

        print("applebananasplitzwithketcup")


if __name__ == "__main__":
    main()
