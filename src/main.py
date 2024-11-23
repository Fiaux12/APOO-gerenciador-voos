import flet as ft
import funcionalidades.cadastros.cadastros  as cadastros

body_content = ft.Column([ft.Text("Selecione uma opção no menu")], alignment=ft.MainAxisAlignment.START, expand=True)

def pilotos():
    return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("CPF")),
                ft.DataColumn(ft.Text("Gênero")),
                ft.DataColumn(ft.Text("Licença")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("João Ribeiro")),
                        ft.DataCell(ft.Text("456.789.321-85")),
                        ft.DataCell(ft.Text("Masculino")),
                        ft.DataCell(ft.Text("Carga")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Clarice Romano")),
                        ft.DataCell(ft.Text("782.663.751-28")),
                        ft.DataCell(ft.Text("Feminino")),
                        ft.DataCell(ft.Text("Passageiro")),
                    ]
                )
            ]
        )



def update_content(index, body_content):
    body_content.controls.clear() 

    if index == 0: 
        body_content.controls.append(ft.Text("Cadastrar Pilotos", size=20))
        body_content.controls.append(cadastros.cadastrar_piloto())

    elif index == 1: 
        body_content.controls.append(ft.Text("Cadastrar Comissários", size=20))
        body_content.controls.append(cadastros.cadastrar_comissario())

    elif index == 2:  
        body_content.controls.append(ft.Text("Criar Tripulação", size=20))

    elif index == 3: 
        body_content.controls.append(ft.Text("Cadastrar Aviões", size=20))
        body_content.controls.append(cadastros.cadastrar_aviao())

    elif index == 4:  
        body_content.controls.append(ft.Text("Criar Voo", size=20))

    body_content.update() 

def main(page: ft.Page):
    page.title = "Gerenciador de Voos"
    page.window_width = 1300
    page.window_height = 700
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    body_content = ft.Column(alignment=ft.MainAxisAlignment.START, expand=True)

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON_4_OUTLINED, selected_icon=ft.icons.PERSON_4_ROUNDED, label="Pilotos"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON_3_OUTLINED, selected_icon=ft.icons.PERSON_3_ROUNDED, label="Comissários"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.GROUPS_3_OUTLINED, selected_icon=ft.icons.GROUPS_3_ROUNDED, label="Tripulação"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FLIGHT_OUTLINED, selected_icon=ft.icons.FLIGHT, label="Aviões"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FLIGHT_TAKEOFF_OUTLINED, selected_icon=ft.icons.FLIGHT_TAKEOFF, label="Voos"
            ),
        ],
        on_change=lambda e: update_content(e.control.selected_index, body_content),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                body_content,
            ],
            width=1300,
            height=700,
        )
    )
    page.update()

ft.app(target=main)

