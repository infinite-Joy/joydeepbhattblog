Virtual Box
##############

:date: 2016-02-15 10:20
:modified: 2016-10-12 00:04
:tags: virtualisation
:category: devops
:slug: virtual-box
:authors: Joydeep Bhattacharjee
:summary: virtualisation using virtual-box

I have been struggling a lot with a particular problem and now that I have made finally had a breakthrough, in retrospect it seems, as with all breakthroughs, should not have been that tough. I installed ubuntu in virtual-box and I was not able to make it fullscreen. Nevertheless I am going to go through all the steps that I did for this purpose.

Almost all the resources that a modern developer works with have been virtualised. Nothing is bare-metal these days and virtualisation of the OS or the bare metal server was one of the first resources where the concept of virtualisation was widely adopted. For an individual developer this is of great value. A developer needs to sometimes manipulate and access core areas of the OS or the kernel that he is working in, maybe as a simple developer requirement or for greater performance of his application. He may also need to install various software that he needs for his work. `Virtual Box`_ is an awesome free virtual machine set-up tool provided by Oracle that can cater to such needs of the developer. Also it is also the only professional solution that is freely available as Open Source Software under the terms of the GNU General Public License (GPL) version 2. Whenever i hear the term Open Source I just go GAGA like a school girl.

Having heard these benefits of virtualisation I thought maybe this is something to be tried out and I should definitely look more into it. I am primarily a windows user for my entertainment needs, but because of my work I have good(let me please indulge myself) knowledge of the linux environment. I know that linux will give me a wide range of tools which will make life easier. I wanted to separate my normal environment and my development environment so that if something goes wrong the deleting of the virtual machine will just be a piece of cake and I can always reinstall everything. I have a windows 7 in my core machine and I decided that I will install virtual-box and will install `Ubuntu`_ in my virtual machine.

Next I downloaded and installed virtual-box and the `instructions`_ were helpful. I downloaded the ubuntu image file. I fired a vm in the virtual-box and then installed the Ubuntu OS.

Now here comes the fun part. I saw that the screen takes up only a part of the screen. It is as if the whole visualization thing went south on me. Kaboom.!!?! The screen filled only a tiny part of my desktop. And when I fired the `Almighty Terminal`_ (cntrl+alt+t), that too took more smaller part and things just was not working for me. At that time I was doing some learning C/C++ language and had not figured out how to compile it in windows. In any case this was a good thing because this drove me towards `Cygwin`_ and `MinGW`_ and I could learn a little more on how to code in windows. Isn't it our failures that bring out the best in us. So fail a lot, fail fast and look forward to failures.

But then again something happened and the universe again pounded on me that there is a reason why best practices are what they are and why everyone follows them. I was building an app in windows and the language I was using was `Python2.7`_ and I used the multiprocessing module to pipeline the tasks as it was making a lot of network calls and when I fired the app to test it exploded. It took me five seconds to understand what was happening but then I understood that my C:\ drive was filling up completely. Within seconds my app just gobbled up something around 20 GB of space on my main windows drive.

I was sitting there feeling like maybe an administrator in the wake of a viral outbreak with the virus of my own creation. The<span class="Apple-converted-space"> </span>wise old men have always told me that you never ever test things in your main machine, you use a vm and you listen to your own advice. I freed up my disk space by going through files and finding files which were created recently and which are of big sizes, while continually being afraid what if I break my main OS installation. On a side note Cygwin helped me in this which I installed because I was having problems with virtual box in the first place. Its interesting how things move in circles.

So I started looking deeper into the problem and looked into oracle docs and virtual box forums and then they were talking about something called guest additions. The `oracle docs`_ says that installing the guest additions software optimizes the operating system for better performance. So I went and installed it. `This document`_ also helped in understanding it. The installation instructions are given there. After that I rebooted the ubuntu OS.

One other setting that I needed to change was that in the virtual machine settings I needed to have 3D-acceleration enabled and raised the video memory to maximum which is 128 mb.

<img class="alignnone" src="http://i.stack.imgur.com/nyqdc.png" alt="" width="659" height="542" />

One small note: After I resolved this issue I saw that the shared clipboard is also working. So this was the cause of it!
<p style="font-size: 12px;">Reference:
http://askubuntu.com/questions/247629/how-do-i-display-the-whole-desktop-in-virtual-box-fullscreen-mode
http://askubuntu.com/questions/314685/is-there-a-way-to-make-a-fullscreen-on-virtualbox
https://forums.virtualbox.org/viewtopic.php?f=2&amp;t=47641</p>


.. _Virtual Box: https://www.virtualbox.org/
.. _Ubuntu: http://www.ubuntu.com/
.. _instructions: https://www.virtualbox.org/manual/ch02.html#installation_windows
.. _Almighty Terminal: https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal
.. _Cygwin: https://www.cygwin.com/
.. _MinGW: http://www.mingw.org/
.. _Python2.7: https://www.python.org/
.. _oracle docs: https://docs.oracle.com/cd/E36500_01/E36502/html/qs-guest-additions.html
.. _This document: https://www.virtualbox.org/manual/ch04.html
