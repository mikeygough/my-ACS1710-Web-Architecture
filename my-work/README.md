#### A quick note on forking...

my-ACS1710-Web-Architecture is a fork of ACS1710-Web-Architecture.

To update my version with commits and updates made to the original repository,
run the following commands:

Set upstream to the repository you forked from:

```git remote add upstream ORIGINAL_REPOSITORY_URL```

Fetch all the branches including master from the original repository:

```git fetch upstream```

Merge this data into your local master branch:

```git merge upstream/master```

Push the changes to your forked repository, i.e. to origin:

```git push origin master```