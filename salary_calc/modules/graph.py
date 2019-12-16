from matplotlib import pyplot


class Graph:

    def __init__(self, par_1, par_2, par_3, par_4, par_5, par_6, par_1_brutto, par_2_brutto, par_3_brutto, par_4_brutto,
                 par_5_brutto, par_6_brutto):
        self.par_1 = par_1
        self.par_2 = par_2
        self.par_3 = par_3
        self.par_4 = par_4
        self.par_5 = par_5
        self.par_6 = par_6
        self.par_1_brutto = par_1_brutto
        self.par_2_brutto = par_2_brutto
        self.par_3_brutto = par_3_brutto
        self.par_4_brutto = par_4_brutto
        self.par_5_brutto = par_5_brutto
        self.par_6_brutto = par_6_brutto

    def get_x(self):
        x = []
        x.append(self.par_1)
        x.append(self.par_2)
        x.append(self.par_3)
        x.append(self.par_4)
        x.append(self.par_5)
        x.append(self.par_6)
        return x

    def get_y(self):
        y = []
        y.append(self.par_1_brutto)
        y.append(self.par_2_brutto)
        y.append(self.par_3_brutto)
        y.append(self.par_4_brutto)
        y.append(self.par_5_brutto)
        y.append(self.par_6_brutto)
        return y

    def draw_graph(self, graph_file):
        x = self.get_x()
        y = self.get_y()

        pyplot.plot(x, y)
        pyplot.title('Wynagrodzenia brutto-netto')
        pyplot.ylabel('Wynagrodzenia brutto')
        pyplot.xlabel('Wynagrodzenia netto')
        pyplot.savefig(graph_file)

