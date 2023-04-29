from django import template

register=template.Library()
@register.filter(name='swaping')
def swap(val):
    return val.swapcase()

@register.filter()
def remove(val,arg):
    return val.replace(arg,'')

@register.filter(name='count')
def counting(val,arg):
    c=0
    for i in range(len(val)):
        if arg==val[i:i+len(arg)]:
            c+=1
    return c



#register.filter('swaping',swap)
#register.filter('remove',remove)
#register.filter('count',counting)