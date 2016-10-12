One of the things that interest me are stocks and shares and I have been very inpired by <a href="https://en.wikipedia.org/wiki/Benjamin_Graham">Benjamin Graham</a>'s <a href="http://www.flipkart.com/intelligent-investor-english/p/itmdyszyhhrjj6sn?pid=9780062312686&amp;ref=L%3A-2964926893515846508&amp;srno=p_1&amp;query=intelligent+investor+by+benjamin+graham&amp;otracker=from-search">The Intelligent Investor</a>. So I started creating an app for security analysis. I am writing it in python and its freely available in this <a href="https://github.com/infinite-Joy/stock-analysis">github repo</a>.

To do this I am trying to scrape data from various financial websites by using the lxml and requests libraries.
<pre><code>from lxml import html
import requests</code></pre>
We can then get the content from the url through the requests module and then parse the webpage through the html module in lxml
<pre><code>page = requests.get(url)
tree = html.fromstring(page.content)</code></pre>
To get the specific resource from the webpage I used the firefox add-on <a href="https://getfirebug.com/firstrun#Firebug%202.0.13">Firebug.</a> After that if we hover on the specific resource that we need we can right click on that resource and this should appear.

<a href="http://joydeepbhatt.com/wp-content/uploads/2015/11/firebug.png"><img class="alignnone size-full wp-image-38" src="http://joydeepbhatt.com/wp-content/uploads/2015/11/firebug.png" alt="firebug" width="222" height="248" /></a>

Click on Inspect Element with firebug and this should take you to a page which should show the specific resource along with the underlying tags. You can then right click on it again and this should select "copy xpath" or "copy relative xpath" which ever is present. This would copy the xpath to the clipboard. The xpath looks something like this.
<pre><code>/html/body/div[4]/div[8]/div[8]/div[2]/div/a[4]/
or
//*[@id="ltpid"]</code></pre>
This can then be added to the code to get the required resource from the tree.
<pre><code>required_resource = tree.xpath('xpath/copied/on/clipboard/text()')</code></pre>
Taking similar approach we can simulate the clicking on a link in the page.
<pre><code>link = tree.xpath('xpath/copied/on/clipboard/@href')
link_page = requests.get(link)</code></pre>