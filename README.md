# CI for Python with Travis.org
![Build status](https://travis-ci.org/ddmee/travis-git-python.svg?branch=master)

Travis.org provides open-source projects with a free CI facility. 

This repository plays around with Travis and Github, to automatically test the contained python code.

Goals:
1. Automatically build and test all commits
2. Prevent commits to master that have not passed the tests.

Goal 1 is pretty easy to meet. Travis is easier to setup, so that whenever any commit is made on Github, it builds the commit. Travis only supports Linux (I found the OSX build option to cause failures for no-reason. It is still in beta). Using tox, we can build against the code on multiple versions of python.

Goal 2 is a little more difficult. The natural way to prevent commits to master or to the server would be to use Git's server side hooks. Server side hooks are run in response to events, like a pull or commit, happen. Hook's allow arbitrary code to run run when the event occurs.

However, hosted solutions do not normally allow the use of server side hooks because of the arbitrary code execution feature. Instead, Github provides some other reduced functionality in place of git server-side hooks.

### Support or Contact

Contact (email gmail.com) mee.donal  if you are interested in what this does.
