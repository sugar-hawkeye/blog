import markdown2
import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe



register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    lists = ["break-on-newline", "code-friendly", "code-color", "cuddled-lists", "fenced-code-blocks",
             "footnotes", "header-ids",  "markdown-in-html", "metadata",
             "nofollow", "numbering", "pyshell", "smarty-pants", "spoiler", "target-blank-links",
             "toc", "tables", "use-file-vars", "wiki-tables", "xml","tag-friendly"]
    # lists = ["break-on-newline","code-friendly","code-color","cuddled-lists","fenced-code-blocks",
    #          "footnotes","header-ids","html-classes","link-patterns","markdown-in-html","metadata",
    #          "nofollow","numbering","pyshell","smarty-pants","spoiler","target-blank-links",
    #          "toc","tables","use-file-vars","wiki-tables","xml","tag-friendly"]
    return mark_safe(markdown2.markdown(force_text(value),extras=lists))


@register.filter(is_safe=True)
@stringfilter
def pure_text(value):
    content = mark_safe(markdown2.markdown(force_text(value)))
    # content = content.replace('<h1>', '')
    # content = content.replace('</h1>', '')
    # content = content.replace('<h2>', '')
    # content = content.replace('</h2>','')
    # content = content.replace('<h3>', '')
    # content = content.replace('</h3>', '')
    # content = content.replace('"', '')
    # content = content.replace('<p>', '')
    # content = content.replace('</p>', '').strip().strip('"')

    # a = re.compile('<p>','</p>')
    content = re.sub(r'<h\d>','',content)
    content = re.sub(r'</h\d>', '', content)
    content = re.sub(r'<p>', '', content)
    content = re.sub(r'</p>', '', content)
    content = re.sub(r'\n\n', '', content)
    content = re.sub(r'\s+', '', content)

    return content
