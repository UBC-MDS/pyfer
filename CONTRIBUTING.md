# Contributing

We're using Github to version control our work. By contributing to this project, you agree to abide by the [code of conduct](https://github.com/UBC-MDS/pyfer/blob/master/CONDUCT.md).

### How to contribute:

1) Fork and clone the repo:

      git clone https://github.com/<your_user_name>/pyfer

2) Make changes or updates, then push it to your forked repo:

      git add <the file which has been changed>.
      git commit -m "<message about this commit>"
      git push

3) If the forked branch has fall behind the `master` branch, you can follow following steps to catchup.First time you need to catch up, you have to tell your computer where the upstream repo is:

      git remote add upstream <original_repo_URL>

  Then to catch up this time (and any other time) you type:

      git fetch upstream
      git merge upstream/master
      git push

Push to your forked branch and submit a pull request. One of our developers will review and reply.

Contributing document inspired by [Thoughtbot](https://github.com/thoughtbot/factory_bot_rails/blob/master/CONTRIBUTING.md).
