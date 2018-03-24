# CI for Python with Travis.org
![Build status](https://travis-ci.org/ddmee/travis-git-python.svg?branch=master)

Travis.org provides open-source projects with a free CI facility. 

This repository plays around with Travis and Github, to automatically test the contained python code.

Goals:
1. Automatically build and test all commits
2. Prevent commits to master that have not passed the tests.

Goal 1 is pretty easy to meet. Travis is easier to setup, so that whenever any commit is made on Github, it builds the commit. Travis only supports Linux (I found the OSX build option to cause failures for no-reason. Multiple operating system builds is beta-feature in Travis). Using tox, we can build the code and run the tests in many versions of python.

Goal 2 is a little more difficult. The natural way to prevent commits to master or to the server is to use Git's server side hooks. Server side hooks run in response to events, like a pull or a commit. Hook's allow the execution of arbitrary code to run the event occurs.

However, hosted solutions, like Github and Bitbucket do not provide a way to upload server-side hooks for obvious reasons. Instead, Github replicates a stripped down version of server-side hooks through an API and branch protection that can wait for CI integrations to pass before commiting to a protected branch.

### Support or Contact

Contact (email gmail.com) mee.donal  if you are interested in what this does.
