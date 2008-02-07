# coding=big5
#from wx import *

import wx._core as wx
from wx.html import *
import string

from blogtrans.data import Article

def make_html_list(list) :
  str = "<ul>"
  for item in list :
    str += "<li>" + item + "</li>"
  str += "</ul>"
  str += "<hr />"
  return str

class BlogHtmlWindow(HtmlWindow):
  def __init__(self, parent) :
    HtmlWindow.__init__(self,parent,wx.ID_ANY, style = wx.SIMPLE_BORDER)
    
  def ShowArticle(self, article) :
    info = []
    
    info.append(u"�@��: "+article.author )
    info.append(u"���D: "+article.title )
    info.append(u"���: "+article.date.strftime("%Y-%m-%d %H:%M:%S") )
    info.append(u"���O: "+string.join(article.category, ",") )
    
    if article.status==Article.PUBLISH : status = u"���}"
    elif article.status==Article.DRAFT : status = u"��Z"
    else : status = u"�p�K"
    info.append(u"���A: "+status)
    
    self.SetPage(make_html_list(info)+article.body+article.extended_body)
    
  def ShowComment(self, comment) :
    info = []
    
    info.append(u"�d����: " + comment.author )
    info.append(u"Email: " +comment.email )
    info.append(u"���}: " + comment.url)
    info.append(u"���: " + comment.date.strftime("%Y-%m-%d %H:%M:%S") )
    
    self.SetPage(make_html_list(info)+comment.body)
    