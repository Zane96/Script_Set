from urllib.request import urlopen
from bs4 import BeautifulSoup

html = """
       <!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="小葵要革命|">

    <title>挣脱不足与蒙昧</title>

    <link rel="canonical" href="http://adastaybrave.com/">

    <!-- Icons -->
  <link rel="shortcut icon" href="img/favicon.ico">

    <!-- Bootstrap Core CSS -->
    <link rel="stylesheet" href="/css/bootstrap.min.css">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="/css/clean-blog.css">

    <!-- Pygments Github CSS -->
    <link rel="stylesheet" href="/css/syntax.css">

    <!-- Custom Fonts -->
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href='//fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>






<body ontouchstart="">

    <!-- Navigation -->
<nav class="navbar navbar-default navbar-custom navbar-fixed-top">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header page-scroll">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">挣脱不足与蒙昧</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <a href="/">Home</a>
                </li>

                <li>
                    <a href="/about/">About</a>
                </li>

                <li>
                    <a href="/archive/">Archive</a>
                </li>

                <li>
                    <a href="/milestone/">milestone</a>
                </li>

                <li>
                    <a href="/tags/">Tags</a>
                </li>

            </ul>
        </div>
        <!-- /.navbar-collapse -->
    </div>
    <!-- /.container -->
</nav>


    <!-- Page Header -->
<header class="intro-header" style="background-image: url('/img/facebook.jpg')">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                <div class="site-heading">
                    <h1>挣脱不足与蒙昧</h1>
                    <hr class="small">
                    <span class="subheading">小葵要革命</span>
                </div>
            </div>
        </div>
    </div>
</header>

<link rel="stylesheet" href="/css/backtop.css">  <!-- Back Top -->
<script type="text/javascript" src="/js/backtop.js"></script>  <!-- Back Top -->

<div id="back-top">
  <a href="#top" title="回到顶部"></a>
</div>

<!-- Main Content -->
<div class="container">
	<div class="row">
		<div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">

<div class="post-preview">
    <a href="/python%E7%88%AC%E8%99%AB/2016/07/30/BeautifulSoup%E7%AE%80%E4%BB%8B/">
        <h2 class="post-title">
            BeautifulSoup简介
        </h2>

        <div class="post-content-preview">
            决定开一个系统的基于python 3.5的爬虫教程，囊括对Html的解析，API的使用，数据的存储，文档的读取。数据清洗，语言处理。

之前的6篇文章里对爬虫时用到的BeautifulSoup篇幅太少，为了后续的教程，准备认真开一个写。

Beautiful库出自于《爱丽丝仙境》的诗歌，不得不...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on July 30, 2016</p>
</div>

<hr>

<div class="post-preview">
    <a href="/opencv/2016/06/18/openCV%E6%A3%80%E6%B5%8B%E8%BF%9E%E9%80%9A%E5%9F%9F/">
        <h2 class="post-title">
            openCV检测连通域
        </h2>

        <div class="post-content-preview">
            這一段时间在做研读的论文的实现工作，期间一下用了很多opencv的知识，希望后续会有时间把所学的写成一个系列。

opencv作为一个图像处理库在图像分割，特征提取，人脸识别，计算机视觉领域中应用广泛，今天写一个关于采用opencv对图像连通域检测的demo

前期也是翻阅了很多资料，常见的有...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on June 18, 2016</p>
</div>

<hr>

<div class="post-preview">
    <a href="/python%E7%88%AC%E8%99%AB/2016/06/03/Python-%E7%88%AC%E8%99%AB(6)-%E6%AD%BB%E6%9C%89%E6%89%80%E5%9B%A0/">
        <h2 class="post-title">
            爬虫(6) 死有所因
        </h2>

        <div class="post-content-preview">
            最近忙了起来，博客更新的速度慢了一些。希望忙过這一阵子可以保持持续更新的速度。此后还会开通相册功能，摄影爱好者的必要板块啊！

之前的爬虫学习，调试时进场遇到HTTTP错误状态吗，此篇总结一下的网页的访问异常处理。

异常一般发生在没有网络连接，对方服务器不存在的情况下。

传送门之–常见的h...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on June 3, 2016</p>
</div>

<hr>

<div class="post-preview">
    <a href="/python%E7%88%AC%E8%99%AB/2016/05/24/Python-%E7%88%AC%E8%99%AB(5)-%E5%A4%95%E8%8A%B1%E6%9C%9D%E6%8B%BE/">
        <h2 class="post-title">
            爬虫(5) 夕花朝拾
        </h2>

        <div class="post-content-preview">
            很多爬虫都会写怎么爬取图片，我看着也就写了一点。

不忘初心，爬虫是从网页上抓取数据，那么对网页的解析至关重要。

如果我们要怎么抓取一个有很多图片信息的网页怎么做呢？简单粗暴：


  定位图片标签在html文件中的位置
  提取图片的url
  下载图片到本地


必备工具之Beautif...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on May 24, 2016</p>
</div>

<hr>

<div class="post-preview">
    <a href="/python%E7%88%AC%E8%99%AB/2016/05/19/Python-%E7%88%AC%E8%99%AB(4)-%E8%B8%8F%E9%9B%AA%E6%97%A0%E7%97%95/">
        <h2 class="post-title">
            爬虫(4) 踏雪无痕
        </h2>

        <div class="post-content-preview">
            咱们前边说到，服务器端是可以通过你的Headers信息来识别访问端的，当它发现不正常，会屏蔽其爬虫程序。

User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求继而屏蔽.

我们要修改header的信息来假装自己是浏览器在做访问。


方法一：修改head...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on May 19, 2016</p>
</div>

<hr>

<div class="post-preview">
    <a href="/python%E7%88%AC%E8%99%AB/2016/05/18/Python-%E7%88%AC%E8%99%AB(3)-%E7%89%9B%E5%88%80%E5%B0%8F%E8%AF%95/">
        <h2 class="post-title">
            爬虫(3) 牛刀小试
        </h2>

        <div class="post-content-preview">
            下面就要用上一篇的内容的那个来做一个更为细致的实战了。

placekitten给猫奴的福利网站。全是喵星人。


当你输入为http://placekitten.com/1000/1000就获得一张1000*1000分辨率大小的喵星人图片了。


好的，我们现在就根据這个来小试牛刀。
## ...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on May 18, 2016</p>
</div>

<hr>

<div class="post-preview">
    <a href="/python%E7%88%AC%E8%99%AB/2016/05/17/Python-%E7%88%AC%E8%99%AB(2)-%E7%A5%9E%E8%AF%B4%E8%A6%81%E6%9C%89%E5%85%89/">
        <h2 class="post-title">
            爬虫(2) 神说要有光
        </h2>

        <div class="post-content-preview">
            爬虫是什么？
爬虫即为Web Spider，将其视作一种在网页中抓取数据的工具即可。想象我们常用的搜索引擎，当你输入关键字搜索的时候，爬虫就在搜寻含有你关键字信息的网页，按照一定规则排序呈现在你眼前。

URL与爬虫
爬虫抓取的是指定的网络资源、数据。读入并存储本地。按图索骥的图。用到的自然就...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on May 17, 2016</p>
</div>

<hr>

<div class="post-preview">
    <a href="/python%E7%88%AC%E8%99%AB/2016/05/15/Python-%E7%88%AC%E8%99%AB(1)-%E5%B7%A5%E6%AC%B2%E5%96%84%E5%85%B6%E4%BA%8B-%E5%BF%85%E5%85%88%E5%88%A9%E5%85%B6%E5%99%A8/">
        <h2 class="post-title">
            爬虫(1) 工欲善其事，必先利其器
        </h2>

        <div class="post-content-preview">
            准备用Python做点什么了。
开始学习用Python做一点爬虫玩。

为什么选择Python

  Python使你更关注问题，而不是弄明白语言本身。
  Python的功能强大，不需要考虑程序所需要的内存這样底层的细节。
  库丰富，功能模块這样的轮子别人已经造好了。
  Python可以...
        </div>
    </a>
    <p class="post-meta">Posted by Ada on May 15, 2016</p>
</div>

<hr>


<!-- Pager -->

<ul class="pager">


    <li class="next">
        <a href="/page2">Older Posts &rarr;</a>
    </li>

</ul>


		</div>
	</div>
</div>

<hr>


    <!-- Footer -->
<footer>
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                <ul class="list-inline text-center">
                    <!-- kill the Facebook and Weibo -->
                    <li>
                        <a href="/feed.xml">
                            <span class="fa-stack fa-lg">
                                <i class="fa fa-circle fa-stack-2x"></i>
                                <i class="fa fa-rss fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                    </li>



                    <li>
                        <a href="https://github.com/ada-hs">
                            <span class="fa-stack fa-lg">
                                <i class="fa fa-circle fa-stack-2x"></i>
                                <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                    </li>


                    <!--

                    -->

                    <!--

                    -->


                    <li>
                        <a target="_blank" href="https://www.zhihu.com/people/Adastaybrave">
                            <span class="fa-stack fa-lg">
                                <i class="fa fa-circle fa-stack-2x"></i>
                                <i class="fa  fa-stack-1x fa-inverse">知</i>
                            </span>
                        </a>
                    </li>

                    <!--

                    -->

                </ul>
                <p class="copyright text-muted">
                &copy; 2016  Ada ❖ Powered by Jekyll.
                </p>
            </div>
        </div>
    </div>
</footer>

<!-- jQuery -->
<script src="/js/jquery.min.js "></script>

<!-- Bootstrap Core JavaScript -->
<script src="/js/bootstrap.min.js "></script>

<!-- Custom Theme JavaScript -->
<script src="/js/clean-blog.min.js "></script>



<!-- Highlight.js -->
<script>
    async("http://cdn.bootcss.com/highlight.js/8.6/highlight.min.js",function(){
        hljs.initHighlightingOnLoad();
    })
</script>
<link href="http://cdn.bootcss.com/highlight.js/8.6/styles/github.min.css" rel="stylesheet">


</body>

</html>
"""

bsObj = BeautifulSoup(html,'html.parser')
print(bsObj.h1)