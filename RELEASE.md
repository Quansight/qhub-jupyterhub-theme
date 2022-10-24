# Making a release

This is the process that the development team follows in order to make
a release:

1. Create a new branch for the release, e.g. `release/2022.10.1`:

    ```bash
    git checkout -b release-0.3.6
    ```

2. Document an overview of changes since the last release in `CHANGELOG.md`
3. Update the version in `pyproject.toml`
4. Build locally using `hatch build`, and verify the contents of the artifacts
5. Submit the PR, and merge the release branch into `main` once approved
6. Prepare the release commit - checkout the branch for the release and make sure it is to date and the repo is clean:

   ```bash
   git checkout main
   git fetch && git pull
   git clean -xdfq
   ```

7. Tag the release with version number and push to `nebari_jupyterhub_theme`

    ```bash
    # remember we use non-zero-padded months and release numbers
    git tag -a `YY.MM.release-no` -m "Release `YY.MM.release-no`"
    git push origin `YY.MM.release-no`
    ```

    If you need to course-correct and delete the tag:

    ```bash
    git tag -d `YY.MM.release-no`
    git push --delete origin `YY.MM.release-no`
    ```

8. Check that the release has been published on PyPI
