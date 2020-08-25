# -*- coding:utf-8 -*-
def sendWordpress(Title,Content,username,password,URL="lxzblog.xjqxz.top", status="publish", category=['未分类'], tag=['None']):
    from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
    from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
    from wordpress_xmlrpc.methods.users import GetUserInfo
    from wordpress_xmlrpc.methods import posts, taxonomies, media
    from wordpress_xmlrpc.compat import xmlrpc_client
    wp = Client('http://'+URL+'/xmlrpc.php', username, password)
    post = WordPressPost()
    post.title = Title
    post.content = Content
    post.post_status = status  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    post.terms_names = {
        'post_tag': tag,  # 文章所属标签，没有则自动创建
        'category': category  # 文章所属分类，没有则自动创建
    }
    post.id = wp.call(posts.NewPost(post))
sendWordpress("测试","使用python发布Wordpress",'xingzhili2007','Lxz20070822',category=["测试","python"])
