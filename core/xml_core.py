import xml.etree.cElementTree as ET


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def str_to_bool(data: str) -> bool:
    if data.lower() == 'true':
        return True
    elif data.lower() == 'false':
        return False
    else:
        return None


class parameters:
    def __init__(self, path: str):
        super(parameters, self).__init__()
        self.path: str = path
        self.tree: ET.ElementTree = None
        self.root: ET.Element = None
        self. m_attribute = ['line_x0', 'line_y0', 'line_z', 'line_radius', 'line_points', 'line_rect_a', 'line_rect_b']
        self.open_file()

    def open_file(self):
        try:
            self.tree = ET.parse(self.path)
            self.root: ET.Element = self.tree.getroot()
        except FileNotFoundError:
            pass

    def set(self, data: list):
        self.root = ET.Element('parameters')
        for i, value in enumerate(data):
            param = ET.Element(self.m_attribute[i])
            param.text = str(value)
            self.root.append(param)
        indent(self.root)
        self.tree = ET.ElementTree(self.root)
        self.save()

    def get(self) -> list:
        m_result = list()
        for i, attribute in enumerate(self.m_attribute):
            try:
                value = self.tree.find(attribute).text
                m_result.append(value)
            except AttributeError:
                return None
        return m_result

    def save(self):
        self.tree.write(self.path)
