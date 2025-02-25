import flet as ft
import classes.pessoa.comissario_de_voo  as comissario
import classes.voo.tripulacao as tripulacao
import classes.pessoa.piloto as piloto

class ModuloTripulacao():
    def __init__(self) -> None:
        pass

    def criar_tripulacao():
        def button_clicked(e):
            piloto_selecionado_str = f"Pilotos selecionados: {piloto_selecionado_1.value}, {piloto_selecionado_2.value}\n"
            comissarios_selecionados = [
                dropdown.value for dropdown in dropdowns_comissarios if dropdown.value
            ]
            comissarios_selecionados_str = f"Comissários selecionados: {', '.join(comissarios_selecionados)}"
            t.value = piloto_selecionado_str + comissarios_selecionados_str

            try:
                tripulacao.Tripulacao.contruir_tripulacao(piloto_selecionado_1.value, piloto_selecionado_2.value, comissarios_selecionados)
                t.value = f"Tripuação cadastrada!"
                t.color = ft.Colors.GREEN

            except Exception as e:
                print(f"An exception occurred: {e}")
                t.value = f"{e}"
                t.color = ft.Colors.RED
                
            t.update()
            

        pilotos = piloto.Piloto.carregarLista()
        opcoes_pilotos = [ft.dropdown.Option(f"{piloto["nome"]}, {piloto["cpf"]}") for _, piloto in pilotos.iterrows()] if not pilotos.empty else []

        comissarios = comissario.ComissarioDeVoo.carregarLista()
        opcoes_comissarios = [ft.dropdown.Option(f"{comissario["nome"]}, {comissario["cpf"]}") for _, comissario in comissarios.iterrows()] if not comissarios.empty else []

        dropdowns_comissarios = []

        def atualizar_comissarios(e):
            quantidade = int(numero_comissarios.value) if numero_comissarios.value else 0
            lista_comissarios.controls.clear()
            dropdowns_comissarios.clear()
            lista_comissarios.controls.append(ft.Text("Selecione os comissários pelo nome e cpf", size=15))
            for i in range(quantidade):
                dropdown = ft.Dropdown(
                    width=500,
                    options=opcoes_comissarios,
                    hint_text=f"Comissário {i + 1}"
                )
                dropdowns_comissarios.append(dropdown)
                lista_comissarios.controls.append(dropdown)
            lista_comissarios.update()

        t = ft.Text()
        texto_piloto_1 = ft.Text("Selecione o piloto principal pelo nome e cpf", size=15)
        piloto_selecionado_1 = ft.Dropdown(width=500, options=opcoes_pilotos)

        texto_piloto_2 = ft.Text("Selecione o copiloto pelo nome e cpf", size=15)
        piloto_selecionado_2 = ft.Dropdown(width=500, options=opcoes_pilotos)

        texto_numero_comissarios = ft.Text("Selecione o número de comissários", size=15)
        numero_comissarios = ft.Dropdown(
            width=100,
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            on_change=atualizar_comissarios
        )

        lista_comissarios = ft.Column()

        return ft.Column(controls=[
            texto_piloto_1,
            piloto_selecionado_1,
            texto_piloto_2,
            piloto_selecionado_2,
            texto_numero_comissarios,
            numero_comissarios,
            lista_comissarios,
            ft.ElevatedButton(text="Cadastrar", on_click=button_clicked),
            t
        ])

    def dialog():
        def carregar_lista_tripulacoes():
            df = tripulacao.Tripulacao.carregarLista()

            rows = []
            for _, row in df.iterrows():
                comissarios = ', '.join(row["comissarios_voo"]) 
                pilotos = ', '.join(row["pilotos"]) 
                rows.append([row["id"],comissarios, pilotos])

            return rows

        rows = carregar_lista_tripulacoes()
        dlg = ft.AlertDialog(
            title=ModuloTripulacao.tripulacoesTable(rows), on_dismiss=lambda e: print("Dialog dismissed!")
        )

        def open_dlg(e):
            rows = carregar_lista_tripulacoes()
            dlg.title = ModuloTripulacao.tripulacoesTable(rows) 
            e.control.page.overlay.append(dlg)
            dlg.open = True
            e.control.page.update()

        return ft.Column(
            [
                ft.ElevatedButton("Visualizar Tripulações", on_click=open_dlg),
            ]
        )

    def tripulacoesTable(rows):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Identificação")),
                ft.DataColumn(ft.Text("Comissários")),
                ft.DataColumn(ft.Text("Pilotos")),
            ],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row]) for row in rows],
        )