'''Generates a Table'''


class Table:

    def __init__(self, table_head, config=None):
        if config is None:
            self.config = {
                    'borders': True,
                    'center_header': True,
                    'horizontal_rule': '=',
                    'number_format': 'scientific'
                    }
        else:
            self.config = config

        self.table = []

        self.num_of_columns = len(table_head)
        self.num_of_rows = 0

    def __getitem__(self, indices):
        i = indices[0]
        j = indices[1]
        return self.table[i][j]

    def add_row(self, content):
        if not isinstance(content, list):
            raise TypeError('content of row must be list')
        if len(content) != self.columns:
            raise IndexError('number of columns in table must be consistent')
        for item in content:
            item = str(item)
        self.table.append(content)

    def del_row(self, row):
        self.table.remove(row)

    def update_element(self, indices, value):
        i = indices[0]
        j = indices[1]
        self.table[i][j] = str(value)

    def draw_table(self, output=None):
        if output is None:
            self.output = {
                    'LaTeX': False,
                    'ASCII': True
                    }
        else:
            self.output = output
