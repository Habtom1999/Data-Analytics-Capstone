from shiny import App, ui

app_ui = ui.page_fluid(
    ui.h2("Testing Shiny App"),
    ui.input_text("txt", "Enter text"),
    ui.output_text("txt_out")
)

def server(input, output, session):
    @output
    @ui.render_text
    def txt_out():
        return f"You entered: {input.txt()}"

app = App(app_ui, server)