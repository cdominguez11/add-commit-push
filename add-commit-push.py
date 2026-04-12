import argparse
import subprocess


def run_and_print(cmd):
    print(f"> {' '.join(cmd)}")
    print()
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", dest="message", default="Update")
    parser.add_argument("-f", dest="force", action="store_true")
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
        pass
    else:
        confirm = input("\nExecute the above commands? (y to confirm): ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            return

    # Execute each command
    print()
    for cmd in commands:
        run_and_print(cmd)


if __name__ == "__main__":
    main()
