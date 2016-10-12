<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">New Post : GitHub vs. Bitbucket: It’s More Than Just Features <a href="http://t.co/5HcDgEJU8j">http://t.co/5HcDgEJU8j</a> by <a href="https://twitter.com/takipid">@takipid</a> <a href="https://twitter.com/tkfxin">@tkfxin</a> <a href="http://t.co/FkY9BHGtgM">pic.twitter.com/FkY9BHGtgM</a></p>&mdash; Iris Shoor (@IrisShoor) <a href="https://twitter.com/IrisShoor/status/469181854667784192">May 21, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Disclaimer: In this post I will be talking about `GitHub`_ and `Bitbucket`_. This may include information on related to various topics like price point differences between the various companies. These information are true to the best of my knowledge. Then again, these may change at any later date. Please look into the most recent documents provided directly by those companies to have a more upto date information before making any decisions for your company/product.

Gone are the days when people had no idea about version control systems and companies had to train a junior developer for a year just to get them more acquainted with the nitty gritty of working in a profession team, of which working with a version control system is a huge part. Github has brought the version control sytem to the masses. It feels like facebook/twitter. You can star various repositories, follow your favorite developers, create organisations and release awesome software for the masses. These days it seems like everyone gets born with a github page.

The main competitor to GitHub is the Bitbucket. The basic features are almost the same. The only major difference is in their pricing and that bitbucket provides us with two options for our version control: git and mercurial. Github provides unlimited public repositories but you have to pay for the private ones. Bitbucket on the other hand gives you the option of free private repositories. It charges based on the number of users. You might guess it correctly that the difference in the pricing model mirrors their philosophy. Github is geared towards open-source and bitbucket is focused towards the enterprise developers.

So what does it mean for us, the every-day developers. One strategy can be that we can start our repositories in bitbucket as a private repo. The idea maybe to first prototype it and then see how to goes. Its pretty hard to know from before if an idea has merit. Once a critical stage is reached you can then decide whether to make the product/repo open-source or to make a business out of it. If you decide that its best to open source your product and then leverage the vast expertise of the developer community then we can just port the existing repository that you have to github. To do this you can follow the steps written below. Of course this is only one of the possible combinations and if your use case does not exacly mirror the flow that is described here or if you encounter any issues please post it in the comments below. Alternatively, you can also raise a question on `Stack Overflow`_.

First create a public repository on Github. For creating repositories there are `excellent articles`_ in case you dont already know how to create one. Do not check the"create README.md" option as this might introduce merge issues when doing the migrating later.

Clone the bitbucket repo if you have not already done it
<code style="font-size: 15px;">
git clone git@bitbucket.org:YOUR-BIT-USERNAME/YOUR-BIT-REPOSITORY.git
</code>

Please check once if the origin is pointing to the present bitbucket repository using the command <code style="font-size: 15px;">git remote -v</code>

Next remote add the github repository link for the repository that you had created earlier. Note: It helps if the username for both GitHub and the Bitbucket is the same and you use the same username for commiting changes. This way your profile history in GitHub too will mirror all the work that you had done committing changes while working in the Bitbucket repo.
<code style="font-size: 15px;">
git remote add gitremote git@github.com:YOUR-GIT-USERNAME/YOUR-GIT-REPOSITORY.git
</code>

Now the remote list should look like this.
<code style="font-size: 15px;">
gitremote       git@github.com:YOUR-GIT-USERNAME/YOUR-GIT-REPOSITORY.git (fetch)
gitremote       git@github.com:YOUR-GIT-USERNAME/YOUR-GIT-REPOSITORY.git (push)
origin  git@bitbucket.org:YOUR-BIT-USERNAME/YOUR-BIT-REPOSITORY.git (fetch)
origin  git@bitbucket.org:YOUR-BIT-USERNAME/YOUR-BIT-REPOSITORY.git (push)
upstream        git@bitbucket.org:COMPANY-NAME/COMPANY-BIT-REPOSITORY.git (fetch)
upstream        git@bitbucket.org:COMPANY-NAME/COMPANY-BIT-REPOSITORY.git (push)
</code>

The normal flow can then be resumed as is said in this `nice article`_ on git flows.
Make a new branch
<code style="font-size: 15px;">
git checkout -b migration
</code>

Make any changes if needed. Commit them
<code style="font-size: 15px;">
git commit -am "latest commits before migration"
</code>

Push the branch to Github.
<code style="font-size: 15px;">
git push gitremote migration
</code>

Now that the code has been pushed you can go to Github. You will find that a new branch has been created there. You can open a pull request and merge the branch with master.

Now you might ask why to do this roundabout method instead of just initialising the repo and copying all the code directly from the directory which has the Bitbucket code. Now you dont want to lose the git history that you have created through all the work that you have done in the Bitbucket repo for the last few months. That is the whole point of source control where you want to retain the history of the code and would like to revert back to any previous state from the point where you started your development journey. So pushing all the code along with all the history makes sense.

Now while doing this on my own `predictit repo`_ which I recently open-sourced, I ran into one more trouble. Github doesnt allow files to be more than 50mb. This is not an issue with Bitbucket. So I had to purge my git history because of that using the below command.

<code style="font-size: 15px;">
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch path/to/big/file' --prune-empty --tag-name-filter cat -- --all
</code>

After that committed the changes and pushed the repo to GitHub and it worked like a charm. If you take this method your profile history should also reflect the amount of work you have done for this.

Before concluding this post I just want to add that there was a lot of complexity that I didn't need to address since I was using git for my source control in Bitbucket as well. If you are using mercurial and want to migrate to github then checkout the blog posts from codio.com that I have linked to in the references.

PEACE.

<ul style="font-size: 12px;">
    <li>https://gist.github.com/foogit/8410710</li>
    <li>http://www.business2community.com/business-innovation/bitbucket-vs-github-best-version-control-software-business-01623901#Eo8gBT3SRB3KkEI2.97</li>
    <li>https://codio.com/blog/moving-from-mercurial-to-git/</li>
    <li>https://help.github.com/articles/remove-sensitive-data/</li>
</ul>

.. _GitHub: https://github.com/
.. _Bitbucket: https://bitbucket.org/
.. _Stack Overflow: http://stackoverflow.com/
.. _excellent articles: https://help.github.com/articles/create-a-repo/
.. _nice article: http://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/
.. _predictit repo: https://github.com/infinite-Joy/predictit
