import subprocess


def print_header():
    print("╭───────────────────────────────────╮")
    print("│          GitBranchCleanUp         │")
    print("│            Version 0.0.1          │")
    print("╰───────────────────────────────────╯")


def list_local_branches():
    try:
        result = subprocess.run(
            ["git", "branch", "--list", "--no-column", "--format=%(refname:short)"],
            stdout=subprocess.PIPE,
            text=True,
            check=True,
        )
        branches = result.stdout.strip().split("\n")
        filtered_branches = [branch for branch in branches if branch != "main"]

        return filtered_branches

    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to list local branches. {e}")
        return []


def delete_branch(branch_name):
    try:
        subprocess.run(["git", "branch", "-D", branch_name], check=True)
        print(f"Deleted branch '{branch_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to delete branch '{branch_name}'. {e}")


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
            if not branches:
                print("No local branches found.")
                return  # Exit the main function, effectively closing the CLI
            for branch in branches:
                delete_branch(branch.strip())
            print("Deleted all local branches except 'main'.")
            return
        elif choice == "2":
            branches = list_local_branches()
            if branches:
                print("Local branches:")
                for i, branch in enumerate(branches, start=1):
                    print(f"{i}. {branch.strip('*')}")

                selection = input(
                    "Enter the branch number(s) or name(s) to delete (comma-separated) or 'm' to main menu: "
                )
                if selection.lower() == "m":
                    continue

                branches_to_delete = [b.strip() for b in selection.split(",")]
                valid_branches = [branch.strip('*') for branch in branches]

                for branch_to_delete in branches_to_delete:
                    if branch_to_delete != "main":
                        if branch_to_delete.isdigit() and int(branch_to_delete) <= len(branches):
                            index = int(branch_to_delete) - 1
                            branch_name = branches[index].strip('*')
                            delete_branch(branch_name)
                        elif branch_to_delete in valid_branches:
                            delete_branch(branch_to_delete)
                        else:
                            print(f"Invalid branch: {branch_to_delete}")
                    else:
                        print("Cannot delete the 'main' branch.")
            else:
                print("No local branches found.")
                return  # Exit the main function, effectively closing the CLI
        elif choice == "3":
            print("Operation canceled.")
            return  # Exit the main function, effectively closing the CLI
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
