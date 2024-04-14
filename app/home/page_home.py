# from app.site_renderer.page import Page
from winged.HTML.div import Div
from winged.HTML.header import Header
from winged.HTML.main import Main
from winged.HTML.h import H
from winged.HTML.table import Table
from winged.HTML.string import String

class PageHome():
    # super().__init__("Michel Lutz Site", "This is Michel Lutz Site", ["home", "page", "meta", "tags"])

    def get_string(self):
        main = Main()
        divC = Div(("class", "container"))
        h = H("1")
        h.add(String("Logado"))
        divC.add(h)
        
        header = Header(("class", "tc pv4"))

        table = Table()
        table.add_table_headers(["Name", "Age", "Height", "Location"])  # Define headers

        table.add_row()
        table.add_in_row(String("John"))
        table.add_in_row(String("25"))
        table.add_in_row(String("1.80"))
        table.add_in_row(String("New York"))

        table.add_row()
        table.add_in_row(String("Maria"))
        table.add_in_row(String("23"))
        table.add_in_row(String("1.50"))
        table.add_in_row(String("New Jersey"))

        main.add(header)
        divC.add(table)
        main.add(divC)
        return main.get_string()
