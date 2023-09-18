# Module 2: Software Engineering on a Team

## Table of Contents

- [Before you begin](#before-you-begin)
- [Activity](#activity)
  - [1. Create a local copy of your team's GitHub repository](#1-create-a-local-copy-of-your-teams-github-repository)
  - [2. Modifying the behavior of an existing feature in the repository](#2-modifying-the-behavior-of-an-existing-feature-in-the-repository)
  - [3. Adding a new feature to the repository](#3-adding-a-new-feature-to-the-repository)
  - [4. Opening a Pull Request](#4-opening-a-pull-request)
  - [5. Review another student's Pull Request](#5-review-another-students-pull-request)
- [Additional Resources](#additional-resources)
  - [Git](#git)
  - [GitHub](#github)
  
## Before you begin

1. Everyone will be assigned a number xx (e.g., 01-99)
2. Authenticate GitHub from your computer and allow git to remember by caching your GitHub credentials. See [this page](https://docs.github.com/en/github/using-git/caching-your-github-credentials-in-git) for details. We suggest using the GitHub Command Line Interface (CLI), `gh`, which is installed in the `bootcamp` conda environment on DataHub. Start a new terminal session and run the following.

    ```bash
    source activate bootcamp
    gh auth login -p https -w
    ```

## Activity
  
### 1. Create a local copy of your team's GitHub repository

- Navigate to this repository: https://github.com/bioinfo-ucsd/BISB-Bootcamp-softeng

A local copy of this repo will let you make edits to the code and
commit history directly from your computer.
We can make a local copy by **cloning** the repo.

- **Clone** the repository

```bash
git clone git@github.com:bioinfo-ucsd/BISB-Bootcamp-softeng.git
cd BISB-Bootcamp-softeng
```

- You can also install the python package in this directory at this time.
  The `-e` flag specifies "editable" mode, which means local changes you make
  to the python code in this package will be reflected when you import the
  module and run code.

```bash
pip install -e .
```

### 2. Modifying the behavior of an existing feature in the repository

By this point, you have been assigned a number `xx` for use during this activity.

In this section, you will modify the behavior of an existing feature in the repository.

Before making any changes, you should checkout a new branch.

```bash
xx=<your-number>
BRANCHNAME=student-${xx}-branch

git branch $BRANCHNAME # create the branch
git checkout $BRANCHNAME # checkout the branch

# OR create and checkout the branch simultaneously
git checkout -b $BRANCHNAME
```

There is a file called `bootcamp/core/student_${xx}.py`

<details>
  <summary>Show the code</summary>

```python
def count_substring(string, substring):
    """Counts the number of occurrences of `substring` in `string`

    Parameters
    ----------
    string : str
        The string to count within
    substring : str
        The value to count in string

    Returns
    -------
    int
        The number of times `substring` occurs in `string`

    """
    count = 0

    string_length = len(string)
    substring_length = len(substring)
    n_subsequences = string_length - substring_length + 1

    for i in range(n_subsequences):
        left_bound = i
        right_bound = i + substring_length
        candidate_substring = string[left_bound:right_bound]
        if candidate_substring == substring:
            count += 1

    return count

```

</details>

And there is a corresponding tests in `bootcamp/core/tests/test_student_${xx}.py`

<details>
  <summary>Show the code</summary>

```python
from bootcamp.core.student_xx import count_substring


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count

```

</details>

**GOAL**: As a team we have decided that `count_substring()` should be case insensitive, since `ACGT` is equivalent
to `acgt` for our DNA string use case.

For this portion of the activity, you will

1. Write test cases that test whether the existing `count_substring()` code is case insensitive.
2. Modify `count_substring()` in your `student_xx.py` so that it is case insensitive (i.e., `'acgt' == 'ACGT', == 'aCgT'`).
3. Verify that your new code passes the unit tests you wrote. You can do that with the following (run from the root of the git repo):

    ```bash
    pytest
    ```

4. Verify that the code you wrote passes the style checks. You can do that with the following command (run from the root of the git repo)

    ```bash
    flake8
    ```

5. Once you are satisfied with your changes, you should make sure to commit them to your branch:

    ```bash
    # stage your changes
    git add bootcamp/core/student_${xx}.py bootcamp/core/tests/test_student_${xx}.py
    # commit with an informative message
    git commit -m "ENH make count_substring case insensitive"
    ```

### 3. Adding a new feature to the repository

*If you get to this step with fewer than 20 minutes left in the activity, go ahead and skip to the "**4. Opening a Pull Request**" section*

In this section you will add a new feature to the repository.

You should create a file called `bootcamp/contrib/student_${xx}` where you can implement your new feature.

Once you have done this, you can repeat the steps above in the **Modifying the behavior of an existing feature
in the repository**, except with a twist: you get to decide what your function does.

A few guidelines that will help us moderate the activity:

- Please do not import any modules that are not a part of the base python installation (e.g., no `numpy` etc.)
- Please keep your new feature to fewer than 10 lines of code.
- Make sure you run the test suite and style checks locally *before* advancing to "**4. Opening a Pull Request**"

### 4. Opening a Pull Request

After you have made all of the changes you have made (and committed them with `git commit`, you should push them to GitHub

```bash
git push
```

If it is the first time you have pushed on a new branch, you will have to run

```bash
git push origin $BRANCHNAME
```

You can then navigate to  [https://github.com/bioinfo-ucsd/BISB-Bootcamp-module-07](https://github.com/bioinfo-ucsd/BISB-Bootcamp-softeng).

If you have pushed recently, you may notice a box that tells you that you can open a pull request (aka PR).

Otherwise, you can

1. Navigate to the `Pull Requests` tab
2. Click `New pull request` in green on the right-hand side of the page
3. Change the 'compare' branch to your new feature branch. 

Keep the automatically filled PR name, provide a description of your PR (including your student number for this activity) and click `Create pull request`.

After submitting, make sure the automatic checks (GitHub Actions) pass (may
take a couple minutes). If they fail, make sure your code
changes are passing the test suite and style checking locally.

If you make any changes after opening a PR, you can always push more commits. The PR will automatically be updated
and the CI checks will automatically be restarted.

### 5. Review another student's Pull Request

As a contributor to the repository, you can review another student's PR.

1. Navigate to the `Pull Requests` tab and select the PR of another student according to the table below.
2. Ensure that the PR is passing CI checks. If is not, investigate why it is failing.
3. Examine the code of the PR. We encourage you to comment and make suggestions for improvement.
4. Once you are satisfied with the PR, approve and merge it to the `master` branch.

| Your Number | Number to Review |
|-------------|------------------|
| 01          | 22               |
| 02          | 21               |
| 03          | 20               |
| 04          | 19               |
| 05          | 18               |
| 06          | 17               |
| 07          | 16               |
| 08          | 15               |
| 09          | 14               |
| 10          | 13               |
| 11          | 12               |
| 12          | 11               |
| 13          | 10               |
| 14          | 09               |
| 15          | 08               |
| 16          | 07               |
| 17          | 06               |
| 18          | 05               |
| 19          | 04               |
| 20          | 03               |
| 21          | 02               |
| 22          | 01               |

## Additional Resources

If you would like to learn more about git and GitHub, we like the following resources:

### Git

1. [Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf) provided by GitHub is great pocket reference to keep around as you work with git.
2. If you're still having a hard time wrapping your head around what's going on when you use git (we don't blame you), we recommend the interactive and visual tutorial [Learn Git Branching](https://learngitbranching.js.org/).
3. [git-scm.com](https://git-scm.com/) holds the official documentation for git. It is a very detailed reference of git's functionality.

### GitHub

1. [GitHub Skills](https://skills.github.com/) has over 10 courses that cover in more detail the concepts we highlighted today and showcases more of what GitHub Actions are capable of.
2. Checkout various branching workflows. Here we used the simple [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow), but those who are developing complex software on bigger teams may want to explore the more involved [git-flow](https://nvie.com/posts/a-successful-git-branching-model/)
3. [GitHub Docs](https://docs.github.com/en) is where you can find answers to virtually any question about GitHub features.
