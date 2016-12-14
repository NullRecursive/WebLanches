from xhtml2pdf import pisa 
import cStringIO as StringIO 
from django.template.loader import get_template 
from django.template import Context 
from django.http import HttpResponse
def write_to_pdf(request,template_path, context): 
    template = get_template(template_path) 
    context = Context(context) 
    html = template.render(context) 
    result = StringIO.StringIO() 
    pdf = pisa.pisaDocument(StringIO.StringIO(html),dest=result) 
    if not pdf.err: 
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    else: return HttpResponse('Errors')
    
