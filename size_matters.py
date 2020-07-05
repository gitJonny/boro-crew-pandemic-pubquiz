import ipywidgets as widgets

def size_matters(question = 7):

    team_names = ['Judith and Simon',
                  'Rob and Jane',
                  'Louise',
                  'Jay and Diana',
                  'Elle and Phil',
                  'Laura',
                 ]
    
    all_answers = ['']
    if question == 1:
        f = open('sizematters_mrmen.txt', 'r')
    elif question == 2:
        f = open('sizematters_bond.txt', 'r')
    elif question == 3:
        f = open('sizematters_friends.txt', 'r')
    elif question == 4:
        f = open('sizematters_cities.txt', 'r')
    elif question == 5:
        f = open('sizematters_spicegirls.txt', 'r')
    elif question == 6:
        f = open('sizematters_harrypotter.txt', 'r')
    elif question == 7:
        f = open('sizematters_jedis.txt', 'r')
    elif question == 8:
        f = open('sizematters_strictly.txt', 'r')
    elif question == 9:
        f = open('sizematters_rugby.txt', 'r')
    elif question == 10:
        f = open('sizematters_thomas.txt', 'r')
        
    all_answers += f.read().split('\n')

    sorted_answers = sorted(all_answers, key = str.lower)
    lengths = [(len(item) 
                - item.count(' ')
                - item.count('.')
                - item.count(',')
                - item.count('!')
                - item.count('?')
                - item.count("'")
                - item.count('-')
                - item.count('(')
                - item.count(')')
               ) for item in sorted_answers]
    options = list(zip(sorted_answers, lengths))

    def dropdown_eventhandler(change, widget_to_update):
        widget_to_update.value = change.new

    def instantiate_widget(description):
        dropdown = widgets.Dropdown(options = options,
                                    description = description,
                                    style = {'description_width': '200px'},
                                    layout = widgets.Layout(width = '600px')
                                   )
        selected_answer_length = widgets.widgets.IntText(value = 0,
                                                         description = '',
                                                         layout = widgets.Layout(width = '50px')
                                                        )
        point = widgets.widgets.IntText(value = 0,
                                        description = '',
                                        layout = widgets.Layout(width = '50px')
                                       )
        dropdown.observe(lambda change : dropdown_eventhandler(change,selected_answer_length),
                        'value',
                        type = 'change'
                        )
        return dropdown, selected_answer_length, point

    def answer_button_click(b):
        max_answer_length = max(lengths)
        longest_answers = []
        answer_lengths = []
        for i in range(len(lengths)):
            if lengths[i] == max_answer_length:
                longest_answers.append(sorted_answers[i])

            ui_best_answer.value = f'{", ".join(longest_answers)} ({max_answer_length})'
        for i in range(len(team_names)):
            answer_lengths.append(selected_answer_lengths[i].value)
        for i in range(len(team_names)):
            value = selected_answer_lengths[i].value
            if value == 0:
                points[i].value = 0
            elif value == max_answer_length:
                points[i].value = 3
            elif value == max(answer_lengths):
                points[i].value = 2
            else:
                points[i].value = 1

    dropdowns = []
    selected_answer_lengths = []
    points = []

    for i in range(len(team_names)):
        dropdown, selected_answer_length, point = instantiate_widget(description = f'{team_names[i]} :')
        dropdowns.append(dropdown)
        selected_answer_lengths.append(selected_answer_length)
        points.append(point)

    ui_best_answer_button = widgets.Button(description = 'Best Answer :')
    ui_best_answer = widgets.Label('')

    ui_best_answer_button.on_click(answer_button_click)

    ui_dropdowns = widgets.VBox(dropdowns)
    ui_col1 = widgets.VBox([widgets.Label(''), ui_dropdowns])
    ui_answer_lengths = widgets.VBox(selected_answer_lengths)
    ui_col2 = widgets.VBox([widgets.Label('Length'), ui_answer_lengths])
    ui_points = widgets.VBox(points)
    ui_col3 = widgets.VBox([widgets.Label('Points'), ui_points])
    ui_top = widgets.HBox([ui_col1, ui_col2, ui_col3])
    ui_bottom = widgets.HBox([ui_best_answer_button, ui_best_answer])
    ui = widgets.VBox([ui_top, ui_bottom])
    display(ui)


