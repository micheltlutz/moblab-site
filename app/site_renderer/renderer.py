from winged.HTML.html import Html
from winged.HTML.doctype import Doctype
from winged.HTML.head import Head
from winged.HTML.body import Body
from winged.HTML.string import String
from winged.HTML.link_rel import LinkRel
from winged.HTML.script import Script
from winged.HTML.meta import Meta
from winged.core.generic_element import ElementAbstract

class SiteRenderer:
    def __init__(self):
        self.elements = []

    def add_element(self, element: ElementAbstract):
        self.elements.append(element)

    def _make_links(self):
        list_links = ["/static/css/styles.css"]

        return list_links
    
    def _make_meta(self):
        list_meta = [{
            "name": "author",
            "content": "Michel Lutz"
            },
            {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1"
            },
            {
            "name": "appleid-signin-client-id",
            "content": "me.micheltlutz.MobLab"
            },
            {
            "name": "appleid-signin-scope",
            "content": "email"
            },
            {
            "name": "appleid-signin-redirect-uri",
            "content": "https://micheltlutz.me/logged"
            },
            {
            "name": "appleid-signin-use-popup",
            "content": "true"
            },
            ]

        return list_meta

    def _make_scripts(self):
        # list_scripts = []
        list_scripts = ["https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"]

        return list_scripts

    def _make_head(self):
        head_element = Head()

        # lambda to add multiple links from a _make_links() return using LinkRel
        list(map(lambda link: head_element.add(LinkRel(("rel", "stylesheet"), ("href", link))), self._make_links()))
        # lambda to add multiple meta tags from a _make_meta() return using Meta
        list(map(lambda meta: head_element.add(Meta(("name", meta["name"]), ("content", meta["content"]))), self._make_meta()))

        return head_element

    def _generate_seo_tags(self):
        pass

    def _make_body(self):
        body_element = Body()

        list(map(lambda element: body_element.add(element), self.elements))
        list(map(lambda script: body_element.add(Script(("src", script))), self._make_scripts()))

        return body_element

    def generate(self):
        doctype_declaration = Doctype()
        html = Html()
        html.add(self._make_head())
        html.add(self._make_body())

        return doctype_declaration.get_string() + html.get_string()
