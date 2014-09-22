from django import template

register = template.Library()

# @register.filter
# def first(list):
#     if list is not None and len(list):
#         return list[0]
#
# @register.filter
# def suit(list, suit_type):
#     return [item for item in list if item.get_suit_display() == suit_type]
#
#
# @register.filter
# def aces(list, suit_type):
#     return [item for item in list if item.rank == suit_type]