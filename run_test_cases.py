
import subprocess
import sys

def write_and_run_test_file(code: str, filename: str = "testcases.py"):
    """
    Writes generated test code to file and executes it.
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"\n[INFO] Test file written: {filename}\n")

    try:
        result = subprocess.run(
            [sys.executable, filename],
            capture_output=True,
            text=True
        )

        print("===== STDOUT =====")
        print(result.stdout)

        if result.stderr:
            print("===== STDERR =====")
            print(result.stderr)

    except Exception as e:
        print(f"[ERROR] Execution failed: {e}")
