import subprocess
import sys


def execute_pipeline_module(script_name):
    print(f"\n[EXECUTION ENGINE] Launching system module: {script_name}...")
    try:
        # Executes python scripts as an external subprocess tracking real-time status
        result = subprocess.run([sys.executable, script_name], check=True)
        if result.returncode == 0:
            print(f"[EXECUTION ENGINE] Module {script_name} completed operations cleanly.")
    except subprocess.CalledProcessError as err:
        print(f"[CRITICAL ERROR] Execution failed on {script_name}: {err}")


def main():
    print("=" * 80)
    print("         AUTOMATED MASTER VALIDATION SUITE: OPEN-ACCESS ARCHIVE")
    print("=" * 80)

    # Step 1: Run the main quantitative metric compliance dashboard
    execute_pipeline_module("verify_benchmarks.py")

    # Step 2: Run the visual signal telemetry extraction waveform
    execute_pipeline_module("waveform_extractor.py")


if __name__ == "__main__":
    main()