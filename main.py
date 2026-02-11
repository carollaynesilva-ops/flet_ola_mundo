import flet as ft 

def main (page: ft.Page): 
    page.title= "Meu primeiro app Flet"
    page.bgcolor = "#e010c8"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Carollayne"),
        ft.ElevatedButton("Clique Aqui")
    )

ft.run(main)