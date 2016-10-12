Windows task automaton using pywinauto
##############

:date: 2016-07-15 10:20
:modified: 2016-10-12 00:04
:tags: windows, python, automation
:category: python
:slug: windows-task-automaton-using-pywinauto
:authors: Joydeep Bhattacharjee
:summary: automation in windows using python

<script>
  window.fbAsyncInit = function() {
    FB.init({
      xfbml      : true,
      version    : 'v2.6'
    });
  }; 
  (function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
</script>
  
<div 
  class="fb-post" 
  data-href="https://www.facebook.com/eyantrarit/photos/a.630456120414490.1073741828.627320484061387/699969443463157/?type=3&theater" 
  data-width="500"></div>

Python has a huge number of libraries and continually new libraries are being developed that leverage the existing libraries and push the boundaries even more. So it is of no doubt that there will be libraries that make automating everyday tasks seem like a piece of cake. While researching into those libraries I found out about the selenium library that builds on top of the selenium framework and provides easy automation of browser based tasks. This is a great way to automate website and browser testing and can be leveraged by website designers and developers.

But I was in search of a non browser based automation framework. Lots of tasks are there that are done through native desktop apps. This post came into being as an overlook into the automation of the subclass of those tasks i.e. windows based task. The windows version that I am looking into is windows 7 as this version is still in great use but please feel free to look into automating things in windows 10 as well. These methods should work fine there too.

We developers hate repetition. So we constantly look to remove repetition and redundancy and automate anything and everything. The quest for solving these kinds of problems inspired me to look forward and led me to the pywinauto framework. Now after developing some automation scripts using this framework I am pretty that this powerful library is one of the best methods to automate everyday tasks. If you use this library you will be able to leverage the expressive power of python, the powerful testing frameworks of python which result in fast, separate and easy testing of your modules.

There is a disclaimer here. I have only looked at this library and autoit for me automaton needs so I am not sure about the other robot technologies that are out there like the robot class of java. If there are other packages and libraries that you feel to be more powerful, I would love to hear about them. Also I use one of the applications that come bundled with autoit for reasons that I will share later on in this post, so my automaton development is
not "pure" if you like to put it that way.

Now lets move on to the installations and the setup that is required. First of course you need `Python`_. Please ensure that you have pip and virtualenv as well. If you are using python3 that would translate to pip3 and pyvenv. I will be using the python2.7 paradigm for the trivial things. Please translate it to python3 as and where necessary. For non obvious difference I will point those out explicitly.

Then fire up the virtualenv.

<code>virtualenv venv</code>

This should setup the virtual environment in your automaton root directory. Since this is primarily thought to be developed in windows we need to run the activate batch file.

<code>venv\Scripts\activate.bat</code>

Then install the following packages.

<code>pip install pywinauto, nose, pytest</code>

In addition go to the install the pyinstaller package

<code>pip install pyinstaller</code>

This is optional and is required if you need to provide binaries which will run on other scheduling servers where you would like to avoid installing the python package. If you are not concerned about that and need to run the automaton locally then this step can be skipped.

Then download the swapy package. Either clone the package by typing the following command,

<code>git clone https://github.com/pywinauto/SWAPY.git</code>

or just download the zip file and unzip it. This is used to identify the handlers and the controls that can be run on a window. There is no good way to install it so I will suggest install the dependencies and running it directly.

<code>pip install -r dev-requirements.txt
python swapy-ob.py</code>

This should open a window where the controls will be shown for the existing windows that are open. Select the window that you are looking forward to automate and then this should give the control. Good screenshots are available in the `swapy git page`_.

One last package that I would suggest that you download is the `autoit package`_. This is a whole package and automating language by itself but I didn't feel very comfortable in it. But one of the tools that come packaged with the installer is the autoit window info tool. In many cases I was seeing that I was not finding the specific control for the button or a menu item that I need to be clicked. This window info is a very good tool to find the specific coordinates of the button or the control so that I can pass the coordinated to the mouse click method.

<a href="http://joydeepbhatt.com/wp-content/uploads/2016/07/window_info.png"><img src="http://joydeepbhatt.com/wp-content/uploads/2016/07/window_info-200x300.png" alt="window_info" width="200" height="300" class="alignnone size-medium wp-image-117" /></a>

As you can see in the screenshot the mouse menu is highlighted. First give cntrl+shift+f to unfreeze the window info tool. Then if you move the mouse you will see that the position property will change and it would show you the coordinates. Once you take the mouse and hover over the control that you want to click, then press cntrl+shift+f to freeze the tool again and then you can copy the coordinates to your script.

Then fire up and start writing your script. If you still have problems ping me up and I will call you. A sample script is kept at this `github link`_. If you feel that something can be made better or one of the functions can be made smaller send a pull request and I will be happy to merge it.

At the end if you need to distribute the file as a windows exe binary run the following command

<code>pyinstaller --onefile --paths "drive:\path\toi\venv\venv\Lib\site-packages" my_automaton.py</code>

The onefile arguments tells pyinstaller to generate only one binary file. Paths need to be provided so that pyinstaller will search for the requisite packages in the virtual environment directory. If there are any errors in the build please check if its not a syntax error in the script. Test the binary and repeat till you have everything in place.

Thanks for reading this post and if you feel that some things that are explained here can be made better please give in the comments. I hope this has fired you up and now will automate away all the tasks that you have been hating all this time.

Happy Coding.:)

.. _Python: https://www.python.org/
.. _swapy git page: https://github.com/pywinauto/SWAPY
.. _autoit package: https://www.autoitscript.com/site/autoit/
.. _github link: https://github.com/infinite-Joy/windows_automation/blob/master/sql_developer_automaton/sql_developer_automaton.py
