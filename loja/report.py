# -*- coding: utf-8 -*-
# comentar se nao funcionar 
from xhtml2pdf import pisa 
from io import StringIO, BytesIO
from django.template.loader import get_template 
from django.template import Context 
from django.http import HttpResponse

def write_to_pdf(request, template_path, context): 
    template = get_template(template_path) 
    context = Context(context) 
    html = template.render(context) 
    result = BytesIO()
    pdf = pisa.pisaDocument(StringIO(html), dest = result)
    if not pdf.err: 
        return HttpResponse(result.getvalue(), content_type = 'application/pdf')
    else: 
        return HttpResponse('Não foi possivel gerar a impressao do comprovante')
    
