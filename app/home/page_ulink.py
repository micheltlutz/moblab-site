from app.site_renderer.page import Page
from winged.HTML.div import Div
from winged.HTML.p import P
from winged.HTML.string import String
from winged.HTML.nav import Nav
from winged.HTML.a import A
from winged.HTML.ul import Ul
from winged.HTML.li import Li

class PageUlink():
    def _get_menu(self):
        return [
            {'url': 'moblab://moblab.micheltlutz.me/', 'label': 'Abrir App', 'target': '_self'},
            {'url': 'https://moblab.micheltlutz.me/', 'label': 'Abrir App', 'target': '_self'},
            {'url': 'moblab://moblab.micheltlutz.me/settings', 'label': 'Abrir App - Settings', 'target': '_self'},
            {'url': 'https://moblab.micheltlutz.me/settings', 'label': 'Abrir App - Settings', 'target': '_self'},
            {'url': 'https://github.com/micheltlutz/moblab-site', 'label': 'Git Site', 'target': '_blank'},
            {'url': 'https://github.com/micheltlutz/moblab-ios', 'label': 'Git App - iOS', 'target': '_blank'},
            # {'url': 'https://moblab.micheltlutz.me/login', 'label': 'LOGIN', 'target': '_self'},
        ]

    def _component_builder(self) -> Nav:
        nav = Nav(("class", "pa3 pa4-ns"))
        divMenu = Div(("class", "mike-menu"))
        divLine = Div(("class", "navbar-line"))

        menu_items = self._get_menu()
        total_items = len(menu_items)
        ul = Ul(("class", "mike-menu"))

        for index, item in enumerate(menu_items):
            li = Li()
            # Define as classes base que todos os itens terão
            classes = ["dim", "f6", "f5-ns", "dib", "mike-menu"]

            # Se não for o último item, adicione a classe 'mr3'
            if index < total_items - 1:
                classes.append("mr3")

            # Junta todas as classes em uma string separada por espaços
            classes_str = " ".join(classes)

            # Cria o elemento link com as classes apropriadas
            link = A(("href", item['url']),
                    ("target", item['target']),
                    ("class", classes_str)
                    )
            link.add(String(item['label']))
            li.add(link)
            ul.add(li)
            
        divMenu.add(ul)
        nav.add(divMenu)
        nav.add(divLine)

        divC = Div(("class", "container"))
        divC.add(nav)

        divContent = Div(("class", "content"))

        text = P()
        text.add(String("<center>This page is intended to be educational for testing web and mobile resources. <strong>If you want to collaborate, use the links >Git Site< e >Git App< </strong></center>"))
        divContent.add(text)

        divC.add(divContent)

        return divC

    def get_string(self) -> str:
        return self._component_builder().get_string()

    def generate(self):
        print(self._component_builder.get_string())
