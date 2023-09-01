# Git Local Branch Delete Manager

Git Local Branch Delete Manager is a command-line tool for managing local Git branches. It allows you to easily delete branches based on your preferences.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

Git Local Branch Delete Manager simplifies the process of deleting local Git branches. It provides options to delete all branches except the main branch, delete specific branches by name, or cancel the operation entirely. This tool is especially useful for cleaning up your local repository and removing branches that are no longer needed.

## Getting Started

Follow the instructions below to get started with Git Local Branch Delete Manager.

### Prerequisites

Before using Git Local Branch Delete Manager, ensure that you have the following prerequisites installed on your system:

- Git
- Python 3.x

### Installation

1. **Clone the Git Local Branch Delete Manager repository to your local machine:**

   ```bash
   git clone https://github.com/yourusername/git-branch-manager.git
   ```
2. **Change your working directory to the project folder:**
    ```bash
    cd git-branch-manager
    ```
3. source ~/.bashrc  # or source ~/.zshrc if you use Zsh

    ```bash
       chmod +x main.py # chmod +x <file_name_as_you_saved>.py'
    ```
4. **Create an Alias:**
   You can create an alias for the script in your shell configuration file (~/.bashrc, ~/.zshrc, etc.). Edit the appropriate configuration file using a text editor. For example:
    ```bash
    vim ~/.bashrc # you can use also other editor of your choice
    ```
   Add the following line to create an alias:
    ```bash
   #alias name can be anything according to your choice
   # you can only download the main.py file and then rename it as you want
    alias gblm='python3 ~/path/to/git_branch_manager/main.py' # alias gblm='python3 ~/path/to/<file_name_as_you_saved>.py'
    ```
   Replace ~/path/to/git_branch_manager.py with the actual path to your script.
5. **Reload the Shell Configuration:** After saving the configuration file, you need to either restart your terminal or run the following command to apply the changes immediately:
    ```bash
    source ~/.bashrc  # or source ~/.zshrc if you use Zsh
    ```

### Usage
To use Git Local Branch Delete Manager, open a terminal and run the following command:
```bash
gbm
```
You will be presented with the following options:

1. Delete all local branches except 'main'.
2. Delete specific branch/branches.
3. Cancel the operation.
Follow the prompts to make your selection and manage your Git branches accordingly.

### Contributing

We welcome contributions from the community to improve Git Local Branch Delete Manager. To contribute, please follow these steps:

#### Development Environment

Ensure you have the following software installed:

- Python 3.8+
- Virtual environment (optional but recommended)

#### How to Contribute
Please follow our [code of conduct](CODE_OF_CONDUCT.md) and [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thank you to the Git community for inspiration and guidance.
