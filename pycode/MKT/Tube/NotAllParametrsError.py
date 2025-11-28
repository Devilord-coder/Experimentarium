class NotAllParametrsError(Exception):
    def __init__(self, parent, *parametrs):
        super().__init__(f'Не заполнены поля: {', '.join(parametrs)}')
        parent.status.setText(f'Не заполнены поля: {', '.join(parametrs)}')
        parent.status.setStyleSheet('opacity: 0;')
        parent.status.setStyleSheet('background-color: rgb(150, 0, 0);')