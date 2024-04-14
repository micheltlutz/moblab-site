from app.site_renderer.page import Page
from winged.HTML.div import Div
from winged.HTML.string import String
from winged.HTML.nav import Nav
from winged.HTML.a import A
from winged.HTML.button import Button
from urllib.parse import quote

class PageLogin():
    def _get_menu(self):

        bundleId = "me.micheltlutz.MobLab"
        redirectUrl = "moblabapp://micheltlutz.me/logged"

        url = f"https://appleid.apple.com/auth/authorize?client_id={bundleId}&redirect_uri={quote(redirectUrl)}&response_type=code%20id_token&response_mode=form_post&scope=name%20email";
            

        return [
            {'url': url, 'id':'apple-signin_link', 'label': 'com scheme', 'target': '_self'},
        ]

    def _get_button_login(self) -> Div:
        divLogin = Div(("class", "tc pb3 login-container"))
        
        apple_button = Button(("class", "apple-login-button"), ("id", "apple-signin"), ("onclick", "document.getElementById('apple-signin').click();") )

        divLogin.add(apple_button)

        return divLogin

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
        nav.add(self._get_button_login())

        return nav

    def get_string(self) -> str:
        return self._component_builder().get_string()

    def generate(self):
        print(self._component_builder.get_string())
