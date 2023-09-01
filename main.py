import subprocess


def list_local_branches():
    try:
        result = subprocess.run(
            ["git", "branch"], stdout=subprocess.PIPE, text=True, check=True
        )
        branches = result.stdout.strip().split("\n")
        return branches
    except subprocess.CalledProcessError:
        print("Error: Unable to list local branches.")
        return []


def delete_branch(branch_name):
    try:
        subprocess.run(["git", "branch", "-D", branch_name], check=True)
        print(f"Deleted branch '{branch_name}'.")
    except subprocess.CalledProcessError:
        print(f"Error: Unable to delete branch '{branch_name}'.")


def print_header():
    print("╭───────────────────────────────────────╮")
    print("│        GitHub Local Branch Manager      │")
    print("│                Version 0.0.1            │")
    print("╰───────────────────────────────────────╯")


def main():
    print_header()
    while True:
        print("Choose an option:")
        print("1. Delete all local branches")
        print("2. Delete specific branch/branches")
        print("3. Cancel")

        choice = input("Enter your choice: ")

        if choice == "1":
            branches = list_local_branches()
            for branch in branches:
                if branch.strip("*") != "main":
                    delete_branch(branch.strip())
            print("Deleted all local branches except 'main'.")
        elif choice == "2":
            branches = list_local_branches()
            print("Local branches:")
            for i, branch in enumerate(branches, start=1):
                print(f"{i}. {branch.strip('*')}")

            selection = input(
                "Enter the branch number or name to delete (or 'done' to exit): "
            )
            if selection.lower() == "done":
                continue

            try:
                selection = int(selection)
                if 1 <= selection <= len(branches):
                    branch_to_delete = branches[selection - 1].strip("*")
                    if branch_to_delete != "main":
                        delete_branch(branch_to_delete)
                    else:
                        print("Cannot delete the 'main' branch.")
                else:
                    print("Invalid selection.")
            except ValueError:
                branch_to_delete = selection.strip()
                if branch_to_delete != "main":
                    delete_branch(branch_to_delete)
                else:
                    print("Cannot delete the 'main' branch.")
        elif choice == "3":
            print("Operation canceled.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
