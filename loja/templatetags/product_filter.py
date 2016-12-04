from django.template import Library, Node
from .models import Produto

register = Library()
class Consultar_produtos(Node):
    def render(self, context):
        context['produto_loja'] = Produto.objects.all()
        return ''

    def get_produtos(parser, token):
        return Consultar_produtos()

    register.tag(get_produtos)
