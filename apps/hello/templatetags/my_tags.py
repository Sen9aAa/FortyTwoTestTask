from django import template
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

register = template.Library()

def edit_link(my_instanse):
  return reverse('admin:%s_%s_change' % (my_instanse._meta.app_label,my_instanse._meta.module_name),
            args=(my_instanse.pk,)
)


register.simple_tag(edit_link)