from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("Testing Shiny App"),
    ui.input_text("txt", "Hello World"),
    ui.output_text_verbatim("txt_out")  # Changed to output_text_verbatim for proper text rendering
)

def server(input, output, session):
    @output
    @render.text
    def txt_out():
        return f"You entered: {input.txt()}"  # Accessing input text correctly

app = App(app_ui, server)