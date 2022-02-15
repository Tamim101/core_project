from django.utils.html import escape

def row_details(self, pk, fields):
    obj = self.model.objects.get(pk=pk)
    json = {}
    html = '<table class="row-details">'
    for field in fields:
        try:
            value = escape(getattr(obj, field))
            json[field] = value
            html += '<tr><td>%s</td><td>%s</td></tr>' % (field, value)
        except Exception as e:
            pass
    html += '</table>'

    return {'html': html, 'json': json}





