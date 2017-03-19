# search-algorithms

Folder Organization

- Python
- Java
- C++


# 🚀 Submitting a Pull Request

1. Fork the repository on GitHub
2. Clone the forked repository to your machine
3. Create a "feature" branch in your local repository
4. Make your changes and commit them to your local repository
5. Rebase and push your commits to your GitHub remote fork/repository
6. Issue a Pull Request to the official repository
7. Your Pull Request is reviewed by a committer and merged into the repository


_Do you have a contribution?  We welcome contributions, but please ensure that you read the following information
before issuing a pull request.  Also refer back to this document as a checklist before issuing your pull request.
This will save time for everyone._

# Before You Start

## Understanding the Basics

If you don't understand what a *pull request* is, or how to submit one, please refer to the [help documentation](https://help.github.com/articles/about-pull-requests/)
provided by GitHub.

## Is It Really a Support Issue

If you aren't sure if your contribution is needed or necessary, please visit the [support forum][] before attempting to
submit a pull request or a ticket.

## Search the Project Issues

It is useful, before you get too far, to make sure that your issue isn't already known or otherwise addressed by checking
the [issues list][issues] for this project.  If you think it is a valid defect or enhancement, feel free to submit your pull
request.

## Discuss Non-Trivial Contributions with the Committers

If your desired contribution is more than a non-trivial fix, you should discuss it on the
[contributor's mailing list][dojo-contrib].  If you currently are not a member, you can request to be added.

## Contributor License Agreement

We require all contributions to be covered under the JS Foundation's [Contributor License Agreement][cla].  This can
be done electronically and essentially ensures that you are making it clear that your contributions are your
contributions, you have the legal right to contribute and you are transferring the copyright of your works to the Dojo
Foundation.

If you are an unfamiliar contributor to the committer assessing your pull request, it is best to make it clear how
you are covered by a CLA in the notes of the pull request.  The committer will verify your status.

If your GitHub user id you are submitting your pull request from differs from the e-mail address which you have signed
your CLA under, you should specifically note what you have your CLA filed under (and for CCLA that you are listed under
your company's authorised contributors).

# Submitting a Pull Request

The following are the general steps you should follow in creating a pull request.  Subsequent pull requests only need
to follow step 3 and beyond:

1. Fork the repository on GitHub
2. Clone the forked repository to your machine
3. Create a "feature" branch in your local repository
4. Make your changes and commit them to your local repository
5. Rebase and push your commits to your GitHub remote fork/repository
6. Issue a Pull Request to the official repository
7. Your Pull Request is reviewed by a committer and merged into the repository

*Note*: While there are other ways to accomplish the steps using other tools, the examples here will assume the most
actions will be performed via the `git` command line.

## 1. Fork the Repository

When logged in to your GitHub account, and you are viewing one of the main repositories, you will see the *Fork* button.
Clicking this button will show you which repositories you can fork to.  Choose your own account.  Once the process
finishes, you will have your own repository that is "forked" from the official one.

Forking is a GitHub term and not a git term.  Git is a wholly distributed source control system and simply worries
about local and remote repositories and allows you to manage your code against them.  GitHub then adds this additional
layer of structure of how repositories can relate to each other.

## 2. Clone the Forked Repository

Once you have successfully forked your repository, you will need to clone it locally to your machine:

```bash
$ git clone --recursive git@github.com:username/core.git dojo-core
```

This will clone your fork to your current path in a directory named `dojo-core`.

You should also set up the `upstream` repository.  This will allow you to take changes from the "master" repository
and merge them into your local clone and then push them to your GitHub fork:

```bash
$ cd dojo-core
$ git remote add upstream git@github.com:dojo/core.git
$ git fetch upstream
```

Then you can retrieve upstream changes and rebase on them into your code like this:

```bash
$ git pull --rebase upstream master
```

For more information on maintaining a fork, please see the GitHub Help article [Fork a Repo][] and information on
[rebasing][] from git.

## 3. Create a Branch

The easiest workflow is to keep your master branch in sync with the upstream branch and do not locate any of your own
commits in that branch.  When you want to work on a new feature, you then ensure you are on the master branch and create
a new branch from there.  While the name of the branch can be anything, it can often be easy to use the issue number
you might be working on (if an issue was opened prior to opening a pull request).  For example:

```bash
$ git checkout -b issue-12345 master
Switched to a new branch 'issue-12345'
```

You will then be on the feature branch.  You can verify what branch you are on like this:

```bash
$ git status
# On branch issue-12345
nothing to commit, working directory clean
```

## 4. Make Changes and Commit

Now you just need to make your changes.  Once you have finished your changes (and tested them) you need to commit them
to your local repository (assuming you have staged your changes for committing):

```bash
$ git status
# On branch issue-12345
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#        modified:   somefile.js
#
$ git commit -m "Corrects some defect, fixes #12345, refs #12346"
[t12345 0000000] Corrects some defect, fixes #12345, refs #12346
 1 file changed, 2 insertions(+), 2 deletions(-)
```

## 5. Rebase and Push Changes

If you have been working on your contribution for a while, the upstream repository may have changed.  You may want to
ensure your work is on top of the latest changes so your pull request can be applied cleanly:

```bash
$ git pull --rebase upstream master
```

When you are ready to push your commit to your GitHub repository for the first time on this branch you would do the
following:

```bash
$ git push -u origin issue-12345
```

After the first time, you simply need to do:

```bash
$ git push
```

## 6. Issue a Pull Request

In order to have your commits merged into the main repository, you need to create a pull request.  The instructions for
this can be found in the GitHub Help Article [Creating a Pull Request][].  Essentially you do the following:

1. Go to the site for your repository.
2. Click the Pull Request button.
3. Select the feature branch from your repository.
4. Enter a title and description of your pull request in the description.
5. Review the commit and files changed tabs.
6. Click `Send Pull Request`

You will get notified about the status of your pull request based on your GitHub settings.

## 7. Request is Reviewed and Merged

Your request will be reviewed.  It may be merged directly, or you may receive feedback or questions on your pull
request.
