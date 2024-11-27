from contextlib import closing
from xml.parsers.expat import ParserCreate


class XmlBpmnHandler(object):

    def startElementHandler(self, name, attrs,data):
        print("startElement: %s ,attr: %s" % (name, attrs))

    def endElementHandler(self, name):
        print("endElement: %s " % name)

    def charsHandler(self, data):
        print("characters: %s " % data)


def parse_xml(xml_str):
    handler = XmlBpmnHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.startElementHandler
    parser.CharacterDataHandler = handler.charsHandler
    parser.EndElementHandler = handler.endElementHandler
    parser.Parse(xml_str)


if __name__ == '__main__':
    with closing(open("extraTest.bpmn","r",encoding="utf-8")) as op:
        xml_str = op.read()
        parse_xml(xml_str)

