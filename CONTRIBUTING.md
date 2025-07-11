# Contributing to the Oasis Project

We're thrilled you're interested in contributing to the Oasis project! Your help is invaluable in making this real estate prediction tool even better. This document outlines the guidelines for contributing to ensure a smooth and collaborative process for everyone.

## How to Contribute

We primarily use **Pull Requests (PRs)** for all contributions, whether it's a new feature, a bug fix, or an improvement to the documentation. This helps us review changes, discuss potential improvements, and maintain code quality.

### 2. Clone the git repository

Clone the repository to your local machine:

```bash
git clone [https://github.com/nclsprsnw/oasis.git](https://github.com/nclsprsnw/oasis.git)
cd oasis
```

### 3 Create a New Branch

Before making any changes, create a new branch for your feature, bug fix, or enhancement. This keeps your work organized and isolated from the `main` branch. Use a descriptive name for your branch (e.g., `feat/add-api-logging`, `fix/data-ingestion-error`, `docs/update-readme`).

```bash
git checkout -b your-branch-name
```

### 4. Make Your Changes

Now you're ready to make your contributions\!

  * **Code Style:** Please adhere to the existing code style in the project. We recommend using linters and formatters (e.g., Black for Python) if configured.
  * **Tests:** If your changes involve new features or bug fixes, please include relevant unit or integration tests to ensure correctness and prevent regressions.
  * **Documentation:** Update any relevant documentation (e.g., comments in code, README files, or specific documentation within `api/` or `web/`) to reflect your changes.

### 5. Commit Your Changes

Commit your changes with clear and concise commit messages. A good commit message explains *what* you did and *why* you did it.

```bash
git add .
git commit -m "feat: Add new climate event data processing"
```

We encourage using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) (e.g., `feat:`, `fix:`, `docs:`) for better commit history readability.

### 6. Push to Your Fork

Push your new branch and commits to your forked repository on GitHub:

```bash
git push origin your-branch-name
```

### 7. Create a Pull Request (PR)

Go to your forked repository on GitHub. You should see a prompt to create a **Pull Request** from your new branch to the `main` branch of the original Oasis repository.

When creating your PR, please:

  * **Provide a clear title:** Summarize the main purpose of your PR.
  * **Write a detailed description:** Explain the changes you've made, the problem it solves, any new features it introduces, and how you've tested it. Screenshots or GIFs can be very helpful for UI changes.
  * **Reference any issues:** If your PR addresses a specific issue, link it using keywords like `Closes #123` or `Fixes #456`.

### 8. Code Review and Iteration

Once you submit your PR, a team member will review your code. They might leave comments, ask questions, or request changes. Please be open to feedback and be prepared to iterate on your changes. We appreciate your patience during this process\!

### 9. Merge

After your PR has been reviewed and approved, a maintainer will merge it into the `main` branch. Congratulations, your contribution is now part of the Oasis project\!

-----

Thank you for helping us build a better Oasis\!
