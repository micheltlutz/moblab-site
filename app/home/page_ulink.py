from app.site_renderer.page import Page
from winged.HTML.div import Div
from winged.HTML.main import Main
from winged.HTML.h import H
from winged.HTML.string import String
from winged.HTML.nav import Nav
from winged.HTML.a import A
# from winged.HTML.ul import Ul
# from winged.HTML.li import li

class PageUlink():
    def _get_menu(self):
        return [
            {'url': 'oxxoapp://p18777908c1dev-store.occa.ocs.oraclecloud.com', 'label': 'com scheme', 'target': '_self'},
            {'url': 'https://p18777908c1dev-store.occa.ocs.oraclecloud.com', 'label': 'com https', 'target': '_self'},
            {'url': 'oxxoapp://p18777908c1dev-store.occa.ocs.oraclecloud.com', 'label': 'com scheme blank', 'target': '_blank'},
            {'url': 'https://p18777908c1dev-store.occa.ocs.oraclecloud.com', 'label': 'com https blank', 'target': '_blank'},
        ]

    def _component_builder(self) -> Nav:
        nav = Nav(("class", "pa3 pa4-ns"))
        divMenu = Div(("class", "tc pb3"))
        divLine = Div(("class", "navbar-line"))

        menu_items = self._get_menu()
        total_items = len(menu_items)

        for index, item in enumerate(menu_items):
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
            divMenu.add(link)

        nav.add(divMenu)
        nav.add(divLine)

        return nav

    def get_string(self) -> str:
        return self._component_builder().get_string()

    def generate(self):
        print(self._component_builder.get_string())
