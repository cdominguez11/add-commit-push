import argparse
import subprocess
import sys


def run_and_print(cmd):
    print(f"> {' '.join(cmd)}")
    print()
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    if output:
        print(output)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(description="Add, commit, and push changes to Git.")
    parser.add_argument("-m", dest="message", default="Update", help="Commit message")
    parser.add_argument("-f", dest="force", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()

    # Show current git status
    print("git status:")
    status = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(status.stdout.strip())

    # Show queued commands and ask for confirmation
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", args.message],
        ["git", "push"],
    ]
    print("\nQueued commands:")
    for cmd in commands:
        print(f"  {' '.join(cmd)}")

    if args.force:
        print("\nForce flag set — skipping confirmation.")
    else:
        confirm = input("\nExecute the above commands? (y to confirm): ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            sys.exit(0)

    # Execute each command
    print()
    for cmd in commands:
        run_and_print(cmd)

    print("\nDone.")


if __name__ == "__main__":
    main()
