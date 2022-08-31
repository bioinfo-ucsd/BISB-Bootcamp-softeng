# Module 7: Software Engineering on a Team

## Table of Contents

- [Before you begin](#before-you-begin)
- [Brief Overview](#brief-overview)
- [Activity](#activity)
  - [1. Create a local copy of your team's GitHub repository](#1-create-a-local-copy-of-your-teams-github-repository)
  - [2. Modifying the behavior of an existing feature in the repository](#2-modifying-the-behavior-of-an-existing-feature-in-the-repository)
  - [3. Adding a new feature to the repository](#3-adding-a-new-feature-to-the-repository)
  - [4. Opening a Pull Request](#4-opening-a-pull-request)
  - [5. Review another student's Pull Request](#5-review-another-students-pull-request)
  
## Before you begin

1. Make sure you have a GitHub account. See [here](https://www.codecademy.com/articles/f1-u3-git-setup) for help.
2. Authenticate GitHub from your computer and allow git to remember by caching your GitHub credentials. See [this page](https://docs.github.com/en/github/using-git/caching-your-github-credentials-in-git) for details. We suggest using the GitHub Command Line Interface (CLI), `gh`, which is installed on DataHub.
3. Everyone will be assigned a number xx (e.g., 01-99)

## Brief Overview

This module will cover using git/GitHub to contribute to an existing body of code.

The major steps involved in this tutorial will be:

1. Creating a local copy of your team's GitHub repository.
2. Implementing a feature and tests on a new branch
3. Opening a pull request for your new feature
4. Review a pull request and approve it

## Activity
  
### 1. Create a local copy of your team's GitHub repository

- Navigate to this repository: [https://github.com/bioinfo-ucsd/BISB-Bootcamp-2022-module-07](https://github.com/bioinfo-ucsd/BISB-Bootcamp-2022-module-07)

A local copy of this repo will let you make edits to the code and
commit history directly from your computer.
We can make a local copy by **cloning** the repo.

- **Clone** the repository

```bash
GIT_USERNAME=<your-git-user-name-here>
git clone https://github.com/${GIT_USERNAME}/BISB-Bootcamp-2022-module-07.git
cd BISB-Bootcamp-2022-module-07
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

    If you do not have pytest installed, you can install it with

    ```bash
    pip install -U pytest
    ```

4. Verify that the code you wrote passes the style checks. You can do that with the following command (run from the root of the git repo)

    ```bash
    flake8
    ```

    If you do not have flake8 installed, you can install it with

    ```bash
    pip install -U flake8 
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

You can then navigate to  [https://github.com/bioinfo-ucsd/BISB-Bootcamp-2022-module-07](https://github.com/bioinfo-ucsd/BISB-Bootcamp-2022-module-07).

If you have pushed recently, you may notice a box that tells you that you can open a pull request (aka PR).

Otherwise, you can

1. Navigate to the `Pull Requests` tab
2. Click `New pull request` in green on the right-hand side of the page
3. Change the 'compare' branch to your new feature branch

Then, provide a description of your PR (including your student number for this activity) and click `Create pull request`.

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
| ----------- | ---------------- |
| 01          | 28               |
| 02          | 27               |
| 03          | 26               |
| 04          | 25               |
| 05          | 24               |
| 06          | 23               |
| 07          | 22               |
| 08          | 21               |
| 09          | 20               |
| 10          | 19               |
| 11          | 18               |
| 12          | 17               |
| 13          | 16               |
| 14          | 15               |
| 15          | 14               |
| 16          | 13               |
| 17          | 12               |
| 18          | 11               |
| 19          | 10               |
| 20          | 09               |
| 21          | 08               |
| 22          | 07               |
| 23          | 06               |
| 24          | 05               |
| 25          | 04               |
| 26          | 03               |
| 27          | 02               |
| 28          | 01               |

