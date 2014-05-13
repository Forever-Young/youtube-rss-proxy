# updated version of https://djangosnippets.org/snippets/1963/

from django.contrib.admin.filters import FieldListFilter
from django.db import models
from django.utils.translation import ugettext as _


def _register_front(cls, test, factory):
    cls._field_list_filters.insert(0, (test, factory))


FieldListFilter.register_front = classmethod(_register_front)


class NullListFilter(FieldListFilter):
    fields = (models.CharField, models.IntegerField, models.FileField)

    def test(cls, field):
        return field.null and isinstance(field, cls.fields) and not field._choices
    test = classmethod(test)

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = '%s__isnull' % field.name
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        super(NullListFilter, self).__init__(field, request, params, model, model_admin, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_val]

    def choices(self, cl):
        # bool(v) must be False for IS NOT NULL and True for IS NULL, but can only be a string
        for k, v in ((_('All'), None), (_('Has value'), ''), (_('Omitted'), '1')):
            yield {
                'selected': self.lookup_val == v,
                'query_string': cl.get_query_string({self.lookup_kwarg: v}),
                'display': k
            }


FieldListFilter.register_front(NullListFilter.test, NullListFilter)
